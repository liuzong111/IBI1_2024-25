# drug_dosage_calculator.py
# This script calculates the required volume of paracetamol solution for children.

def calculate_paracetamol_volume(weight, strength):

    if weight < 10 or weight > 100:
        return "Error: Weight out of range (10-100 kg)"
    if strength not in (120, 250):
        return "Error: Paracetamol strength must be 120 mg/5ml or 250 mg/5ml"

    required_dose = weight * 15
    volume = (required_dose * 5) / strength
    return volume


weight = int(input("Weight_in_kg"))
strength = int(input("Strength_in_mg/kg"))
print(calculate_paracetamol_volume(weight, strength))
