<html>
	<head>
		<title>Usuários</title>
		<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
		<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="container">
			<h1>Usuários</h1>
			<table class="table">
				<thead>
					<tr>
						<th>Id</th>
						<th>Nome</th>
						<th>Telefone</th>
						<th>Senha</th>
						<th>Role</th>
						<th>Ações</th>
					</tr>
				</thead>
				<tbody>
					% for usuario in usuarios:
						<tr>
							<td>{{usuario['id']}}</td>
							<td>{{usuario['nome']}}</td>
							<td>{{usuario['telefone']}}</td>
							<td>{{usuario['senha']}}</td>
							<td>{{usuario['role']}}</td>
							<td>
								<a href="/app/user/update?id={{usuario['id']}}"><button type="button" class="btn btn-primary btn-xs">Editar</button></a>
								<a href="/app/user/delete?id={{usuario['id']}}"><button type="button" class="btn btn-primary btn-xs">Excluir</button></a>
							</td>
						</tr>
					% end
				</tbody>
			</table>
			<div class="pull-right">
				<a href="/app/home"><button type="button" class="btn">Voltar</button></a>
				<a href="/app/user/new"><button type="button" class="btn btn-primary">Novo</button></a>
			</div>
		</div>
	</body>
</html>