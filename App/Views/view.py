def view_admin(cursor):
  cursor.execute("DROP VIEW IF EXISTS admin_view")
  cursor.execute("""CREATE VIEW admin_view" AS
  SELECT 
      v.id AS id_venda,     
      f.nome AS nome_funcionario,
      p.nome AS produto,
      p.valor,
      v.data
      FROM venda v
      JOIN funcionario f ON v.id_vendedor = f.id
      JOIN cliente c ON v.id_cliente = c.id
      JOIN produto p ON v.id = p.id

  """)
  cursor.execute("GRANT ALL PRIVILEGES ON empresa.* TO 'admin_user'@'localhost';")

def view_gerente(cursor):
  cursor.execute("DROP VIEW IF EXISTS gerente_view")
  cursor.execute("""CREATE VIEW gerente_view AS
  SELECT 
      f.nome AS funcionario,
      f.cargo,
      COUNT(v.id) AS total_vendas,
      SUM(p.valor) AS total_valor_vendido
      FROM venda v
      JOIN funcionario f ON v.id_vendedor = f.id
      JOIN produto p ON v.id = p.id
      GROUP BY f.nome, f.cargo

                 
                 
  """)

def view_func(cursor):
  cursor.execute("DROP VIEW IF EXISTS func_view")
  cursor.execute("""CREATE VIEW func_view AS
  SELECT 
      v.id AS id_venda,
      v.id_cliente,
      v.id_vendedor,
      v.data
      FROM venda v         
  """)




  cursor.execute("FLUSH PRIVILEGES;")
