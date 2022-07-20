<?php
echo '<head>';
echo	'<meta charset="utf-8">';
echo	'<meta http-equiv="X-UA-Compatible" content="IE=edge">';
echo    '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
echo	'<link rel="stylesheet" href="estilo.css">';
echo	'<link rel="preconnect" href="https://fonts.googleapis.com">';
echo	'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>';
echo	'<link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital@1&display=swap" rel="stylesheet">';
echo	'<title>Fim do jogo</title>';
echo '</head>';

session_start();

$totalPontosJogador = $_SESSION['totalPontosJogador'];

arsort($totalPontosJogador);

echo '<div class="destaque borda">';
echo 'Fim do jogo!';
echo '</div>';

echo '<br>';

echo '<div class="borda">';
echo 'Estatísticas da partida:';
echo '<br>';
foreach ($totalPontosJogador as $jogador => $pontos) {
	echo '<br>O jogador ' . $jogador . ' fez <b>' . $pontos . '</b> pontos!';
}
echo '</div>';

session_destroy();

echo '<form action="telaInicial.php" method="">';
echo '<br><input class="button" type="submit" value="Novo jogo">';
echo '</form>';
