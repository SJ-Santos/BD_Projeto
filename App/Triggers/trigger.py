import pandas as pd
import numpy as np
from mysql import connector

def criar_triggers(cursor):

    cursor.execute("DROP TRIGGER IF EXISTS TG_FUNCI_ESPECIAL")

    cursor.execute("""
    CREATE TRIGGER TG_FUNCI_ESPECIAL
    BEFORE INSERT
    ON venda
    FOR EACH ROW
    BEGIN
                   
    IF NEW.venda > 1000 THEN
                   
    DECLARE f_nome VARCHAR(100);
    DECLARE f_idade INT;
    DECLARE f_sexo CHAR(1);
    DECLARE f_cargo VARCHAR(10);
    DECLARE f_salario DECIMAL(10,2);
    DECLARE f_nascimento DATE;
    
    SELECT nome, idade, sexo, cargo, salario, nascimento
    INTO f_nome, f_idade, f_sexo, f_cargo, f_salario, f_nascimento
    FROM funcionario
    WHERE id = NEW.id_vendedor;
                   
    f_salario = f_salario + ((NEW.venda/100) * 5);
                   
    INSERT INTO funcionarioespecial (nome, idade, sexo, cargo, salario, nascimento) VALUES
    (f_nome, f_idade, f_sexo, f_cargo, f_salario, f_nascimento)
                   
    SELECT CONCAT('O bonus total vai ser: R$', ((NEW.venda/100) * 5)) AS mensagem;
    
    END IF;
                   
    END;
     """, multi=True)
    
    cursor.execute("DROP TRIGGER IF EXISTS TG_CLIE_ESPECIAL")
    
    cursor.execute("""
    CREATE TRIGGER TG_CLIE_ESPECIAL
    BEFORE INSERT
    ON venda
    FOR EACH ROW
    BEGIN
    
    IF NEW.venda > 500 THEN
    DECLARE c_nome VARCHAR(100);
    DECLARE c_sexo CHAR(1);
    DECLARE c_idade INT;
    DECLARE c_cashback DECIMAL(10,2);
    c_cashback = 0;
                   
    SELECT nome, sexo, idade
    INTO c_nome, c_sexo, c_idade
    FROM cliente
    WHERE id = NEW.id_cliente;
                   
    c_cashback = c_cashback + ((NEW.venda/100) * 2);
                   
    INSERT INTO clienteespecial (nome, sexo, idade, id_cliente, cashback) VALUES
    (c_nome, c_sexo, c_idade, NEW.id_cliente, c_cashback)
                   
    SELECT CONCAT('O cashback adicionado vai ser: R$', ((NEW.venda/100) * 2)) AS mensagem;
    
    END IF;
    
    END;
     """,multi=True)
    
    cursor.execute("DROP TRIGGER IF EXISTS TG_CLIE_NAO_ESPECIAL")

    cursor.execute("""
    CREATE TRIGGER TG_CLIE_NAO_ESPECIAL
    AFTER UPDATE
    ON clienteespecial
    FOR EACH ROW
    BEGIN
                   
    IF NEW.cashback <= 0 THEN
    DELETE FROM clienteespecial
    WHERE id_cliente = NEW.id_cliente;
                   
    END IF;
                   
    END;
     """,multi=True)