<!DOCTYPE html>
<html>
	<head>
		<title>Status</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="css/bootstrap.min.css">
		<script src="js/jquery-1.12.0.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/status.js"></script>
	</head>
	<body>
		<!-- <div class="container"> -->
			<div class="col-sm-12">
				<table class="table">
					<thead>
						<tr>
							<th>Id</th>
							<th>Descrição</th>
							<th>Ações</th>
						</tr>
					</thead>
					<tbody>
						% for status in statusList:
							<tr>
								<td>{{status['id']}}</td>
								<td>{{status['descricao']}}</td>
								<td>
									<button type="button" class="btn btn-primary btn-xs btn_update_status" id="{{status['id']}}">Editar</button>
									<button type="button" class="btn btn-primary btn-xs btn_delete_status" id="{{status['id']}}">Excluir</button>
								</td>
							</tr>
						% end
					</tbody>
				</table>
				<div class="pull-right">					
					<button type="button" class="btn btn-primary" id="btn_novo_status">Novo</button>
				</div>
			</div>
		<!-- </div> -->
	</body>
</html>