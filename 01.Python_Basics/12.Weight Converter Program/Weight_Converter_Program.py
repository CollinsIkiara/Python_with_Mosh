# This program converts weight from pounds to kilograms and vice versa. It takes the weight and the unit of measurement as input from the user and then performs the conversion based on the unit provided.

weight = float(input("Weight: "))
unit_weight = input("(L)bs or (K)g: ").lower()

if unit_weight == "k":
    weight_lbs = weight // 0.45
    print(f"You are {weight_lbs} pounds.")
elif unit_weight == "l":
    weight_kgs = weight * 0.45
    print(f"You are {weight_kgs} kilograms.")