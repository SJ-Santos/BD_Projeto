import mysql.connector
from Users.user import create_user,create_database,inserts,drop_database,insert_produto,insert_cliente
from Views.view import view_prod_mais_vendidos,view_resumo_vendas,view_func_por_venda,grant_admin,grant_func,grant_gerente


connector = mysql.connector.connect(
    host = "localhost",
    user = "root_projeto",
    password = "ThisIsPero123"
)
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

cursor = connector.cursor() #criando cursor 
if connector.is_connected:
    print("yep")

create_database(cursor) #cria database
inserts(cursor)#cria inserts
view_func_por_venda(cursor)
view_prod_mais_vendidos(cursor)
view_resumo_vendas(cursor)

print("Digite seu usuario e senha ")
usuario = input("Usuario: ")
senha = input("Senha: ")

if (usuario == Administrador["username"] and senha == Administrador["password"] ): #user admin
    create_user(cursor,Administrador)#cria user adm
    print("Deseja criar ou destruir a database?")
    choose = int(input("1-Criar , 2- Destruir"))

    if(choose == 1):
        create_database(cursor)
    elif(choose == 2):
        drop_database(cursor)
     
    print("deseja inserir um produto?")
    choose_insert_prod = int(input("1-sim,2-não"))
    if(choose_insert_prod ==1):
        nome = input("nome do produto")
        qtd = int(input("quantidade em estoque"))
        descricao = input("descrição do produto")
        valor = float(input("valor do produto"))
        print(f"nome={nome}, quantidade={qtd}, descricao={descricao}, valor={valor}")

        try:
            insert_produto(cursor, nome, qtd, descricao, valor)
            connector.commit()
            print("Produto inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir produto: {e}")

    else:
        print("ok")

    print("deseja inserir um cliente novo?")
    choose_insert_cliente = int(input("1-sim,2-não"))
    if(choose_insert_cliente == 1):
         nome = input("nome do produto")
         sexo = input("sexo do cliente")
         idade = int(input("idade do cliente"))
         nascimento=input("data de nascimento do cliente")
         insert_cliente(cursor,nome,sexo,idade,nascimento)

elif (usuario== Gerente["username"] and senha == Gerente["password"] ):
    create_user(cursor,Gerente)#cria user gerente

    print("deseja inserir um produto?")
    choose_insert_prod = int(input("1-sim,2-não"))
    if(choose_insert_prod ==1):
        nome = input("nome do produto")
        qtd = int(input("quantidade em estoque"))
        descricao = input("descrição do produto")
        valor = float(input("valor do produto"))
        insert_produto(cursor,nome,qtd,descricao,valor)
        cursor.commit()

elif(usuario== Funcionario["username"] and senha == Funcionario["password"] ):
    create_user(cursor,Funcionario)#cria user funcionario
    print("deseja inserir um cliente novo?")
    choose_insert_cliente = int(input("1-sim,2-não"))
    if(choose_insert_cliente == 1):
         nome = input("nome do produto")
         sexo = input("sexo do cliente")
         idade = int(input("idade do cliente"))
         nascimento=input("data de nascimento do cliente")
         insert_cliente(cursor,nome,sexo,idade,nascimento)

else:
    print("deu errado patrão")

connector.commit()
cursor.close()
connector.close()


