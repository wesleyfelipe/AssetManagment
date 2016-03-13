<html>
	<head>
		<title>Usuários</title>
		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
	</head>
	<body>
		<form action='new/save' role="form">
			<div class="container">
				<h1>Usuários</h1>
				<div class="form-group">
					<label for='nome'>Nome: </label><input id='nome' type='text' name='nome' required class="form-control">
				</div>
				<div class="form-group">
					<label for='telefone'>Telefone: </label> <input id='telefone' type='text' name='telefone' class="form-control">
				</div>
				<div class="form-group">
					<label for='senha'>Senha: </label> <input id='senha' type='text' name='senha' required class="form-control">
				</div>
				<div class="form-group">
					<label for='role'>Perfil: </label>
					<select id='role' name='role' class="form-control">
						<option value="FUN" selected="selected">Funcionário</option>
						<option value="ADM">Administrador</option>
					</select>
				</div>
				<div class="pull-right">
					<a href="/app/user"><button type="button" class="btn">Voltar</button></a>
					<button type="submit" class="btn btn-primary">Salvar</button>
				</div>
			</div>
		<form>
	</body>
</html>