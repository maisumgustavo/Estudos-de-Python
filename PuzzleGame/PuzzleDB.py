# CRUD do banco de dados
import sqlite3

con = sqlite3.connect("puzzleDB.db")

cur = con.cursor()

def criarTabela():
    cur.execute('''
        CREATE TABLE questoes(
            pergunta text,
            resposta text
        )
    ''')
    con.commit()

# C - Criação do dado
def salvar(perguntasEResposta):
    cur.executemany('''
        INSERT INTO questoes VALUES(?, ?)
    ''', perguntasEResposta)
    con.commit()

# R - Consulta dos dados
def listarBanco():
    for row in cur.execute('SELECT * FROM questoes'):
        print(row)

# U - Atualização dos dados
# def atualizar(perguntaEResposta):
#     cur.execute('''
#         UPDATE questoes
#         SET pergunta = ?
#         WHERE 
#     ''')

# D - Apagar os dados
def apagar(perguntaEResposta):
    pass


listarBanco()