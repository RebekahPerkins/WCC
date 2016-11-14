


print('Welcome to the Mad Lib Generator!\n')
advective1 = raw_input('Type in an adjective:')
#Type in an adjective: fearless
advective2 = raw_input('Another adjective:')
#Another adjective: gooey
advective3 = raw_input('And another adjective: ')
#And another adjective: sassy
advective4 = raw_input('One more adjective: ')
#One more adjective: fancy
plural_animal = raw_input('Plural animal (e.g., puppies): ')
#Plural animal (e.g., puppies): elephants
verb = raw_input('Now a verb: ')
#Now a verb: skip
plural_noun = raw_input('Now a plural noun: ')
#Now a plural noun: marbles
musician = raw_input('The first name of a woman musician: ')
#The first name of a woman musician: Ani
beverage = raw_input('A beverage: ')
#A beverage: chocolate milk
body_parts = raw_input('And finally, a plural body part: ')
#And finally, a plural body part: knees

print('\nExcellent choices! Here\'s your story...\n--------------------------------\nThere once was a ' + advective1 + ' programmer named ' + musician)
print('who wanted to build a ' + advective2 + ' mobile app to\nhelp ' + advective3 + ' ' + plural_animal + ' find new homes.')
print(musician + ' stayed up all night, drinking lots of\ncaffeinated ' + beverage + ' as she worked and worked')
print('trying to complete her ' + advective4 + ' program.\n')
print('Whenever ' + musician + ' hit a dead end, she would\nexclaim *' + plural_noun + '*!\n')
print('But she was not discouraged, and after a quick break\nto ' + verb + ' and clear her head, she got back to work.\n')
print('By morning, when the sun started to rise, she let out a\nbig yawn and stretched her ' + body_parts + '.\nFinally, she was done.\n--------------------------------')