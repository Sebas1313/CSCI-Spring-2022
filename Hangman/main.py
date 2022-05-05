import re

#Answer of puzzle 
answer = "What's up, Doc?"

answer = answer.upper()

guessed_answer = []

#determine if the character in the answer needs to be guessed
for answer_character in answer:
  if re.search("^[A-Z]$", answer_character):
    guessed_answer.appened(False)
  else:
    guessed_answer.append(True)


#Game logic.
TOTAL_NUM_OF_INCORRECTED_GUESSES_ALLOWED = 5 
num_of_incorrect_guesses = 0 
guessed_letters = []

while num_of_incorrect_guesses <TOTAL_NUM_OF_INCORRECTED_GUESSES_ALLOWED and False in guessed_answer:
  print("---------------------------------------")
  print("Guessed letters: ", end = "")


  for current_guessed_letters in guessed_letters:
    print(f"{current_guessed_letters}", end= "")

  print(f"Number of incorrect guesses remaining:{TOTAL_NUM_OF_INCORRECTED_GUESSES_ALLOWED}")

  print()

  for answer_index in range(len(answer)):
    if guessed_answer[answer_index]:
      print(answer[answer_index], end = "")
    else:
      print("_", end = "")

  print()

  letter = input("Enter a letter: ")

  letter = letter.upper()

  if letter not in guessed_letters and len(letter) == 1 and re.search("^[A-Z]$", letter):
    #process the letter in the puzzle 
    guessed_letters_insert_index = 0 

    for current_guessed_letters in guessed_letters:
      if letter < current_guessed_letters:
        break

      guessed_letters_insert_index += 1 

    guessed_letters.insert(guessed_letters_insert_index, letter)

    if letter in answer: 
      #letter guessed is in the puzzle 