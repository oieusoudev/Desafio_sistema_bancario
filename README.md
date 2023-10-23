# Desafio_sistema_bancario
Desafio do curso de Python Developer na DIO.
<br>
Nos foi pedido para criar um sistema bancário simples com as opções  Depositar, Sacar, consultar Extrato e Sair.

Foram declaradas as variáveis saldo, limite, extrato, numero_saques e LIMITE_SAQUES.

No Código foi utilizado While para repetição.
</br>

Para a opção de depósito foi criada uma condição if/ else para verificar se o valor de deposito é maior que 0, adicionar o saldo, adicionar essa informação ao extrato e um else para caso nada disso aconteça.

<br>
Um ELIF para a opção de Saque para verificarmos se o valor a ser sacado é menor que o saldo caso seja ele apresenta uma mensagem de saldo insuficiente ;
Verificar se o valor está de acordo com o limite diário ;
Verificar se o usuário excedeu o limite de saques diário.
</br>
<br>
UM ELIF para caso o valor seja maior que 0 ele subtrai o valor do saldo, grava no extrato e contabiliza 1 de 3 saques diários.

Para o Extrato temos um IF TERNÁRIO para verificar se o extrato está vazio ou não.

Para sair da foi utilizado o BREAK

ELSE para qualquer número, letra ou caráctere que nao tenha sido definido como opção.
</br>

