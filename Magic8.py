'''
Write a magic8.py Python program that can answer any “Yes” or “No” 
question with a different fortune each time it executes.
'''

name = "Eddie"  # Name of person who ask a question
question = "Will mom buy me a toy?" # Question to ask the Magic 8-Ball
answer = "" # The Magic 8-Ball's answer

import random 
# Import a module to use its functions

random_number = random.randint(1, 9)
# Generate a random number between 1 (inclusive) and 9 (inclusive)

print(random_number)