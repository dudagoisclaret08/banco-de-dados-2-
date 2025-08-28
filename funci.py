##atvdd1 
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()

cursor.execute("UPDATE funcionarios SET salario = salario * 1.10 WHERE departamento = 'TI'")
banco.commit()  
  
cursor.execute("SELECT nome, departamento, salario FROM funcionarios")
funcionarios = cursor.fetchall()

banco.close()



#atvdd2 
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()

cursor.execute("UPDATE funcionarios SET telefone = '(11) 98888-7777' WHERE cpf = '15967994960'")

banco.commit()
print("Telefone atualizado com sucesso!")

banco.close()



###atvdd3
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()

cursor.execute("UPDATE funcionarios SET departamento = 'RH' WHERE pnome = 'Ana'")

banco.commit()
print("Departamento atualizado com sucesso!")

banco.close()


#atvdd4
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()

cursor.execute("UPDATE funcionarios SET cargo = 'Analista' WHERE cargo = 'Estagiário' ")

banco.commit()

print("Cargo atualizado de Estagiário para Analista com sucesso!")

banco.close()


# ##atvdd5
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()

cursor.execute("DELETE FROM funcionarios WHERE idade < 20")

banco.commit()

print("Registros de funcionários com idade menor que 20 foram removidos com sucesso!")

banco.close()

##atvdd6
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()

cursor.execute("DELETE FROM funcionarios WHERE pnome = 'Victor'")

banco.commit()

print("Funcionário Victor removido com sucesso!")

banco.close()



##atvdd7
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()


cursor.execute("DELETE FROM funcionarios WHERE departamento = 'Marketing'")

banco.commit()

print("Funcionários do departamento Marketing removidos com sucesso!")

banco.close()


##atvdd8
import sqlite3 as funcionarios

banco = funcionarios.connect('ricardaofather.db')
cursor = banco.cursor()

cursor.execute("SELECT cpf FROM funcionarios GROUP BY cpf HAVING COUNT(*) > 1 LIMIT 1") 
#HAVING COUNT(*) > 1 filtra para CPFs que aparecem mais de uma vez (duplicados). # LIMIT 1 pega só um desses CPFs duplicados.
cpf_duplicado = cursor.fetchone()

if cpf_duplicado:
    cpf = cpf_duplicado[0]
    cursor.execute("SELECT id FROM funcionarios WHERE cpf = ? LIMIT 1", (cpf,))
    registro_para_deletar = cursor.fetchone() # apaga os resgistros 
    
    if registro_para_deletar:
        id_para_deletar = registro_para_deletar[0]
        cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_para_deletar,))
        banco.commit()
        print(f"Um registro duplicado com CPF {cpf} foi removido com sucesso!")
    else:
        print("Nenhum registro encontrado para deletar.")
else:
    print("Nenhum CPF duplicado encontrado.")


banco.close()
