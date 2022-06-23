
# # loan_costs = [500, 600, 200, 1000, 450]

# # # This statment finds the number of loans
# # totalNumberOfLoans = len(loan_costs)

# # # This statment finds the sum of all the loans
# # totalSumOfLoans = float(sum(loan_costs))

# # # This statment finds the average of all the loans.
# # averageLoanPrice = totalSumOfLoans / totalNumberOfLoans

# # #These print out the total number of loans, the sum of them, and the avererage price of them.
# # print(f"The total number of loans is: {totalNumberOfLoans}")
# # print(f"The sum of all the loans is $:{totalSumOfLoans: ,}")
# # print(f"The average loan price is $:{averageLoanPrice: ,}")


# loan = {
#     "loan_price": 500,
#     "remaining_months": 9,
#     "repayment_interval": "bullet",
#     "future_value": 1000,
# }

# # This extracts the future value from the dictionary aka the amount the barrower must pay back.
# future_value = loan.get("future_value")
# # This extracts the remaining months to repay the loan from the dicitonary.
# remaining_months = loan.get("remaining_months")
# # prints the remaining months and future value.
# print(
#     f"This loan has {remaining_months} months remaining and it's future value is : ${future_value}")

# # This calulates the present value of the loan.
# fairValue = future_value / (1 + 0.20/12) ** remaining_months
# print(f"The present value of this loan is: ${fairValue: 0.2f}")

# if fairValue >= future_value:
#     print("The loan is worth at least the cost to buy it.")
# else:
#     print("The loan is too expensive and not worth the price")

from pathlib import Path
import csv
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# annual_discount_rate = 0.20


# def present_value_calulator(future_value, remaining_months, annual_discount_rate):
#     # This calulates the present value of the loan.
#     present_value = future_value / \
#         (1 + annual_discount_rate/12) ** remaining_months
#     # This method returns a float type value that represents the present value of the loan.
#     return present_value


inexpensive_loans = []

for row in loans:
    if row.get("loan_price") <= 500:
        inexpensive_loans.append(row)
print(inexpensive_loans)


header = ["loan_price", "remaining_months",
          "repayment_interval", "future_value"]
pathOfOurCsv = Path("list_of_inexpensive_loans.csv")

with open(pathOfOurCsv, 'w', newline='') as currentOpenFile:
    # creates a writer object that allows us to write to our open file
    csvwriter = csv.writer(currentOpenFile)

    # writes the header first
    csvwriter.writerow(header)

    # This for loop writes the data in one row at a time
    for row in inexpensive_loans:
        # This will write only the values of the dicitonaries to the row excluding the key values.
        # values() essentially converts a dictionary into a list
        csvwriter.writerow(row.values())
