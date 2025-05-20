import pypyodbc
from datetime import datetime

def conectar():
    try:
        conn_str = (
            "Driver={PostgreSQL Unicode};"
            "Server=localhost;"
            "Port=5432;"
            "Database=atividade_db;"
            "Uid=admin;"
            "Pwd=admin123;"
        )
        conn = pypyodbc.connect(conn_str)
        return conn
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return None

def listar_projetos(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projeto ORDER BY codigo;")
    projetos = cursor.fetchall()
    print("\n-- Projetos --")
    for p in projetos:
        print(f"ID: {p[0]} | Nome: {p[1]} | Descrição: {p[2]} | Dept: {p[3]} | Responsável: {p[4]} | Início: {p[5]} | Fim: {p[6]}")
    cursor.close()

def listar_atividades(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM atividade ORDER BY codigo;")
    atividades = cursor.fetchall()
    print("\n-- Atividades --")
    for a in atividades:
        print(f"ID: {a[0]} | Descrição: {a[1]} | Projeto ID: {a[2]} | Início: {a[3]} | Fim: {a[4]}")
    cursor.close()

def inserir_projeto(conn):
    nome = input("Nome do projeto: ")
    descricao = input("Descrição: ")
    depto = int(input("ID do departamento: "))
    responsavel = int(input("ID do responsável: "))
    data_inicio = input("Data início (YYYY-MM-DD): ")
    data_fim = input("Data fim (YYYY-MM-DD): ")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO projeto (nome, descricao, depto, responsavel, data_inicio, data_fim)
            VALUES (?, ?, ?, ?, ?, ?)
        """, [nome, descricao, depto, responsavel, data_inicio, data_fim])
        conn.commit()
        print("Projeto inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir projeto: {e}")
        conn.rollback()
    finally:
        cursor.close()

def atualizar_lider_projeto(conn):
    projeto_id = int(input("ID do projeto a atualizar: "))
    novo_lider = int(input("ID do novo líder: "))
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE projeto SET responsavel = ? WHERE codigo = ?", [novo_lider, projeto_id])
        if cursor.rowcount == 0:
            print("Projeto não encontrado.")
        else:
            conn.commit()
            print("Líder do projeto atualizado com sucesso!")
    except Exception as e:
        print(f"Erro ao atualizar líder: {e}")
        conn.rollback()
    finally:
        cursor.close()

def inserir_atividade(conn):
    descricao = input("Descrição da atividade: ")
    projeto_id = int(input("ID do projeto: "))
    data_inicio = input("Data início (YYYY-MM-DD): ")
    data_fim = input("Data fim (YYYY-MM-DD): ")
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
            VALUES (?, ?, ?, ?)
        """, [descricao, projeto_id, data_inicio, data_fim])
        conn.commit()
        print("Atividade inserida com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir atividade: {e}")
        conn.rollback()
    finally:
        cursor.close()

def menu():
    conn = conectar()
    if not conn:
        return

    while True:
        print("\n--- MENU ---")
        print("1 - Listar Projetos")
        print("2 - Listar Atividades")
        print("3 - Inserir Projeto")
        print("4 - Atualizar Líder de Projeto")
        print("5 - Inserir Atividade")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_projetos(conn)
        elif opcao == '2':
            listar_atividades(conn)
        elif opcao == '3':
            inserir_projeto(conn)
        elif opcao == '4':
            atualizar_lider_projeto(conn)
        elif opcao == '5':
            inserir_atividade(conn)
        elif opcao == '0':
            print("Saindo...")
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
