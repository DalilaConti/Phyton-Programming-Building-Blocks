#Activity for practice true/false variables; AND or; IF
print("For each of these questions, please provide a 1-10 rating:")
large_loan = int(input('How large is the loan?'))
credit_history = int(input('How good is your credit history?'))
high_income = int(input('How high is your income?'))
down_payment = int(input('How large is your down payment?'))
should_loan = False

if large_loan >= 5:
 if credit_history >= 7 and  high_income >=7:
  should_loan = True
 else:
  should_loan = False
else: # This means its a small loan
    if credit_history < 4:
        should_loan = False
    else:
        if high_income >= 7 or down_payment >= 7:
            should_loan = True
        elif high_income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

if should_loan:
    print("The decision is yes. This is a good loan.")
else:
    print("The decision is no. You should not loan this money.")


