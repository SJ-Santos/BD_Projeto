import mysql.connector
from Users import create_user

connector = mysql.connector(
    host = "localhost",
    user = "root_projeto",
    password = "ThisIsPero123"
)

cursor = connector.cursor()

Administrador = {
    "username":"Administrador",
    "host":"localhost",
    "password" : "Adm123"
}

Gerente = {
    "username" : "Gerente",
    "host":"localhost",
    "password":"Ger123"
}

Funcionario = {
    "username":"Funcionario",
    "host":"localhost",
    "password":"Fun123"
}

create_user(connector,Administrador)
create_user(connector,Gerente)
create_user(connector,Funcionario)

cursor.execute("""CREATE DATABASE empresa;
                  
                  CREATE TABLE """)

connector.commit()
cursor.close()
connector.close()


