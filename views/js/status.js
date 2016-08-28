var statusScript = function() {
	$("#btn_novo_status").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");		
		carregaPagina("/status/new");		
	});
	$("#btn_back_status").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/status");
	});
	$("#btn_create_status").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaStatus();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");			
			criaStatus("/status/new/save");
		}		
	});
	$(".btn_update_status").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagUpdateStatus("/status/update", $(this).attr('id'));
	});
	$(".btn_delete_status").click(function (){
		$( ".message" ).html("<span>Excluindo...</span>");
		delStatus("/status/delete", $(this).attr('id'));
	});
	$("#btn_save_update_status").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaStatus();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");
			atualizaStatus("/status/update/save");
		}
	});
};

function validaStatus() {
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

function criaStatus(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			descricao : $("#descricao").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("<span>Status cadastrado com sucesso!</span>");
		carregaPagina("/status");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

function carregaPagUpdateStatus(urlPag, idStatus){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : idStatus
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("");
		$( ".conteudo" ).html( retHtml );
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao buscar status - " + textStatus + "</span>");
	});	
}

function delStatus(urlPag, idStatus){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			id : idStatus
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("Status excluido com sucesso!");
		carregaPagina("/status");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao excluir status - " + textStatus + "</span>");
	});	
}

function atualizaStatus(urlPag){
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
		$( ".message").html("<span>Status atualizado com sucesso!</span>");
		carregaPagina("/status");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

$(document).ready(statusScript);