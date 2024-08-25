pennies = .01
nickels = .05
dimes = .10
quarters = .25
dollars = 1

announcement = print('This is a program to find out how much money you have')
num_of_pennies = input('How many pennies do you have ')
num_of_nickels = input('How many nickels do you have ')
num_of_dimes = input('How many dimes do you have ')
num_of_quarters = input('How many quarters do you have ')
num_of_dollars = input('How many dollars do you have? ')

pennie_result = num_of_pennies * pennies
nickel_result = num_of_nickels * nickels
dime_result = num_of_dimes * dimes
quarter_result = num_of_quarters * quarters
dollar_result = num_of_dollars * dollars

total = quarter_result + dime_result + nickel_result + pennie_result + dollar_result
print('You have: ')
print(total)
