import pytest
import tempfile
import os
import csv
from first_py import ler_csv

@pytest.fixture
def arquivo_csv_temporario():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', newline='', encoding='utf-8') as arquivo_temp:
        nome_arquivo = arquivo_temp.name
        escritor = csv.writer(arquivo_temp)
        escritor.writerow(["nome", "idade", "cidade"])
        escritor.writerow(["Alice", "30", "São Paulo"])
        escritor.writerow(["Bob", "25", "Rio de Janeiro"])
    yield nome_arquivo
    os.remove(nome_arquivo)

def test_ler_csv_sucesso(arquivo_csv_temporario):
    esperado = [
        {"nome": "Alice", "idade": "30", "cidade": "São Paulo"},
        {"nome": "Bob", "idade": "25", "cidade": "Rio de Janeiro"}
    ]
    assert ler_csv(arquivo_csv_temporario) == esperado

def test_ler_csv_arquivo_nao_existe():
    with pytest.raises(FileNotFoundError):
        ler_csv("arquivo_inexistente.csv")

