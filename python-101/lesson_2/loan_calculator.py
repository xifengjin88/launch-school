MONTHS_PER_YEAR = 12


def prompt(message):
    print(f"==> {message}")


def calculate_monthly_payment(loan_amount, loan_yearly_apr, loan_duration_in_month):
    loan_monthly_apr = loan_yearly_apr / MONTHS_PER_YEAR
    return loan_amount * (loan_monthly_apr / (1 - (1 + loan_monthly_apr) ** (-loan_duration_in_month)))


def loan_calculator_program():
    prompt("Please enter the loan amount: ")
    loan_amount = float(input())
    prompt("Please enter the APR (Annual Percentage Rate): ")
    loan_yearly_apr = float(input())
    prompt("Please enter the loan duration: ")
    loan_duration_in_years = float(input())
    monthly_payment = calculate_monthly_payment(
        loan_amount, loan_yearly_apr, loan_duration_in_years * MONTHS_PER_YEAR)

    print(f"Your monthly payment is ${monthly_payment:.2f}")


def main():
    prompt("Welcome to loan calculator!")
    while True:
        loan_calculator_program()
        prompt("Would you like to continue? y|n")
        response = input()
        if response and response.strip() != "y":
            break


main()
