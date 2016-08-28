<!DOCTYPE html>
<html>
	<head>
		<title>Usuários</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="css/bootstrap.min.css">
		<script src="js/jquery-1.12.0.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/user.js"></script>
	</head>
	<body>
		<form action="#" role="form" id="form_user">
			<!-- <div class="container"> -->
				<div class="col-sm-12">
					<h2>Novo Usuário</h2>
					<div class="form-group nome">
						<label for='username'>Username*: </label><input id='username' type='text' name='username' required class="form-control">
					</div>
					<div class="form-group nome">
						<label for='nome'>Nome*: </label><input id='nome' type='text' name='nome' required class="form-control">
					</div>
					<div class="form-group">
						<label for='telefone'>Telefone: </label> <input id='telefone' type='text' name='telefone' class="form-control">
					</div>
					<div class="form-group">
						<label for='email_addr'>E-mail: </label> <input id='email_addr' type='text' name='email_addr' class="form-control">
					</div>
					<div class="form-group senha">
						<label for='senha'>Senha*: </label> <input id='senha' type='password' name='senha' required class="form-control">
					</div>
					<div class="form-group">
						<label for='role'>Perfil*: </label>
						<select id='role' name='role' class="form-control">
							<option value="user" selected="selected">user</option>
							<option value="admin">admin</option>
						</select>
					</div>
					<div class="pull-right">						
						<button type="button" class="btn btn-primary" id="btn_back_user">Voltar</button>						
						<button type="button" class="btn btn-primary" id="btn_create_user">Cadastrar</button>
					</div>
				</div>
			<!-- </div> -->
		<form>
	</body>
</html>