from pathlib import Path
from datetime import datetime

PASTA_PACK = Path(__file__).parent
CAMINHO_HISTORICO = PASTA_PACK / "historico.txt"


def salvar_historico(cliente, livro, status):
    with open(CAMINHO_HISTORICO, 'a+', encoding='utf-8') as file:
        data_registro = datetime.now().strftime('%d/%m/%Y %H:%M')
        file.write(
            f"[{data_registro}] | Cliente: {cliente} [{status}] | {livro}\n"
        )
