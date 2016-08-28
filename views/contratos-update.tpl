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
		<form action="#" role="form" id="form_contratos">
			<div class="col-sm-12">
				<input id="id" name="id" type="hidden" value="{{ctr['id']}}"/>
				<h2>Contrato</h2>
				<div class="form-group desc">
					<label for="descricao">Descrição: </label><input id="descricao" type="text" name="descricao" class="form-control" value="{{ctr['descricao']}}"/>
				</div>
				<div class="pull-right">
					<button type="button" class="btn btn-primary" id="btn_back_contrato">Voltar</button>
					<button type="button" class="btn btn-primary" id="btn_save_update_contrato">Salvar</button>
				</div>
			</div>
		</form>
	</body>
</html>