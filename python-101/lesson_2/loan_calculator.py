MONTHS_PER_YEAR = 12


def prompt(message):
    print(f"==> {message}")


def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError(f"Value must be > 0: {number_str}")
    except ValueError:
        return True
    return False


def calculate_monthly_payment(loan_amount, loan_yearly_apr, loan_duration_in_month):
    loan_monthly_apr = loan_yearly_apr / MONTHS_PER_YEAR
    return loan_amount * (loan_monthly_apr / (1 - (1 + loan_monthly_apr) ** (-loan_duration_in_month)))


def loan_calculator_program():
    prompt("Please enter the loan amount: ")
    loan_amount = input()
    while invalid_number(loan_amount):
        prompt("Please enter a valid value")
        loan_amount = input()

    prompt("Please enter the APR (Annual Percentage Rate): ")
    loan_yearly_apr = input()
    while invalid_number(loan_yearly_apr):
        prompt("Please enter a valid value")
        loan_yearly_apr = input()

    prompt("Please enter the loan duration: ")
    loan_duration_in_years = input()
    while invalid_number(loan_duration_in_years):
        prompt("Please enter a valid value")
        loan_duration_in_years = input()
    monthly_payment = calculate_monthly_payment(
        float(loan_amount), float(loan_yearly_apr), float(loan_duration_in_years) * MONTHS_PER_YEAR)

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
