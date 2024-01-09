
#Use dictionary to store information about a person you know.
#Store their first name, last name, age, city in which they live 
#.YOu should have keys such as first_name, last_name, age and city.
#Print each piece of information stored in your dictionary


person = {
    'first_name': "md",
    'last_name': "billah",
    'age': 39,
    'city': "Austin",
}

print(person["first_name"])
print(person['last_name'])
print(person['age'])
print(person['city'])

'''

out put :
md
billah
39
Austin

'''

#Favorite numbers:
'''
Use a dictinary to store people's favoorite numbers. Think of five names and use
them as keys in your dictionary. Think of a fovorite number for each person and store 
each as a value in your dictionary. Print each person's name and their favorite number .
For even more fun, poll a few friends and get some actual data for your program

'''
favorite_numbers = {
    'mandy': 42,
    'micah': 23,
    'gus': 7,
    'hank': 1000_000,
    'maggie': 0,
}

num = favorite_numbers['mandy']
print(f"Mandy's favorite number is {num}")

num = favorite_numbers['micah']
print(f"Micah's favorite number is {num}.")

num = favorite_numbers['gus']
print(f"Gus's favorite number is {num}.")

num = favorite_numbers['hank']
print(f"Hank's favorite number is {num}.")

num = favorite_numbers['maggie']
print(f"Maggie's favorite number is {num}.")

'''
Mandy's favorite number is 42.
Micah's favorite number is 23.
Gus's favorite number is 7.
Hank's favorite number is 1000000.
Maggie's favorite number is 0.

'''

#Glossary
'''
 A python dictionary can be used to model an actual dictionary. HOwever, to avoid 
 confusion let's call it glossary

 --.1. Think of five progrmaing words you have learned previuoly. Use this words as the key
 ---in your glossary, and store their meanings as values.
 --2. print each word and its meaning as neatly formatted output. You might print the 
 ---word followed by a colon and then its meaning or print the word on one line and then
 ---print its meaning indented on a second line. Use the newline character {'\n'} to insert a 
 blank line between each word-meaning pair in your output

'''
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
}

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")
























