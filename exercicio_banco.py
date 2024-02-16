import sqlite3

conexao = sqlite3.connect('exercicios_banco')
cursor = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(50))')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
reg_alunos = [(1, 'João', 20, 'Engenharia'),
              (2, 'Maria', 22, 'Medicina'),
              (3, 'Pedro', 21, 'Direito'),
              (4, 'Ana', 19, 'Administração'),
              (5, 'Carlos', 23, 'Economia'),
              (6, 'Juliana', 20, 'Psicologia'),
              (7, 'Lucas', 21, 'Engenharia'),
              (8, 'Mariana', 22, 'Arquitetura'),
              (9, 'Felipe', 20, 'Ciência da Computação'),
              (10, 'Amanda', 21, 'Marketing')]
for registro in reg_alunos:
    cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (?,?,?,?)', registro)

# 3. Consultas Básicas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)
# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT nome, idade FROM alunos WHERE idade>20')
for aluno in dados:
    print(aluno)
# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso="Engenharia" ORDER BY nome')
for aluno in dados:
    print(aluno)
# d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT COUNT (nome) FROM alunos')
for aluno in dados:
    print(aluno)

# 4. Atualização e Remoção
# a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade=22 WHERE nome="Ana"')
# b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id=10')
dados = cursor.execute('SELECT * FROM alunos')
for aluno in dados:
    print(aluno)

# 5. Criar uma Tabela e Inserir Dados
# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes(id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')
reg_clientes = [(1, 'Sofia', 25, 500.50),
                (2, 'Enzo', 30, 2000.75),
                (3, 'Valentina', 35, 1800.00),
                (4, 'Miguel', 28, 2200.25),
                (5, 'Laura', 32, 900.00),
                (6, 'Davi', 29, 2050.50),
                (7, 'Manuela', 47, 1750.75),
                (8, 'Arthur', 31, 300.00),
                (9, 'Helena', 36, 1950.25),
                (10, 'Bernardo', 33, 100.00)]
for registro in reg_clientes:
    cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (?,?,?,?)', registro)

# 6. Consultas e Funções Agregadas
# Escreva consultas SQL para realizar as seguintes tarefas:
# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade>30')
for cliente in dados:
    print(cliente)
# b) Calcule o saldo médio dos clientes.
dados = cursor.execute('SELECT AVG(saldo) FROM clientes')
for cliente in dados:
    print(cliente)
# c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('SELECT * FROM clientes WHERE saldo=(SELECT MAX(saldo) FROM clientes)')
for cliente in dados:
    print(cliente)
# d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT COUNT(nome) FROM clientes WHERE saldo>1000')
for cliente in dados:
    print(cliente)

# 7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo=1900 WHERE nome="Laura"')
# b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE id=8')
dados = cursor.execute('SELECT * FROM clientes')
for cliente in dados:
    print(cliente)

# 8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes". Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
cursor.execute('CREATE TABLE compras(id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(50), valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

reg_compras = [(1, 1, 'Livro', 30.00),
               (2, 3, 'Roupa', 50.00),
               (3, 5, 'Eletrônico', 200.00),
               (4, 7, 'Acessório', 15.00),
               (5, 9, 'Cosmético', 40.00),
               (6, 2, 'Alimento', 20.00),
               (7, 4, 'Eletrônico', 300.00),
               (8, 6, 'Livro', 25.00),
               (9, 8, 'Roupa', 70.00),
               (10, 10, 'Acessório', 10.00)]
for registro in reg_compras:
    cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (?,?,?,?)', registro)

dados = cursor.execute('SELECT nome, produto, valor FROM clientes LEFT JOIN compras ON clientes.id=compras.cliente_id')
for compra in dados:
    print(compra)

conexao.commit()
conexao.close 