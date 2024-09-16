net_amount = 0

while True:
    transaction = input("Enter transaction (D/W amount or 'STOP' to end): ")
    if transaction.lower() == "stop":
        break
    type_of_transaction, amount = transaction.split()
    amount = int(amount)

    if type_of_transaction == 'D':
        net_amount += amount
    elif type_of_transaction == 'W':
        net_amount -= amount

print(f"Net amount in bank account: {net_amount}")
