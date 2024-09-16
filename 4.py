def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time period (years): "))

SI = simple_interest(P, R, T)
print(f"Simple Interest: {SI}")


