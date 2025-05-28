class patients:
    def __init__(self, name, age, date, history):
        self.name = name
        self.age = age
        self.latestadmission = date
        self.history = history

    def information_print(self):
        print(
            f"Name: {self.name}, Age: {self.age}, Last Hospitalization Date: {self.latestadmission}, History: {self.history}")


# example
patient_list = (patients("John Doe", 30, "2024-10-11", "No known allergies"), patients("Jane Smith",
                25, "2023-1-02", "Allergic to penicillin"), patients("Alice Johnson", 40, "2024-10-05", "Diabetic"))
patients.information_print(patient_list[0])
