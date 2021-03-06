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
		<!-- <div class="container"> -->
			<div class="col-sm-12">
				<table class="table">
					<thead>
						<tr>
							<th>Usuário</th>
							<th>Nome</th>
							<th>Role</th>
							<th>Ações</th>
						</tr>
					</thead>
					<tbody>
						% for usuario in usuarios:
							<tr>
								<td>{{usuario['username']}}</td>
								<td>{{usuario['nome']}}</td>
								<td>{{usuario['role']}}</td>
								<td>
									<button type="button" class="btn btn-primary btn-xs btn_update_user" id="{{usuario['username']}}">Editar</button>
									<button type="button" class="btn btn-primary btn-xs btn_delete_user" id="{{usuario['username']}}">Excluir</button>
								</td>
							</tr>
						% end
					</tbody>
				</table>
				<div class="pull-right">					
					<button type="button" class="btn btn-primary" id="btn_new_user">Novo</button>
				</div>
			</div>
		<!-- </div> -->
	</body>
</html>