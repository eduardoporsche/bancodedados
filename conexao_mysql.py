import mysql.connector
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prova_2",
)

cursor = conexao.cursor()

opcao = int(input("Digite a opção que deseja: \n 1-Cadastrar \n 2-Exibir \n 3-Selecionar nome \n 4-Selecionar \n 5-Selecionar Categoria \n 6-Porcentegaem \n 7-Deletar:\n "))

print("você selecionou a opção 01: ", opcao ,"\n ")


match opcao:
    case 1:
        descrição= input("Digite a descrição do veiculo: ")
        marca= input("Digite a marca do veiculo: ")
        tipo_combustivo= input("Digite o tipo de combustivo: ")
        ano_fabricação= input("Digite o ano de fabricação: ")
        categoria= input("Digite a categoria do carro: ")
        qtd_passageiro= input("Digite a quantidade de passageiros: ")
        valor= input("Digte o valor do veiculo: ")

        sql= f'INSERT INTO veiculos VALUES(0,"{descrição}","{marca}","{tipo_combustivo}","{ano_fabricação}","{categoria}","{qtd_passageiro}","{valor}")'
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        conexao.close()
    case 2:
        comando= f'SELECT * FROM veiculos'
        cursor.execute(comando)
        resultado= cursor.fetchall()
        print(resultado)

        cursor.close()
        conexao.close()
    case 3:
        nome= input("Digite o nome do veiculo: ")
        marca= input("Digite a marca do veiculo: ")

        sql= f'SELECT * FROM veiculos WHERE descricao="{nome}" AND marca="{marca}"'
        cursor.execute(sql)
        resultado= cursor.fetchall()
        print(resultado)

        cursor.close()
        conexao.close()
    case 4:
        valor= input("Digite o valor do veiculo: ")
        comnustivo= input("Digite o tipo do combustiv0: ")

        sql = f'SELECT * FROM veiculos WHERE tipo_combustivo="{comnustivo}" AND valor>="{valor}"'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
    case 5:
        categoria= input("Digite a categoria do carro: ")
        valor = input("Digite o valor do veiculo: ")

        sql = f'SELECT * FROM veiculos WHERE categoria="{categoria}" AND valor="{valor}"'
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)

        cursor.close()
        conexao.close()
    case 6:
        combustivo= input("Digite o combustivel do carro: ")
        sql= f'UPDATE veiculos SET valor= valor*1.10'
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        conexao.close()
    case 7:
        nome= input("Digite o nome do veiculo que voçe deseja deletar: ")
        sql= f'DELETE FROM veiculos WHERE descricao="{nome}"'
        cursor.execute(sql)
        conexao.commit()

        cursor.close()
        conexao.close()