<!DOCTYPE html>
% stts = {}
% for s in status:
	% stts[s['id']] = s['descricao']
% end
% ctrs = {}
% for c in contratos:
	% ctrs[c['id']] = c['descricao']
% end
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
		<div class="col-sm-12">
			<div class="col-sm-9">				
				<div class="form-group busca">
					<input id="busca" type="text" name="busca" value="" class="form-control">						
				</div>				
			</div>
			<div class="col-sm-2">
				<div class="form-group campo_busca">
					<select id="filtro_busca" name="filtro_busca" value="" class="form-control">
						<option value="id" >Id</option>
						<option value="descricao" >Descrição</option>
						<option value="status" >Status</option>
						<option value="data_compra" >Data de Compra</option>
					</select>
				</div>
			</div>
			<div class="col-sm-1">
				<div class="pull-right">
					<button type="button" class="btn btn-primary" id="btn_buscar_ativo">Buscar</button>
				</div>
			</div>
			<table class="table" id="tab_linhas_ativo">
				<thead>
					<tr>
						<th>ID</th>
						<th>Descrição</th>
						<th>Valor</th>
						<th>Data de Compra</th>
						<th>Depreciação</th>
						<th>Status</th>
						<th>Contrato</th>
					</tr>
				</thead>
				<tbody>
					% for atv in ativos:
						<tr>
							<td>{{atv['id']}}</td>
							<td>{{atv['descricao']}}</td>
							<td>{{atv['valor']}}</td>
							<td>{{atv['data_compra']}}</td>
							<td>{{atv['depreciacao']}}</td>
							<td>{{stts[atv['id_status']]}}</td>
							<td>{{ctrs[atv['id_contrato']]}}</td>
							<td>
								<button type="button" class="btn btn-primary btn-xs btn_update_ativo" id="{{atv['id']}}">Editar</button>
								<button type="button" class="btn btn-primary btn-xs btn_delete_ativo" id="{{atv['id']}}">Excluir</button>
							</td>
						</tr>
					% end
				</tbody>				
			</table>
			<div class="pull-right">					
				<button type="button" class="btn btn-primary" id="btn_novo_ativo">Novo</button>
			</div>
		</div>
	</body>
</html>