var main = function() {
	$("a").click(function (){
		var activeMenu = $(".active");
		activeMenu.removeClass("active");
		$(this).addClass("active");
		$(this).blur();
	});
	
	/* interacoes menu */
	$("#menu_ativos").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/ativo");
	});
	$("#menu_contratos").click(function (){		
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/contratos");
	});
	$("#menu_status").click(function (){
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/status");
	});
	$("#menu_usuarios").click(function (){		
		$( ".message" ).html("<span>Carregando...</span>");
		carregaPagina("/user");
	});
	$("#menu_logout").click(function (){		
		$( ".message" ).html("<span>Saindo...</span>");
		logout('/logout');
	});	
	
	$(".active").trigger("click");
};

function carregaPagina(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",		
		cache: false
	});
	
	ajax.done(function( retHtml ) {
		$( ".conteudo" ).html( retHtml );
		$( ".message").html("");
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".conteudo" ).html( "<p>Erro ao carregar pagina - " + textStatus + "</p>" );
		$( ".message").html("");
	});
}

function logout(urlPag){
	var ajax = $.ajax({
		url: urlPag,
		method: "POST",		
		cache: false
	});
	
	ajax.done(function() {
		window.location = '/';
	});
	ajax.fail(function(jqXHR, textStatus) {
		$( ".conteudo" ).html( "<p>Erro ao carregar pagina - " + textStatus + "</p>" );
		$( ".message").html("");
	});
}

function er_replace( pattern, replacement, subject ){
	return subject.replace( pattern, replacement );
}

$(document).ready(main);