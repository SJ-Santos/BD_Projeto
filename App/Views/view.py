def view_prod_mais_vendidos(cursor):
  cursor.execute("DROP VIEW IF EXISTS produtos_mais_vendidos")
  cursor.execute("""CREATE VIEW produtos_mais_vendidos AS
  SELECT 
      p.nome AS produto,
      COUNT(v.id) AS total_vendido
      FROM produto p
      JOIN venda v ON p.id = v.id_produto
      GROUP BY p.id, p.nome
      ORDER BY total_vendido DESC;
  """)

  cursor.execute("GRANT ALL PRIVILEGES ON empresa.* TO 'admin_user'@'localhost';")

def view_resumo_vendas(cursor):
  cursor.execute("DROP VIEW IF EXISTS resumo_vendas_funcionario")
  cursor.execute("""CREATE VIEW resumo_vendas_funcionario AS
  SELECT 
      f.nome AS funcionario,
      COUNT(v.id) AS quantidade_vendas,
      f.salario
      FROM funcionario f
      JOIN venda v ON f.id = v.id_vendedor
      GROUP BY f.id, f.nome, f.salario;            
  """)

def view_func_por_venda(cursor):
  cursor.execute("DROP VIEW IF EXISTS view_func_por_venda")
  cursor.execute("""CREATE VIEW view_func_por_venda AS
  SELECT 
      f.nome AS funcionario,
       c.nome AS cliente,
       v.data,
       v.valor
       FROM venda v
       JOIN funcionario f ON v.id_vendedor = f.id
       JOIN cliente c ON v.id_cliente = c.id
       ORDER BY v.data, v.valor DESC;
      
  """)




  cursor.execute("FLUSH PRIVILEGES;")
