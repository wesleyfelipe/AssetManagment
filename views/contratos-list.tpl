<!DOCTYPE html>
<html>
	<head>
		<title>Contratos</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="css/bootstrap.min.css">
		<script src="js/jquery-1.12.0.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/contratos.js"></script>
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
						% for contratos in contratosList:
							<tr>
								<td>{{contratos['id']}}</td>
								<td>{{contratos['descricao']}}</td>
								<td>
									<button type="button" class="btn btn-primary btn-xs btn_update_contrato" id="{{contratos['id']}}">Editar</button>
									<button type="button" class="btn btn-primary btn-xs btn_delete_contrato" id="{{contratos['id']}}">Excluir</button>
								</td>
							</tr>
						% end
					</tbody>
				</table>
				<div class="pull-right">					
					<button type="button" class="btn btn-primary" id="btn_novo_contrato">Novo</button>
				</div>
			</div>
		<!-- </div> -->
	</body>
</html>