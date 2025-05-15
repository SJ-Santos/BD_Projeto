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
    CREATE PROCEDURE estatistica()
BEGIN
    DECLARE produto_mais_vendido_id INT;
    DECLARE nome_produto_mais_vendido VARCHAR(100);
    DECLARE nome_vendedor_associado VARCHAR(100);
    DECLARE nome_produto_menos_vendido VARCHAR(100);
    DECLARE valor_total FLOAT;
    DECLARE mes_maior_venda VARCHAR(7);
    DECLARE mes_menor_venda VARCHAR(7);

    SELECT v.id_produto, p.nome
    INTO produto_mais_vendido_id, nome_produto_mais_vendido
    FROM venda v
    JOIN produto p ON v.id_produto = p.id
    GROUP BY v.id_produto, p.nome
    ORDER BY COUNT(*) DESC
    LIMIT 1;

    SELECT f.nome
    INTO nome_vendedor_associado
    FROM venda v
    JOIN funcionario f ON v.id_vendedor = f.id
    WHERE v.id_produto = produto_mais_vendido_id
    GROUP BY f.id, f.nome
    ORDER BY COUNT(*) DESC
    LIMIT 1;

    SELECT p.nome
    INTO nome_produto_menos_vendido
    FROM venda v
    JOIN produto p ON v.id_produto = p.id
    GROUP BY p.id, p.nome
    ORDER BY COUNT(*) ASC
    LIMIT 1;

    SELECT SUM(venda)
    INTO valor_total
    FROM venda
    WHERE id_produto = produto_mais_vendido_id;

    SELECT DATE_FORMAT(data, '%Y-%m')
    INTO mes_maior_venda
    FROM venda
    WHERE id_produto = produto_mais_vendido_id
    GROUP BY DATE_FORMAT(data, '%Y-%m')
    ORDER BY COUNT(*) DESC
    LIMIT 1;

    SELECT DATE_FORMAT(data, '%Y-%m')
    INTO mes_menor_venda
    FROM venda
    WHERE id_produto = produto_mais_vendido_id
    GROUP BY DATE_FORMAT(data, '%Y-%m')
    ORDER BY COUNT(*) ASC
    LIMIT 1;

    SELECT 
        nome_produto_mais_vendido AS 'Produto Mais Vendido',
        nome_vendedor_associado AS 'Vendedor Associado',
        nome_produto_menos_vendido AS 'Produto Menos Vendido',
        valor_total AS 'Valor Total com Produto Mais Vendido',
        mes_maior_venda AS 'Mês de Maior Venda',
        mes_menor_venda AS 'Mês de Menor Venda';
END //
                       """)
