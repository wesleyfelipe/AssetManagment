<!DOCTYPE html>
<html>
	<head>
		<title>Ativo</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<link rel="stylesheet" href="css/bootstrap.min.css">
		<script src="js/jquery-1.12.0.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/ativo.js"></script>
	</head>
	<body>
		<form action="#" role="form" id="form_ativo">
			<div class="col-sm-12">
				<input id="id" name="id" type="hidden" value="{{ativo['id']}}"/>
				<h2>Ativo</h2>
				<div class="form-group desc">
					<label for="desc">Descrição: </label><input id="desc" type="text" name="desc" value="{{ativo['descricao']}}" class="form-control">
				</div>
				<div class="form-group valor">
					<label for="valor">Valor: </label><input id="valor" type="text" name="valor" value="{{ativo['valor']}}" class="form-control">
				</div>
				<div class="form-group dt_compra">
					<label for="dt_compra">Data de Compra: </label><input id="dt_compra" type="text" name="dt_compra" value="{{ativo['data_compra']}}" class="form-control">
				</div>				
				<div class="form-group">
					<label for="depreciacao">Depreciação: </label><input id="depreciacao" type="text" name="depreciacao" value="{{ativo['depreciacao']}}" class="form-control">
				</div>				
				<div class="form-group status">
					<label for="status">Status: </label>
					<select id="status" name="status" value="" class="form-control">
						% for stt in status:
						<option value="{{stt['id']}}" {{!'selected="selected"' if ativo['id_status'] == stt['id'] else ''}} >{{stt['descricao']}}</option>
						% end
					</select>
				</div>
				<div class="form-group contrato">
					<label for="contrato">Contrato: </label>
					<select id="contrato" name="contrato" value="" class="form-control">
						% for ctr in contratos:
						<option value="{{ctr['id']}}" {{!'selected="selected"' if ativo['id_contrato'] == ctr['id'] else ''}} >{{ctr['descricao']}}</option>
						% end
					</select>
				</div>				
				<div class="pull-right">
					<button type="button" class="btn btn-primary" id="btn_back_ativo">Voltar</button>
					<button type="button" class="btn btn-primary" id="btn_save_update_ativo">Salvar</button>
				</div>
			</div>
		</form>
	</body>
</html>