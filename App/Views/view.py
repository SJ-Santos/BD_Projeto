def view_admin(cursor):
  cursor.execute("CREATE VIEW Administrador AS admin_view" \
  "SELECT ")

def view_gerente(cursor):
  cursor.execute("CREATE VIEW Gerente AS gerente_view")

def view_func(cursor):
  cursor.execute("CREATE VIEW Funcionario AS func_view" \
  "")