var ativo = function() {
	$("#btn_novo_ativo").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");		
		carregaPagina("/ativo/new");		
	});
	$("#btn_back_ativo").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/ativo");
	});
	$("#btn_cria_ativo").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaAtivo();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");			
			criaAtivo("/ativo/new/save");
		}		
	});
	$(".btn_update_ativo").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");		
		carregaPagUpdateAtivo("/ativo/update", $(this).attr('id'));
	});
	$(".btn_delete_ativo").click(function (){
		$( ".message" ).html("<span>Excluindo...</span>");
		delAtivo("/ativo/delete", $(this).attr('id'));
	});
	$("#btn_save_update_ativo").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaAtivo();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");
			atualizaAtivo("/ativo/update/save");
		}
	});
	$("#btn_buscar_ativo").click(function (){
		erro = validaBusca();
		
		if (!erro) {
			$(".message").html("<span>Buscando...</span>");
			
			buscaAtivos("/ativo/busca");
		}
	});
	$("#valor_ativo").keyup(function() {		
		var valor = $( this );
		valor.val( er_replace( /[^0-9]+/g,'', valor.val() ) );
	});
	$("#valor_ativo").keyup(function() {		
		var valor = $( this );
		valor.val( er_replace( /[^0-9]+/g,'', valor.val() ) );
	});
	$("#depreciacao_ativo").keyup(function() {		
		var valor = $( this );
		valor.val( er_replace( /[^\.0-9]+/g,'', valor.val() ) );
	});
};

function validaAtivo() {
	var erro = false;	
	
	if ($("#desc").val() == ""){
		erro = true;
		$(".desc").addClass("has-error");
	}
	else{
		$(".desc").removeClass("has-error");
	}
	
	if ($("#valor").val() == ""){
		erro = true;
		$(".valor").addClass("has-error");
	}
	else{
		$(".valor").removeClass("has-error");
	}
	
	if ($("#dt_compra").val() == ""){
		erro = true;
		$(".dt_compra").addClass("has-error");
	}
	else{
		$(".dt_compra").removeClass("has-error");
	}
	
	if (erro){
		$(".message").html("<span>Favor preencher os campos indicados.</span>");
	}
	
	return erro;
}

function validaBusca() {
	var erro = false;

	if ($("#busca").val() == ""){
		erro = true;
		$(".busca").addClass("has-error");
	}
	else{
		$(".busca").removeClass("has-error");
	}
	
	if (erro) {
		$(".message").html("<span>Favor preencher o campo de busca.</span>");
	}
	
	return erro;
}

function criaAtivo(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			desc : $("#desc").val(),
			valor : $("#valor").val(),
			dt_compra : $("#dt_compra").val(),
			depreciacao : $("#depreciacao").val(),					
			status : $("#status").val(),
			contrato : $("#contrato").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("<span>Ativo cadastrado com sucesso!</span>");
		carregaPagina("/ativo");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

function carregaPagUpdateAtivo(urlPag, idAtivo){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : idAtivo
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("");
		$( ".conteudo" ).html( retHtml );
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao buscar ativo - " + textStatus + "</span>");
	});	
}

function delAtivo(urlPag, idAtivo){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : idAtivo
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("Ativo excluido com sucesso!");
		carregaPagina("/ativo");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao excluir ativo - " + textStatus + "</span>");
	});	
}

function atualizaAtivo(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : $("#id").val(),
			desc : $("#desc").val(),
			valor : $("#valor").val(),
			dt_compra : $("#dt_compra").val(),
			depreciacao : $("#depreciacao").val(),			
			status : $("#status").val(),
			contrato : $("#contrato").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("<span>Ativo atualizado com sucesso!</span>");
		carregaPagina("/ativo");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

function buscaAtivos(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			busca : $("#busca").val(),
			filtro_busca : $("#filtro_busca").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {		
		$( ".message").html("");
		$( "#tab_linhas_ativo").find("tr:gt(0)").remove();
		$( "#tab_linhas_ativo > tbody:last-child").append(retHtml);		
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro na busca - " + textStatus + "</span>");
	});
}

$(document).ready(ativo);