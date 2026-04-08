# In this example, we take the weight in pounds as input from the user, convert it to a float, and then calculate the weight in kilograms by multiplying it by 0.45. Finally, we print the result.

weight_lbs = input('Weight (lbs): ')
weight_kg = float(weight_lbs) * 0.45
print('Weight (kg): ' + str(weight_kg))