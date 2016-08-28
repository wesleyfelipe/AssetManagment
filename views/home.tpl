<!DOCTYPE html>
<html>
	<head>
		<title>Asset Management</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta http-equiv="Cache-control" content="no-cache">
		<meta http-equiv="Expires" content="-1">
		<link rel="stylesheet" href="css/bootstrap.min.css">
		<link rel="stylesheet" href="css/style.css">
		<script src="js/jquery-1.12.0.min.js"></script>
		<script src="js/bootstrap.min.js"></script>
		<script src="js/main.js"></script>
		<script src="js/user.js"></script>
		<script src="js/ativo.js"></script>
		<script src="js/status.js"></script>
		<script src="js/contratos.js"></script>
	</head>
	<body>
		<div class="container">
			<header>
				<div class="col-sm-12">
					<h1>Asset Management</h1>				
				</div>
			</header>
			<div class="col-sm-12">
				<ul class="menu">
					<li><a href="#" id="menu_ativos" class="active">Ativos</a></li>
					% if (role == 'admin'):
					<li><a href="#" id="menu_contratos" >Contratos</a></li>
					<li><a href="#" id="menu_status">Status</a></li>
					<li><a href="#" id="menu_usuarios" >Usuários</a></li>
					% end
					<li class="logout"><a href="#" id="menu_logout">Sair</a></li>
				</ul>
			</div>
			<div class="col-sm-12 message">
			</div>
			<div class="col-sm-12 conteudo">
			</div>
		</div>
	</body>
</html>