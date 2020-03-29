# Teste Estágio - Controle de Clientes por Advogado e Crawler
Teste de estágio com o objetivo de criar um sistema de controle de clientes para advogados, junto de um crawler para preencher informações do clientes com infos do google.
<br><br>
O website é feito utilizando Django, evitando configuração front-end. O banco de dados utiliza postgress no Heroku.
O website feito com Django pode ser acessado em https://controleclientesadvogados.herokuapp.com.
<br><br>
O formulário adquire o cpf e nome do cliente e utiliza para pesquisar e salvas as informações no banco de dados.
Para permitir executar as tasks, vou utilizado um schedule free no Heroku que permite executar as tasks de 10 em 10 minutos.

