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
		<form action="#" role="form" id="form_status">
			<div class="col-sm-12">
				<input id="id" name="id" type="hidden" value="{{sts['id']}}"/>
				<h2>Status</h2>
				<div class="form-group desc">
					<label for="descricao">Descrição: </label><input id="descricao" type="text" name="descricao" class="form-control" value="{{sts['descricao']}}"/>
				</div>
				<div class="pull-right">
					<button type="button" class="btn btn-primary" id="btn_back_status">Voltar</button>
					<button type="button" class="btn btn-primary" id="btn_save_update_status">Salvar</button>
				</div>
			</div>
		</form>
	</body>
</html>