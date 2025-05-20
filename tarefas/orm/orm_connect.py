from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

# === CONFIGURAÇÃO DO BANCO ===
engine = create_engine('postgresql+psycopg2://admin:admin123@localhost:5432/atividade_db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# === MODELOS ORM ===

class Projeto(Base):
    __tablename__ = 'projeto'

    codigo = Column(Integer, primary_key=True)
    nome = Column(String)
    descricao = Column(String)
    depto = Column(Integer)
    responsavel = Column(Integer)
    data_inicio = Column(Date)
    data_fim = Column(Date)

    atividades = relationship("Atividade", back_populates="projeto")

class Atividade(Base):
    __tablename__ = 'atividade'

    codigo = Column(Integer, primary_key=True)
    descricao = Column(String)
    projeto_id = Column(Integer, ForeignKey('projeto.codigo'))
    data_inicio = Column(Date)
    data_fim = Column(Date)

    projeto = relationship("Projeto", back_populates="atividades")

# Cria as tabelas no banco (caso não existam)
Base.metadata.create_all(engine)

# === FUNÇÕES DE MENU ===

def listar_projetos():
    print("\n-- Projetos --")
    projetos = session.query(Projeto).order_by(Projeto.codigo).all()
    for p in projetos:
        print(f"[{p.codigo}] {p.nome} - {p.descricao} (Resp: {p.responsavel})")

def listar_atividades():
    print("\n-- Atividades --")
    atividades = session.query(Atividade).order_by(Atividade.codigo).all()
    for a in atividades:
        print(f"[{a.codigo}] {a.descricao} - Projeto: {a.projeto_id}")

def inserir_projeto():
    try:
        nome = input("Nome: ")
        desc = input("Descrição: ")
        depto = int(input("ID do Departamento: "))
        resp = int(input("ID do Responsável: "))
        inicio = datetime.strptime(input("Data início (YYYY-MM-DD): "), "%Y-%m-%d")
        fim = datetime.strptime(input("Data fim (YYYY-MM-DD): "), "%Y-%m-%d")

        projeto = Projeto(nome=nome, descricao=desc, depto=depto, responsavel=resp,
                          data_inicio=inicio, data_fim=fim)
        session.add(projeto)
        session.commit()
        print("✅ Projeto adicionado com sucesso!")
    except Exception as e:
        print("Erro ao inserir projeto:", e)

def inserir_atividade():
    try:
        desc = input("Descrição da Atividade: ")
        projeto_id = int(input("ID do Projeto: "))
        inicio = datetime.strptime(input("Data início (YYYY-MM-DD): "), "%Y-%m-%d")
        fim = datetime.strptime(input("Data fim (YYYY-MM-DD): "), "%Y-%m-%d")

        atividade = Atividade(descricao=desc, projeto_id=projeto_id,
                              data_inicio=inicio, data_fim=fim)
        session.add(atividade)
        session.commit()
        print("✅ Atividade adicionada com sucesso!")
    except Exception as e:
        print("Erro ao inserir atividade:", e)

# === MENU PRINCIPAL ===

def menu():
    while True:
        print("\n--- MENU ORM ---")
        print("1 - Listar Projetos")
        print("2 - Listar Atividades")
        print("3 - Inserir Projeto")
        print("4 - Inserir Atividade")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            listar_projetos()
        elif opcao == '2':
            listar_atividades()
        elif opcao == '3':
            inserir_projeto()
        elif opcao == '4':
            inserir_atividade()
        elif opcao == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

# === EXECUÇÃO ===

if __name__ == "__main__":
    menu()
