var login = function() {
	$("#btn_login").click(function (){
		doLogin()
	});
};

function doLogin(){
	var ajax = $.ajax({
		url: "/login/confirm",
		method: "POST",
		data: { 
			username : $("#user").val(),
			senha: $("#senha").val()
		},
		cache: false
	});
	
	ajax.done(function( response ) {
		var auth = JSON.parse(response).authenticated;
		console.log(auth)
		if(auth === 'false'){
			$( ".message" ).html("<span>Credenciais inválidas!</span>");
		} else {
			window.location = "/home";
		}
	});

	ajax.fail(function(jqXHR, textStatus) {
		$( ".message" ).html("<span>Erro ao realizar login - " + textStatus + "</span>");
	});
}

$(document).ready(login);