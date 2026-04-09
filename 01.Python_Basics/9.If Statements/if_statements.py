# The following if statement checks if the variable has_good_credit is True. If it is, it calculates a downpayment of 10% of the price. If it is not, it calculates a downpayment of 20% of the price.

price = 1000000
has_good_credit = True

if has_good_credit:
    print("Pay a downpayment of 10%")
    downpayment = price * 0.1
    print(f"Downpayment: ${downpayment}")
else:
    print("Pay a downpayment of 20%")
    downpayment = price * 0.2
    print(f"Downpayment: ${downpayment}")