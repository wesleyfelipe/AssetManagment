<!DOCTYPE html>
<html>
	<head>
		<title>Login</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="css/bootstrap.min.css">
		<script src="js/jquery-1.12.0.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/main.js"></script>
		<script src="js/login.js"></script>
	</head>
	<body>
		<form action="#" role="form" id="form_login">
			<div class="container">
				<div class="col-sm-4"></div>
				<div class="col-sm-4">
					<h2>Login</h2>
					<div class="message"></div>
					<div class="form-group user">
						<label for='user'>Usuário: </label><input id='user' type='text' name='user' required class="form-control">
					</div>
					<div class="form-group senha">
						<label for='senha'>Senha: </label><input id='senha' type='password' name='senha' required class="form-control">
					</div>
					<div class="pull-right">					
						<button type="button" class="btn btn-primary" id="btn_login">Login</button>						
					</div>
				</div>
				<div class="col-sm-4"></div>
			</div>
		<form>
	</body>
</html>