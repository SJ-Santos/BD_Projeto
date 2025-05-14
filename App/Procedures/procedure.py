def Reajuste (cursor):
    cursor.execute("DROP PROCEDURE IF EXISTS Reajuste ")
    cursor.execute("""
    CREATE PROCEDURE Reajuste (IN cargo varchar, IN porcento DECIMAL(10, 2))
    BEGIN
        UPDATE funcionario
        SET salario = salario + aumento_valor*salario
        WHERE cargo = cargo_funcionario;

    END
    """)
def Sorteio(cursor):
    cursor.execute("DROP PROCEDURE IF EXISTS Sorteio ")
    cursor.execute("""
    CREATE PROCEDURE Sorteio (OUT premio INT, OUT id_cliente INT)
    BEGIN
    SELECT id_cliente INTO id_cliente
    FROM cliente
    ORDER BY RAND()
    LIMIT 1;               

    IF EXISTS (
        SELECT 1 FROM clientes_especial WHERE id_cliente = id_cliente
    ) THEN
        SET premio = 200;
    ELSE
        SET premio = 100;
    END IF;
    END
    """)

def Venda(cursor):
    cursor.execute("DROP PROCEDURE IF EXISTS Venda ")
    cursor.execute("""
    CREATE PROCEDURE Venda (IN id INT)
    BEGIN
    IF quantidade !=0 where id = id_produto THEN
        UPDATE produto
        SET quantidade = quantidade - 1
        WHERE id = id_produto;
    
    END IF
    """)
def Estatísticas (cursor):
    cursor.execute("DROP PROCEDURE IF EXISTS Estatísticas ")
    cursor.execute("""
    CREATE PROCEDURE Estatísticas (IN id INT)
    BEGIN
    SELECT MAX()
                   
    END
    """)
