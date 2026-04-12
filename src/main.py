from medicine_manager import MedicineManager


def main():
    manager = MedicineManager()
    print("--- Sistema de Controle de Medicamentos ---")

    while True:
        print("\n1. Adicionar Medicamento")
        print("2. Listar Medicamentos")
        print("3. Remover Medicamento")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            name = input("Nome do remédio: ")
            dosage = input("Dosagem (ex: 500mg): ")
            time = input("Horário (ex: 08:00): ")
            try:
                manager.add_medicine(name, dosage, time)
                print("Medicamento agendado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")

        elif choice == "2":
            meds = manager.list_medicines()
            if not meds:
                print("Nenhum medicamento cadastrado.")
            for i, m in enumerate(meds):
                print(f"{i}. {m['name']} - {m['dosage']} às {m['time']}")

        elif choice == "3":
            try:
                idx = int(input("Índice do medicamento para remover: "))
                removed = manager.remove_medicine(idx)
                if removed:
                    print(f"Removido: {removed['name']}")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")

        elif choice == "4":
            break


if __name__ == "__main__":
    main()