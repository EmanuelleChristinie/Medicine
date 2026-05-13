import requests

class MedicineManager:
    def __init__(self):
        self.medicines = []

    def add_medicine(self, name, dosage, time):
        if not name or not dosage or not time:
            raise ValueError("Todos os campos devem ser preenchidos.")

        medicine = {"name": name, "dosage": dosage, "time": time}
        self.medicines.append(medicine)
        return medicine

    def list_medicines(self):
        return self.medicines

    def remove_medicine(self, index):
        try:
            return self.medicines.pop(index)
        except IndexError:
            return None

    def buscar_cep(self, cep):
        """Integração com a API ViaCEP"""
        url = f"https://viacep.com.br/ws/{cep}/json/"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                dados = response.json()
                if "erro" in dados:
                    return "CEP não encontrado."
                return f"{dados.get('logradouro', 'Sem logradouro')}, {dados.get('bairro', 'Sem bairro')} - {dados.get('localidade', 'Sem cidade')}/{dados.get('uf', '??')}"
            return "Erro na consulta da API."
        except Exception:
            return "Falha na conexão com o serviço de CEP."