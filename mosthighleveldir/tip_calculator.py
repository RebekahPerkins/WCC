meal_price = float(raw_input('How much was your meal? '))
print('How would you rate the service? ')
print('a. Not so good')
print('b. Good')
print('c. Excellent!')
chosen_option = raw_input('Choose an option: ')

# Here's where conditionals come in...
if chosen_option == 'a':
    percentage = .15;
elif chosen_option == 'b':
    percentage = .18;
elif chosen_option == 'c':
    percentage = .20;
else:
    percentage = .20;
    print ('You did not enter a valid option, defaulting to 20%.')

tip = meal_price * percentage
total_price = meal_price + tip
print('You should tip $' + str(tip))
print('Your total cost would be $' + str(total_price))