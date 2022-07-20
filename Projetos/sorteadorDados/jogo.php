<?php

echo '<head>';
echo	'<meta charset="utf-8">';
echo	'<meta http-equiv="X-UA-Compatible" content="IE=edge">';
echo    '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
echo	'<link rel="stylesheet" href="estilo.css">';
echo	'<link rel="preconnect" href="https://fonts.googleapis.com">';
echo	'<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>';
echo	'<link href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital@1&display=swap" rel="stylesheet">';
echo	'<title>Jogo</title>';
echo '</head>';

if (session_id() == '' || !isset($_SESSION) || session_status() === PHP_SESSION_NONE) {
	session_start();

	if (!isset($_SESSION['jogo'])) {
		$_SESSION['jogo'] = 0;
		$_SESSION['qtdJogadores'] = 0;
		$_SESSION['qtdDados'] = 0;
		$_SESSION['rodadaAtual'] = 0;
		$_SESSION['jogadorAtual'] = 0;
		$_SESSION['ultimoJogador'] = 0;
		$_SESSION['totalPontosJogador'] = array();
	}
}

if ($_SESSION['jogo'] === 0) {
	$jogo = (int) $_POST['jogo'];
	$qtdJogadores = (int) $_POST['qtdJogadores'];
	$qtdDados = (int) $_POST['qtdDados'];

	$_SESSION['jogo'] = $jogo;
	$_SESSION['qtdJogadores'] = $qtdJogadores;
	$_SESSION['qtdDados'] = $qtdDados;
} else {
	$jogo = $_SESSION['jogo'];
	$qtdJogadores = $_SESSION['qtdJogadores'];
	$qtdDados = $_SESSION['qtdDados'];
}

if ($_SESSION['rodadaAtual'] === 0) {
	$rodadaAtual = 0;
	$jogadorAtual = 1;
	$dado = array();
	$ultimoJogador = 0;

	$_SESSION['rodadaAtual'] = $rodadaAtual;
	$_SESSION['jogadorAtual'] = $jogadorAtual;
} else {
	$rodadaAtual = $_SESSION['rodadaAtual'];
	$jogadorAtual = $_SESSION['jogadorAtual'];
	$totalPontosJogador = $_SESSION['totalPontosJogador'];
	$ultimoJogador = $_SESSION['ultimoJogador'];
}

if (!isset($totalPontosJogador[$jogadorAtual]) && $jogadorAtual == 1) {
	for ($jogadorAtual; $jogadorAtual <= $qtdJogadores; $jogadorAtual++) {
		$totalPontosJogador[$jogadorAtual] = 0;
	}
	$jogadorAtual = 1;
} else if (!isset($totalPontosJogador[$jogadorAtual])) {
	$totalPontosJogador[$jogadorAtual] = 0;
}

if ($jogo == 1) {
	$qtdPontosParaVencer = 248;
	$resultadoSomaDados = 0;

	if ($rodadaAtual == 0) {
		echo "Começo do jogo!";

		echo "<br>" . str_repeat("-", 60);

		foreach ($totalPontosJogador as $jogador => $pontos) {
			echo "<br>Pontos do jogador " . $jogador . " = <b>" . $pontos . "</b>";
		}

		echo "<br>" . str_repeat("-", 60);

		$_SESSION['rodadaAtual'] = $rodadaAtual + 1;
	} else {

		if ($jogadorAtual == 2 && $rodadaAtual != 0) {
			echo '<div class="borda">';
			echo "Nova rodada!";
			echo "<br>Rodada atual: " . $rodadaAtual;
			echo "</div>";
			echo '<br>';
		}

		for ($numeroDoDado = 1; $numeroDoDado <= $qtdDados; $numeroDoDado++) {
			if (!isset($dado[$numeroDoDado])) {
				$dado[$numeroDoDado] = 0;
			}

			sleep(rand(1, 10) / 10);

			$dado[$numeroDoDado] = rand(1, 6);

			$resultadoSomaDados += $dado[$numeroDoDado];

			if ($qtdDados == 1) {
				echo "O valor do dado do jogador " . $ultimoJogador . " foi: <b>" . $dado[$numeroDoDado] . "</b>";
			} else {
				echo "O valor do dado " . $numeroDoDado . " do jogador " . $ultimoJogador . " foi: <b>" . $dado[$numeroDoDado] . "</b>";
			}

			if ($numeroDoDado == 1 && $qtdDados > 1) {
				echo "<br>";
			}

			if ($numeroDoDado == $qtdDados) {
				echo "<br>" . str_repeat("-", 60);
			}
		}

		if ($resultadoSomaDados == 1) {
			echo "<br><h3>O jogador " . $ultimoJogador . " fez <b>" . $resultadoSomaDados . "</b> ponto!</h3>";
		} else {
			echo "<br><h3>O jogador " . $ultimoJogador . " fez <b>" . $resultadoSomaDados . "</b> pontos!</h3>";
		}

		echo str_repeat("-", 60);

		$totalPontosJogador[$ultimoJogador] += $resultadoSomaDados;

		arsort($totalPontosJogador);

		if ($jogadorAtual == 1 && $rodadaAtual != 1) {
			echo "<br>Estatísticas do jogo após a rodada " . ($rodadaAtual - 1) . ":";
			foreach ($totalPontosJogador as $jogador => $pontos) {
				echo "<br>O jogador " . $jogador . " possui <b>" . $pontos . "</b> pontos!";
			}
			echo "<br>" . str_repeat("-", 60);
		}
	}

	if ($qtdDados == 1) {
		echo "<br>O jogador " . $jogadorAtual . " deve jogar o dado!";
	} else {
		echo "<br>O jogador " . $jogadorAtual . " deve jogar os dados!";
	}

	echo '<br><br>';


	$_SESSION['ultimoJogador'] = $jogadorAtual;

	if ($jogadorAtual < $qtdJogadores) {
		$_SESSION['jogadorAtual'] = $jogadorAtual + 1;
	} else {
		$_SESSION['jogadorAtual'] = 1;
		$_SESSION['rodadaAtual'] = $rodadaAtual + 1;
	}

	$_SESSION['totalPontosJogador'] = $totalPontosJogador;

	echo '<div class="ajustarPosicionamentoBotoes">';
	echo '<form action="jogo.php" method="">';
	echo '<input class="button" type="submit" value="Jogar">';
	echo '</form>';

	if ($rodadaAtual !== 0 && $rodadaAtual != 1) {
		echo '<form action="telaFinal.php" method="">';
		echo '<input class="button" type="submit" value="Finalizar">';
		echo '</form>';
	}

	echo '</div>';
}
