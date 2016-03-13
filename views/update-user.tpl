<html>
	<head>
		<title>Usuários</title>
		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
	</head>
	<body>
		<form action='update/save' role="form">
			<div class="container">
				<input id='id' name='id' type='hidden' value='{{usuario['id']}}'/>
				<h1>Usuários</h1>
				<div class="form-group">
					<label for='nome'>Nome: </label><input id='nome' type='text' name='nome' value='{{usuario['nome']}}' required class="form-control">
				</div>
				<div class="form-group">
					<label for='telefone'>Telefone: </label> <input id='telefone' type='text' name='telefone' value='{{usuario['telefone']}}' class="form-control">
				</div>
				<div class="form-group">
					<label for='senha'>Senha: </label> <input id='senha' type='text' name='senha' value='{{usuario['senha']}}' required class="form-control">
				</div>
				<div class="form-group">
					<label for='role'>Perfil: </label>
					<select id='role' name='role' value='{{usuario['role']}}' class="form-control">
						<option value="FUN" {{!'selected="selected"' if usuario['role'] == 'FUN' else ""}}>Funcionário</option>
						<option value="ADM" {{!'selected="selected"' if usuario['role'] == 'ADM' else ""}}>Administrador</option>
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