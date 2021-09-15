from quotes import them_quotes
import random

#print(type(them_quotes))

def get_quote():
    number = random.randint(0,len(them_quotes)-1)
    return (them_quotes[number])

get_quote()

