<!DOCTYPE html>
<html>

<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="stylesheet" href="estilo.css">
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital@1&display=swap" rel="stylesheet">
	<title>Tela inicial</title>
</head>

<body>
	<form action="jogo.php" method="post">
		Jogo:
		<select name="jogo" id="jogo">
			<option value="1">Paciência</option>
		</select>
		<br><br>
		Número de jogadores:
		<select name="qtdJogadores" id="jogo">
			<option value="2">2 jogadores</option>
			<option value="3">3 jogadores</option>
			<option value="4">4 jogadores</option>
		</select>
		<br><br>
		Quantidade de dados:
		<select name="qtdDados" id="jogo">
			<option value="1">1</option>
			<option value="2">2</option>
		</select>
		<br><br>
			<input class="button" type="submit" value="Iniciar">
</body>

</html>