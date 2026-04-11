import pytest
from src.medicine_manager import MedicineManager

def test_add_medicine_success():
    manager = MedicineManager()
    med = manager.add_medicine("Dipirona", "1g", "12:00")
    assert len(manager.list_medicines()) == 1
    assert med["name"] == "Dipirona"

def test_add_medicine_empty_fields():
    manager = MedicineManager()
    with pytest.raises(ValueError):
        manager.add_medicine("", "500mg", "")

def test_remove_invalid_index():
    manager = MedicineManager()
    result = manager.remove_medicine(99)
    assert result is None