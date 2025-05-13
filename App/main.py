import mysql.connector
from Users import create_user,create_database,inserts,users



connector = mysql.connector(
    host = "localhost",
    user = "root_projeto",
    password = "ThisIsPero123"
)

cursor = connector.cursor() #criando cursor 


create_database(cursor) # cria a database
inserts(cursor) #coloca os inserts

create_user(connector,users(0)) #cria usuarios
create_user(connector,users(1))
create_user(connector,users(2))

#criar views e atribuilas a users



connector.commit()
cursor.close()
connector.close()


