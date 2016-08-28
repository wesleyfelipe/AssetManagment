var contratosScript = function() {
	$("#btn_novo_contrato").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");		
		carregaPagina("/contratos/new");		
	});
	$("#btn_back_contrato").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/contratos");
	});
	$("#btn_create_contrato").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaContrato();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");			
			criaContrato("/contratos/new/save");
		}		
	});
	$(".btn_update_contrato").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagUpdateContrato("/contratos/update", $(this).attr('id'));
	});
	$(".btn_delete_contrato").click(function (){
		$( ".message" ).html("<span>Excluindo...</span>");
		delContrato("/contratos/delete", $(this).attr('id'));
	});
	$("#btn_save_update_contrato").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaContrato();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");
			atualizaContrato("/contratos/update/save");
		}
	});
};

function validaContrato() {
	var erro = false;	
	
	if ($("#descricao").val() == ""){
		erro = true;
		$(".desc").addClass("has-error");
	}else{
		$(".desc").removeClass("has-error");
	}
		
	if (erro){
		$(".message").html("<span>Favor preencher os campos indicados.</span>");
	}
	
	return erro;
}

function criaContrato(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			descricao : $("#descricao").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("<span>Contrato cadastrado com sucesso!</span>");
		carregaPagina("/contratos");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

function carregaPagUpdateContrato(urlPag, idContrato){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : idContrato
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("");
		$( ".conteudo" ).html( retHtml );
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao buscar contrato - " + textStatus + "</span>");
	});	
}

function delContrato(urlPag, idContrato){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : idContrato
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("Contrato excluido com sucesso!");
		carregaPagina("/contratos");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao excluir contrato - " + textStatus + "</span>");
	});	
}

function atualizaContrato(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : $("#id").val(),
			descricao : $("#descricao").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("<span>Contrato atualizado com sucesso!</span>");
		carregaPagina("/contratos");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

$(document).ready(contratosScript);