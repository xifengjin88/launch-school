balance = 1000
interest = 0.05
num_of_years = 5

balance = balance * (1 + interest) ** num_of_years

print(f"{balance:.2f}")