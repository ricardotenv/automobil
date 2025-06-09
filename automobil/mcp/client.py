from pydantic_ai.providers.google_gla import GoogleGLAProvider # type: ignore
from pydantic_ai.models.gemini import GeminiModel # type: ignore
from pydantic_ai.mcp import MCPServerStdio # type: ignore
from pydantic_ai.agent import Agent # type: ignore
from automobil.settings import Settings
import asyncio
import sys

async def run_chat():
    print("Iniciando o cliente MCP e o agente de IA... Por favor, aguarde.")

    api_key = Settings().GEMINI_API_KEY
    if not api_key or api_key == "YOUR_GEMINI_API_KEY_HERE":
        print("\n[ERRO] Chave da API da Gemini (GEMINI_API_KEY) não encontrada ou não configurada no arquivo .env.")
        print("Por favor, adicione sua chave ao arquivo .env para continuar.")
        return

    full_command = [sys.executable, "-m", "automobil.cli", "start-mcp"]
    
    command_executable = full_command[0]
    command_args = full_command[1:]

    try:
        server = MCPServerStdio(command_executable, args=command_args)

        model = GeminiModel(
            'gemini-2.0-flash',
            provider=GoogleGLAProvider(api_key=api_key)
        )

        agent = Agent(
            model,
            mcp_servers=[server],
            system_prompt=(
                "Você é um vendedor de carros virtual, e seu objetivo principal é usar a ferramenta 'query_automobiles' para encontrar carros para o cliente.\n"
                "Inicie a conversa e, assim que o usuário mencionar um critério de busca (como modelo, marca, cor, etc.), execute imediatamente a ferramenta 'query_automobiles'.\n"
                "Não espere por mais informações. Seja proativo. É melhor mostrar alguns resultados e depois pedir para refinar a busca do que fazer muitas perguntas antes.\n"
                "Após a busca, apresente os resultados de forma clara. Se nenhum carro for encontrado, informe o usuário e peça mais detalhes para tentar novamente."
            )
        )
        
        async with agent.run_mcp_servers():
            print("\n--- Agente Automobil (Online) ---")
            print("Olá! Sou seu assistente de vendas virtual. Como posso te ajudar a encontrar o carro dos seus sonhos hoje?")
            print("Para encerrar, digite 'sair' a qualquer momento.")
            print("---------------------------------")

            message_history = []

            while True:
                user_input = await asyncio.to_thread(input, "Você: ")
                if user_input.lower() in ["sair", "exit", "quit"]:
                    print("Agente: Foi um prazer conversar! Volte sempre que precisar.")
                    break
                
                if not user_input.strip():
                    continue

                result = await agent.run(user_input, message_history=message_history)
                
                message_history = result.new_messages()
                print("Agente: ", result.output)
                print()


    except KeyboardInterrupt:
        print("\n\nAgente: Conversa interrompida. Até mais!")
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {e}")
