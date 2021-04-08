# CRUD do banco de dados
import sqlite3

con = sqlite3.connect("puzzleDB.db")

cur = con.cursor()

class PuzzleDB:
    
    #Metodo construtor da classe
    def __init__(self):
        #Faz a conexão com o banco de dados
        self.con = sqlite3.connect('puzzleDB.db')
        
        #Cria uma especie de ponteiro para fazer o manipulamento dos dados
        self.cur = con.cursor()
        
    def criar_tabela(self):
        try:
            self.cur.execute('''
                CREATE TABLE IF NOT EXISTS Perguntas (
                    Enunciado TEXT
                )
            ''')
        
        except Exception as e:
            print(f'[x] Falha ao criar a tabela [x]: {e}')
        
        else:
            print(f'[!] Tabela criada com sucesso [!]')
    
    def inserir_pergunta(self, pergunta):
        try:
            self.cur.execute('''
                INSERT INTO Perguntas VALUES (?)
            ''', pergunta)
        
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def inserir_resposta(self, resposta):
        try:
            self.cur.execute('''
                INSERT INTO Respostas VALUES (?, ?, ?, ?)
            ''', resposta)
        
        except Exception as e:
            print('\n[x] Falha ao inserir registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        
        else:
            self.con.commit()
            print('\n[!] Registro inserido com sucesso [!]\n')

    def consultar_registro_pelo_id(self, rowid, pergunta):
        return self.cur.executemany('''
            SELECT * FROM Perguntas WHERE rowid=?
        ''', (rowid, ).fetchone())

    def consultar_registros_perguntas(self):
        for row in self.cur.execute('''SELECT * FROM Perguntas'''):
            print(row)

    def alterar_pergunta(self, id, pergunta):
        try:
            self.cur.execute('''
            UPDATE Perguntas SET Enunciado = ? WHERE id=?''', (pergunta, id))
        
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')
    
    def alterar_respostas(self, id, alternativa, descricao, respostaCerta):
        try:
            self.cur.execute('''
            UPDATE Respostas SET Alternativa = ? Descrição = ? RespostaCerta = ?''', (alternativa, descricao, respostaCerta))
        
        except Exception as e:
            print('\n[x] Falha na alteração do registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()
        
        else:
            self.con.commit()
            print('\n[!] Registro alterado com sucesso [!]\n')

    def remover_pergunta(self, id):
        try:
            self.cur.execute(f'''
            DELETE FROM Pergunta WHERE id = ?''', (id,))

        except Exception as e:
            print('\n[x] Falha ao remover registro [x]\n')
            print(f'[x] Revertendo operação (rollback) [x]: {e}\n')
            self.con.rollback()

        else:
            self.con.commit()
            print('\n[!] Registro removido com sucesso [!]\n')

db = PuzzleDB()
db.inserir_pergunta((['Qual a moeda do Brasil?']))
db.consultar_registros_perguntas()