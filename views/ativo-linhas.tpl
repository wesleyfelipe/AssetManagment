% stts = {}
% for s in status:
	% stts[s['id']] = s['descricao']
% end
% ctrs = {}
% for c in contratos:
	% ctrs[c['id']] = c['descricao']
% end
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
<script>ativo();</script>