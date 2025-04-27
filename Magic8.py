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

# print(random_number)

''' 
I decided to use a match-case statement for practice, 
but I could also use an if/elif/else statement
'''

match random_number: # Get random_number and change the answer variable depends on its value
  case 1:
    answer = "Yes - definitely"
  case 2: 
    answer = "It is decidedly so"
  case 3: 
    answer = "Without a doubt"
  case 4: 
    answer = "Reply hazy, try again"
  case 5: 
    answer = "Ask again later"
  case 6: 
    answer = "Better not tell you now"
  case 7: 
    answer = "My sources say no"
  case 8: 
    answer = "Outlook not so good"
  case 9:
    answer = "Very doubtful"
  case default: 
    answer = "Error"

# Print to output asker's name and their question
# print(name + " asks: " + question) 

# Print to output Magic 8-Ball's answer
# print("Magic 8-Ball's answer: " + answer)

''' 
What if the asker does not provide a name, 
such that the value of name is an empty string?
'''

question_with_name = name + " asks: " + question
question_without_name = "Question: " + question

match name: # Print question to the console depends on name variable
  case "":
    print(question_without_name) 
  case default: 
    print(question_with_name)


# What if the question string is empty?

is_question = "Magic 8-Ball's answer: " + answer
isnt_question = "You have to ask a question!"
