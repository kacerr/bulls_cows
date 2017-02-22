import random

def evaluate_guess(secret, guess):
  bulls = 0
  cows = 0
  for i in range(4):
    if (secret[i] == guess[i]):
      bulls +=1
    elif guess[i] in secret:
      cows +=1
  return [bulls, cows]

def is_string_valid_bulls_cows_number(string_value):
  if not string_value.isnumeric or len(string_value) != 4:
    return False
  
  for i in range(4):
    if i==0:
      if string_value[i] in string_value[1:]:
        return False
    else:
      if string_value[i] in (string_value[:i-1] + string_value[i+1:]):
        return False
  return True


# Generate random for digit number with each digit unique
# if number is between 900-999 then add zero as first digit
secret = "0"
while not is_string_valid_bulls_cows_number(secret):
  secret = str(random.randint(100,999))
  if len(secret) == 3: 
    secret = "0" + secret

print("I have generated random 4-digit number, let's see how many guesses you need to find it. \n")
guess_count=0

while True:
  guess_count += 1
  guess = input("Enter you guess number #{0}. (you are looking for 4 digit number: ".format(guess_count))

  if guess!="x" and guess!="cheat" and not is_string_valid_bulls_cows_number(guess):
    print("Invalid guess, it has to be 4 digit number with each digit unique !!!!")
    continue
  
  if guess == "x":
    print ("You have exited the program without finding correct result, better luck next time")
    break

  if guess == "cheat":
    print ("You should not cheat !!!!. Number you are looking for is {0}".format(secret))

  if guess == secret:
    print("Nice!, you have found it, correct number was: {0}. You needed {1} guesses".format(secret, guess_count))
    break;

  # evaluate bulls and cows
  result = evaluate_guess(secret, guess)
  print("Your guess: {0} hit {1} bulls and {2} cows. \n\n".format(guess, result[0], result[1]))
  


