var user = function() {
	/* interacoes botoes */
	$("#btn_new_user").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/user/new");
	});
	$("#btn_back_user").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/user");
	});
	$("#btn_create_user").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaUsuario();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");			
			criaUsuario("/user/new/save");
		}		
	});
	$(".btn_update_user").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");		
		carregaPagUpdateUser("/user/update", $(this).attr('id'));
	});
	$(".btn_delete_user").click(function (){
		$( ".message" ).html("<span>Excluindo...</span>");
		delUsuario("/user/delete", $(this).attr('id'));
	});
	$("#btn_save_update_user").click(function (){
		var erro = false;
		
		$(".message").html("<span>Validando...</span>");
		
		erro = validaUsuario();
		
		if (!erro) {
			$(".message").html("<span>Salvando...</span>");
			atualizaUsuario("/user/update/save");
		}		
	});
	$('#username').on('keypress', function(e) {
        if (e.which == 32)
            return false;
    });
};

function validaUsuario() {
	var erro = false;
		
	if ($("#nome").val() == ""){
		erro = true;
		$(".nome").addClass("has-error");
	}
	else{
		$(".nome").removeClass("has-error");
	}
	
	if ($("#senha").val() == ""){
		erro = true;
		$(".senha").addClass("has-error");
	}
	else{
		$(".senha").removeClass("has-error");
	}
	
	if (erro){
		$(".message").html("<span>Favor preencher os campos indicados.</span>");
	}
	
	return erro;
}

function criaUsuario(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			nome : $("#nome").val(),
			username : $("#username").val(),
			telefone : $("#telefone").val(),
			senha: $("#senha").val(),
			email_addr : $("#email_addr").val(),
			role: $("#role").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		var result = JSON.parse(retHtml).result;
		console.log(retHtml)
		if(result === 'success'){
			$( ".message").html("<span>Usuario cadastrado com sucesso!</span>");
			carregaPagina("/user");
		} else {
			$( ".message" ).html("<span>Erro ao salvar - " + result + "</span>");
		}
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

function carregaPagUpdateUser(urlPag, username){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			username : username
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("");
		$( ".conteudo" ).html( retHtml );
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao buscar usuario - " + textStatus + "</span>");
	});	
}

function delUsuario(urlPag, username){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			username : username
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("Usuario excluido com sucesso!");
		carregaPagina("/user");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao excluir usuario - " + textStatus + "</span>");
	});	
}

function atualizaUsuario(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",
		data: { 
			username : $('#username').val(),
			nome : $("#nome").val(),
			telefone : $("#telefone").val(),
			email_addr: $("#email_addr").val(),
			role: $("#role").val()
		},
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".message").html("<span>Usuario atualizado com sucesso!</span>");
		carregaPagina("/user");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao salvar - " + textStatus + "</span>");
	});
}

$(document).ready(user);