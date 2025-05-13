def users(i):
    if i == 0:
     user =  Administrador = {
        "username":"Administrador",
        "host":"localhost",
        "password" : "Adm123"
      }
    elif i ==1:
     user =  Gerente = {
        "username" : "Gerente",
        "host":"localhost",
        "password":"Ger123"
       }
    elif i==2:
      user =  Funcionario = {
        "username":"Funcionario",
        "host":"localhost",
        "password":"Fun123"
        }
    return user


def create_user(cursor,user):
    cursor.execute(f"CREATE USER '{user['username']}'@'{user['host']}' IDENTIFIED BY '{user['password']}' ;")

def inserts(cursor):
    cursor.execute("""
INSERT INTO cliente (nome, sexo, idade, nascimento) VALUES
('Eva Neves', 'F', 33, '1991-08-08'),
('Felipe Rocha', 'M', 26, '1998-09-09'),
('Grazi Mendes', 'F', 50, '1974-03-03'),
('Hugo Andrade', 'M', 47, '1977-05-05'),
('Íris Carvalho', 'F', 31, '1993-06-06'),
('Jackson Antunes', 'M', 29, '1995-11-11'),
('Kelly Moura', 'F', 30, '1994-10-10'),
('Leandro Queiroz', 'M', 42, '1982-12-12'),
('Manuela Dias', 'F', 27, '1997-09-09'),
('Nathan Santos', 'M', 28, '1996-04-04'),
('Odete Brito', 'F', 36, '1988-02-02'),
('Patrick Linhares', 'M', 39, '1985-01-01'),
('Queila Souza', 'F', 43, '1981-07-07'),
('Renan Guedes', 'M', 45, '1979-06-06'),
('Sara Diniz', 'F', 24, '2000-03-03'),
('Tales Rezende', 'M', 33, '1991-02-02'),
('Ulla Barreto', 'F', 35, '1989-12-12'),
('Vitor Lacerda', 'M', 31, '1993-11-11'),
('Waleska Vieira', 'F', 37, '1987-10-10'),
('Xavier Martins', 'M', 40, '1984-09-09'),
('Yara Figueiredo', 'F', 26, '1998-08-08'),
('Zilda Leal', 'F', 34, '1990-07-07'),
('Alan Ribeiro', 'M', 43, '1981-06-06'),
('Bárbara Cunha', 'F', 29, '1995-05-05'),
('Caio Monteiro', 'M', 48, '1976-04-04'),
('Débora Braga', 'F', 38, '1986-03-03'),
('Elias Morais', 'M', 36, '1988-02-02'),
('Fátima Meireles', 'F', 39, '1985-01-01'),
('Gabriel Matos', 'M', 23, '2001-12-12'),
('Helena Campos', 'F', 27, '1997-11-11'),
('Ítalo Azevedo', 'M', 32, '1992-10-10'),
('Jacqueline Barros', 'F', 45, '1979-09-09'),
('Kevin Santana', 'M', 44, '1980-08-08'),
('Larissa Peixoto', 'F', 31, '1993-07-07'),
('Maurício Castro', 'M', 37, '1987-06-06'),
('Natália Costa', 'F', 30, '1994-05-05'),
('Otávio Rocha', 'M', 34, '1990-04-04'),
('Priscila Fernandes', 'F', 28, '1996-03-03'),
('Quirino Ribeiro', 'M', 49, '1975-02-02'),
('Rita Amaral', 'F', 33, '1991-01-01'),
('Samuel Rocha', 'M', 26, '1998-12-12'),
('Talita Duarte', 'F', 35, '1989-11-11'),
('Ubirajara Lopes', 'M', 40, '1984-10-10'),
('Verônica Martins', 'F', 41, '1983-09-09'),
('Wesley Prado', 'M', 38, '1986-08-08'),
('Ximena Almeida', 'F', 30, '1994-07-07'),
('Ygor Cardoso', 'M', 27, '1997-06-06'),
('Zuleica Oliveira', 'F', 36, '1988-05-05'),
('Adriana Silva', 'F', 25, '1999-01-15'),
('Bruno Costa', 'M', 30, '1994-02-20'),
('Camila Pereira', 'F', 28, '1996-03-25'),
('Daniel Souza', 'M', 31, '1993-04-30'),
('Eduarda Gomes', 'F', 35, '1989-05-10'),
('Fernando Oliveira', 'M', 27, '1997-06-18'),
('Gisele Mendes', 'F', 42, '1982-07-05'),
('Henrique Lima', 'M', 29, '1995-08-23'),
('Isabela Farias', 'F', 33, '1991-09-12'),
('João Batista', 'M', 50, '1974-10-07'),
('Karina Duarte', 'F', 24, '2000-11-29'),
('Luciano Matos', 'M', 39, '1985-12-17'),
('Mariana Ribeiro', 'F', 45, '1979-01-03'),
('Nelson Cardoso', 'M', 37, '1987-02-14'),
('Olga Moreira', 'F', 34, '1990-03-09'),
('Paulo Henrique', 'M', 48, '1976-04-01'),
('Roberta Fernandes', 'F', 41, '1983-05-21'),
('Sandro Rocha', 'M', 32, '1992-06-06'),
('Tânia Alves', 'F', 38, '1986-07-30'),
('Ulisses Castro', 'M', 26, '1998-08-15'),
('Vanessa Freitas', 'F', 43, '1981-09-19'),
('Walter Nogueira', 'M', 36, '1988-10-04'),
('Xênia Oliveira', 'F', 29, '1995-11-27'),
('Yuri Martins', 'M', 47, '1977-12-13'),
('Zara Meireles', 'F', 40, '1984-01-09'),
('Abel Freitas', 'M', 31, '1993-03-15'),
('Bruna Castro', 'F', 29, '1995-04-25'),
('César Lima', 'M', 42, '1982-05-30'),
('Daniela Peixoto', 'F', 33, '1991-06-20'),
('Edson Vieira', 'M', 36, '1988-07-10'),
('Flávia Martins', 'F', 27, '1997-08-18'),
('Gustavo Nogueira', 'M', 39, '1985-09-05'),
('Helena Amaral', 'F', 40, '1984-10-12'),
('Igor Prado', 'M', 28, '1996-11-23'),
('Jéssica Andrade', 'F', 45, '1979-12-03'),
('Kaique Almeida', 'M', 50, '1974-01-29'),
('Letícia Cardoso', 'F', 24, '2000-02-11'),
('Matheus Rocha', 'M', 31, '1993-03-07'),
('Natasha Meireles', 'F', 38, '1986-04-14'),
('Otávio Mendes', 'M', 26, '1998-05-19'),
('Patrícia Fernandes', 'F', 41, '1983-06-09'),
('Rogério Costa', 'M', 32, '1992-07-22'),
('Sabrina Azevedo', 'F', 35, '1989-08-04'),
('Thiago Ribeiro', 'M', 29, '1995-09-21'),
('Úrsula Braga', 'F', 43, '1981-10-15'),
('Vicente Matos', 'M', 37, '1987-11-27'),
('Wanessa Barros', 'F', 34, '1990-12-08'),
('Xander Rezende', 'M', 48, '1976-01-05'),
('Yasmin Santana', 'F', 30, '1994-02-16'),
('Zacarias Morais', 'M', 44, '1980-03-12'),
('Alana Souza', 'F', 28, '1996-04-26'),
('Brendon Antunes', 'M', 36, '1988-05-31');
                   
INSERT INTO funcionario (nome, idade, sexo, cargo, salario, nascimento) VALUES
('João Silva', 35, 'M', 'vendedor', 2500.00, '1989-03-15'),
('Maria Oliveira', 42, 'F', 'gerente', 4500.00, '1982-07-22'),
('Carlos Lima', 29, 'M', 'vendedor', 2300.00, '1995-01-09'),
('Ana Souza', 38, 'F', 'vendedor', 2600.00, '1986-12-03'),
('Roberto Costa', 50, 'M', 'CEO', 9000.00, '1974-06-30');

INSERT INTO produto (nome, quantidade, descricao, valor) VALUES
('Produto A', 100, 'Descrição do produto A', 10.99),
('Produto B', 150, 'Descrição do produto B', 12.50),
('Produto C', 200, 'Descrição do produto C', 8.75),
('Produto D', 50, 'Descrição do produto D', 15.00),
('Produto E', 80, 'Descrição do produto E', 9.99),
('Produto F', 120, 'Descrição do produto F', 13.30),
('Produto G', 90, 'Descrição do produto G', 7.49),
('Produto H', 60, 'Descrição do produto H', 19.99),
('Produto I', 300, 'Descrição do produto I', 5.99),
('Produto J', 110, 'Descrição do produto J', 11.40),
('Produto K', 75, 'Descrição do produto K', 14.20),
('Produto L', 130, 'Descrição do produto L', 6.60),
('Produto M', 95, 'Descrição do produto M', 16.80),
('Produto N', 170, 'Descrição do produto N', 17.50),
('Produto O', 65, 'Descrição do produto O', 10.10),
('Produto P', 85, 'Descrição do produto P', 12.20),
('Produto Q', 140, 'Descrição do produto Q', 9.80),
('Produto R', 180, 'Descrição do produto R', 8.40),
('Produto S', 210, 'Descrição do produto S', 13.75),
('Produto T', 250, 'Descrição do produto T', 14.60);


    """) 

def drop_database(cursor):
    cursor.execute("""
    DROP DATABASE empresa;

    """)

def create_database(cursor):
    cursor.execute("""
CREATE DATABASE empresa;

CREATE TABLE cliente(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
sexo CHAR(1) CHECK (sexo IN ('M', 'F', 'O')),
idade INT,
nascimento DATE
);

CREATE TABLE clienteespecial (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
sexo CHAR(1) CHECK (sexo IN ('M', 'F', 'O')),
idade INT,
id_cliente INT,
cashback INT,
FOREIGN KEY (id_cliente) REFERENCES cliente(id)
);

CREATE TABLE  funcionario(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
idade INT,
sexo CHAR(1) CHECK (sexo IN ('M', 'F', 'O')),
cargo VARCHAR(10) CHECK (cargo IN ('vendedor','gerente','CEO')),
salario DECIMAL(10,2),
nascimento DATE
);

CREATE TABLE produto(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(100),
quantidade INT,
descricao VARCHAR(),
valor DECIMAL(10,2)
);

CREATE TABLE venda(
id INT AUTO_INCREMENT PRIMARY KEY,
id_vendedor INT,
id_cliente INT,
data DATE,
FOREIGN KEY(id_vendedor) REFERENCES funcionario(id),
FOREIGN KEY(id_cliente) REFERENCES cliente(id)
);
        """)

