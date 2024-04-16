import time
while True:
    choice = input("""Do you want to calculate EMI on your loan:
              1. Yes
              2. No, I want to exit
              Option (1 or 2): """)

    if choice == '1':

        try:
            principal_amount = float(input("Enter your principal amount (₹): "))
            loan_tenure_months = int(input("Enter loan tenure in months: "))
            annual_interest_rate = float(input("Enter your annual interest rate (%): "))
            monthly_interest_rate = annual_interest_rate / 12 / 100
            emi = round((principal_amount * monthly_interest_rate * ((1 + monthly_interest_rate) ** loan_tenure_months)) / (((1 + monthly_interest_rate) ** loan_tenure_months) - 1), 2)
            total_payment = round(emi * loan_tenure_months, 2)
            total_interest = round(total_payment - principal_amount, 2)

            print("\nEMI Calculation:")
            print("Principal Amount: ₹", principal_amount)
            print("Loan Tenure: {} months".format(loan_tenure_months))
            print("Annual Interest Rate: {}%".format(annual_interest_rate))
            print("Monthly EMI: ₹", emi)
            print("Total Payment: ₹", total_payment)
            print("Total Interest: ₹", total_interest)

        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    elif choice == '2':
        for i in range(1,6):
            print("Exiting...please wait")
            time.sleep(1)
        print("Goodbye!")
        break

    else:
        print("Please enter a valid option (1 or 2).")
