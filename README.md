# Gerenciando banco de dados com Python, SQLite e DBeaver

Este repositório se refere ao desafio individual do curso Data Analytics da WoMakers Code, módulo de Banco de Dados e SQL.

O script em python é capaz de automatizar tarefas de criar tabelas, inserir, atualizar e remover registros, além de realizar consultas básicas ao banco de dados utilizando funções condicionais como WHERE, ORDER BY, agregações como COUNT, AVG, MAX, sub-consultas e união de tabelas por meio de JOIN.

## Como criar o banco de dados

Para rodar o projeto, é necessário ter instalados um editor de texto e um gerenciador de banco de dados. Utilizamos o VS Code e o DBeaver e sugerimos que você também o faça, para que possa acompanhar o passo a passo com maior aproveitamento.

Com o DBeaver aberto, vamos criar uma conexão com o banco de dados. Para isso, clique no menu `File` e em seguida, em `New`.

O programa vai abrir uma janela e você deverá selecionar a opção `Database Connection` e clicar em `Next`:

![](/imagens/imagem1.jpg)
 
Em seguida, selecione o SQLite como driver e clique em `Next`:

![](/imagens/imagem2.jpg)

Por último, você deve clicar no botão de `Create` e selecionar a pasta onde será salvo seu banco. Essa pasta deve ser a mesma que receberá o script do Python:

![](/imagens/imagem3.jpg)

## Como acessar o script

Na mesma pasta em que você salvou o banco de dados, abra seu terminal e execute o comando:

```
git clone https://github.com/cintiadantas20/RepoWMC_bco_dados.git
```

Porém, como o arquivo do banco de dados estará na pasta raiz, é necessário movê-lo para dentro da pasta criada pelo comando.

O próximo passo é rodar o código .py e acompanhar as modificações no DBeaver. Você pode ir comentando os códigos e rodando de um por um, para verificar os comandos sendo executados um por vez e aproveitar a mágica em sua plenitude.

Espero que você aproveite o conteúdo e sinta-se à vontade para me adicionar.

## Autora

- [@cintiadantas20](https://github.com/cintiadantas20)
- [@Cíntia Dantas](https://www.linkedin.com/in/cintia-dantas/)