import pytest
from src.medicine_manager import MedicineManager

def test_consulta_cep_valido():
    manager = MedicineManager()
    # Testando com o CEP do CEUB (70790-075)
    resultado = manager.buscar_cep("70790075")
    assert "Asa Norte" in resultado
    assert "Brasília" in resultado

def test_consulta_cep_inexistente():
    manager = MedicineManager()
    resultado = manager.buscar_cep("00000000")
    assert resultado == "CEP não encontrado."