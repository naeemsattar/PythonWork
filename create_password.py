# Create the secure password.
import string
import random


def create_password():
    adjectives = ['attractive', 'bald', 'beautiful', 'chubby', 'clean', 'dazzling', 'drab', 'elegant',
                  'fancy', 'fit', 'flabby', 'glamorous', 'gorgeous', 'handsome', 'long'
        , 'magnificent', 'muscular', 'plain', 'plump', 'quaint', 'scruffy', 'shapely', 'short',
                  'skinny', 'stocky', 'ugly', 'unkempt', 'unsightly']

    nouns = ['area', 'book', 'business', 'case', 'child', 'company', 'country', 'day',
             'eye', 'family', 'government', 'hand', 'home', 'life', 'lot'
        , 'man', 'money', 'month', 'mother', 'Mr', 'night', 'number', 'part',
             'question', 'right', 'room', 'school', 'state', 'student', 'week', 'world',
             'year', 'water', 'thing', 'system', 'work']

    colors = ['White', 'Yellow', 'Blue', 'Green', 'Brown', 'Azure', 'Black', 'Gold', 'Silver']

    while True:
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        color = random.choice(colors)
        number = random.randrange(0, 100)
        special_char = random.choice(string.punctuation)
        password = adjective + color + noun  + str(number)  + special_char;
        print("Your Password : " + password)
        response = input("Do you want another Password? Type y or n")
        if response == 'n':
            break

    print("Your Password : " + password)


create_password()
