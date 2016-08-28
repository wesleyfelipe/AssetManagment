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
					<h2>Usuário</h2>
					<div class="form-group nome">
						<label for='username'>Username*: </label><input id='username' type='text' name='username' required class="form-control" value="{{usuario['username']}}" disabled="true">
					</div>
					<div class="form-group nome">
						<label for="nome">Nome*: </label><input id="nome" type="text" name="nome" value="{{usuario['nome']}}" required class="form-control">
					</div>
					<div class="form-group">
						<label for="telefone">Telefone: </label> <input id="telefone" type="text" name="telefone" value="{{usuario['telefone']}}" class="form-control">
					</div>
					<div class="form-group">
						<label for='email_addr'>E-mail: </label> <input id='email_addr' type='text' name='email_addr' class="form-control" value="{{usuario['email_addr']}}">
					</div>
					<div class="form-group">
						<label for="role">Perfil*: </label>
						<select id="role" name="role" value="{{usuario['role']}}" class="form-control">
							<option value="user" {{!'selected="selected"' if usuario['role'] == 'user' else ""}}>user</option>
							<option value="admin" {{!'selected="selected"' if usuario['role'] == 'admin' else ""}}>admin</option>
						</select>
					</div>
					<div class="pull-right">
						<button type="button" class="btn btn-primary" id="btn_back_user">Voltar</button>
						<button type="button" class="btn btn-primary" id="btn_save_update_user">Salvar</button>
					</div>
				</div>
			<!-- </div> -->
		<form>
	</body>
</html>