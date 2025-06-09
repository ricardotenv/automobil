from automobil.mcp.client import run_chat
import asyncio
import os

def main():
    os.environ['AUTOMOBIL_CLI_MODULE'] = 'automobil.cli'
    
    try:
        asyncio.run(run_chat())
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")

if __name__ == "__main__":
    main()