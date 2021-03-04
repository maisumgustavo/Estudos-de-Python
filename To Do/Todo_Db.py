import sqlite3

#conexão com o banco de dados
conn = sqlite3.connect('todo-app.db')

#Criação da tabela de dados
def criar_tabela_Tarefas():
    conn.execute("""
    create table if not exists tarefas (
        id_tarefa integer primary key autoincrement,
        tarefa text,
        concluido integer
    )
    """)
    print('Tabela criada com sucesso.')


def adicionar_tarefa(tarefa):
    """Adiciona uma nova tarefa"""
    conn.execute("insert into tarefas (tarefa, concluido) values (?, ?)", (tarefa, 0))
    conn.commit()


def trocar_tarefa(id_tarefa):
    """Modifica a propriedade de alguma tarefa"""
    conn.execute("update tarefas set tarefa = ? where id_tarefa = ?", (id_tarefa, ))
    conn.commit()


def remover_tarefa(id_tarefa):
    """Remove uma tarefa"""
    conn.execute("delete from tarefas where id_tarefa = ?", (id_tarefa, ))
    conn.commit()


def listar_tarefas():
    """Retorna uma lista das tarefas"""
    return conn.execute("select id_tarefa, tarefa, concluido from tarefas")

def concluir_tarefa(id_tarefa):
    """Retorna o valor 1 para a coluna concluido de alguma tarefa"""
    conn.execute("UPDATE tarefas SET concluido = 1 WHERE id_tarefa = ?", id_tarefa)
    conn.commit()