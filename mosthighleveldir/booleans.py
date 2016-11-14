age = 30

print(age > 10) # Expected outcome:true

print(10 < age) # Expected outcome:true

print(age > 10 + 20) # Expected outcome:false

print(age + 20 > 10) # Expected outcome:true
print('...')
print('a' > 'z') # Expected outcome:false

print('z' > 'a') # Expected outcome:true

print('apples' > 'oranges') # Expected outcome:false

print('oranges' > 'apples') # Expected outcome:true

print('cat' > 'car') # Expected outcome:true

print('car' > 'cat') # Expected outcome:false
print('...\nLogical Operators')
age = 1
print(age > 12 and age < 19) # Expected outcome:f

age = 14
print(age > 12 and age < 19) # Expected outcome:t

age = 19
print(age > 12 and age < 19) # Expected outcome:f

age = 18
print(age > 12 and age < 19 and age != 5) # Expected outcome:t

age = 5
print(age > 12 and age < 19 and age != 5) # Expected outcome:f

age = -1
print(age > 12 and age < 19) # Expected outcome:f

age = 10
print(age > 25 and age < 15) # Expected outcome: f   
# Could the above expression ever be True?no
print('...\nRock Paper Scissors')
gesture = 'rock'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome:true

gesture = 'pape'
print(gesture == 'rock' or gesture == 'paper' or gesture == 'scissors') # Expected outcome:false

gesture = 'rock'
print(gesture == 'rock' and gesture == 'paper' or gesture == 'scissors') # false

print('....How Old')
age = int(raw_input('How old are you?'))
print(age >= 5 and age <= 10)