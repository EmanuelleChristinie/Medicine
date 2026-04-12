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