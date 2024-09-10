import json

# import messages from a config file
with open('loan_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# prompt template
def p(message):
    return f'==> {MESSAGES[message]}'

# invalidating non numeric values
def invalid_input(inp):
    try:
        float(inp)
    except ValueError:
        return True
    return inp in ['inf', 'nan']

# invalidating zero
def invalid_no_zero(inp):
    if inp == '0':
        return True
    return invalid_input(inp)

# calculating monthly pay
def calc_monthly_pay(amount, rate, duration):
    try:
        result = amount * (rate /
                            (1 - (1 + rate) **
                            (-duration)))
    except ZeroDivisionError:
        result = amount / duration
    return result

# validating again input
def invalid_again(answer):
    return answer.casefold() not in ['y', 'n']

# welcomes user
print("""
-------------------------------
Welcome to Mortgage Calculator!
-------------------------------
      """)

# gathers input, does calculations, displays result, allows for repetition
while True:

    # asking for and validating user input
    loan_amt = input(p('loan_amt'))
    while invalid_no_zero(loan_amt):
        loan_amt = input(p('valid_loan'))

    # allows for zero interest rate calc
    apr = input(p('apr'))
    while invalid_input(apr):
        apr = input(p('valid_apr'))

    loan_dur_yr = input(p('loan_dur_yr'))
    while invalid_no_zero(loan_dur_yr):
        loan_dur_yr = input(p('valid_dur'))

    # Coercing variables to float for calculations
    loan_amt = float(loan_amt)
    apr = float(apr) / 100
    loan_dur_yr = float(loan_dur_yr)

    # calculating further variables
    monthly_rt = apr / 12
    loan_dur_mt = loan_dur_yr * 12
    monthly_pay = calc_monthly_pay(loan_amt, monthly_rt, loan_dur_mt)

    # displaying the result
    print("""
-------------------------------
          
          """)
    print(p('result').format(monthly_pay=monthly_pay))
    print("""
-------------------------------
          """)

    # asking user for another calculation, break if n
    again = input(p('again'))
    while invalid_again(again):
        again = input(p('valid_again'))
    if again == 'n':
        print('buh bye!')
        break

    print("""
-------------------------------
""")