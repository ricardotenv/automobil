from automobil.database.models import create_db_and_tables, engine
from automobil.database.types import AutomobileSchema
from automobil.database.models import Automobile
from sqlalchemy.orm import sessionmaker # type: ignore
from automobil.mcp.server.tools import mcp
from typing import List
import math

from pydantic_ai import Agent # type: ignore

def populate() -> None:
    try:
        print("Verificando e assegurando a estrutura do banco de dados e tabelas...")
        tables_were_created_or_updated = create_db_and_tables()
        
        if tables_were_created_or_updated:
            print("Banco de dados e tabelas criados/atualizados com sucesso!")
        else:
            print("Estrutura do banco de dados e tabelas já existente e verificada.")
    except Exception as e:
        print(f"Erro ao assegurar a estrutura do banco de dados e tabelas: {e}")
        exit(1)

    if tables_were_created_or_updated:
        print("Iniciando a geração de novos dados...")

        agent = Agent(
            'gemini-2.0-flash',
            output_type=List[AutomobileSchema]
        )

        total_automobiles_to_generate = 100
        batch_size = 10
        num_batches = math.ceil(total_automobiles_to_generate / batch_size)
        all_automobiles: List[AutomobileSchema] = []

        print(f"Serão gerados {total_automobiles_to_generate} automóveis em {num_batches} lotes de {batch_size}.")

        try:
            for i in range(num_batches):
                print(f"Gerando lote {i + 1}/{num_batches}...")
                automobiles_data = agent.run_sync(
                    f'Generate a list of {batch_size} real car data. This data represents a dealership catalog. ' \
                    'You can generate cars with the same models, but with different features. ' \
                    'Ensure the data is varied.'
                )
                all_automobiles.extend(automobiles_data.output)
            print("Todos os lotes de dados foram gerados com sucesso!")

        except Exception as e:
            print(f"Erro ao gerar novos dados: {e}")
            exit(1)

        print("Salvando dados no banco de dados...")
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        with Session() as session:
            try:
                for automobile_data in all_automobiles:
                    db_automobile = Automobile(**automobile_data.model_dump())
                    session.add(db_automobile)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Erro ao salvar dados no banco de dados: {e}")
                exit(1)
        print(f"{len(all_automobiles)} automóveis salvos com sucesso!")
        exit(0)

def start_mcp() -> None:
    print("Servidor MCP iniciado")
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        print(f"Erro ao iniciar o servidor MCP: {e}")
        exit(1)


