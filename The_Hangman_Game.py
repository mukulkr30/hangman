#list = ["mukul","kumar","mango","apple","dark","elephant","google","practice"]
import random
import hangman_words
import hangman_stage
stage = (hangman_stage.stages)
chosen_word = random.choice(hangman_words.list)
print("The HANGMAN game")
print("Are you ready to play..........")
length = len(chosen_word)
blank_list = []
for l in range(len(chosen_word)):
    blank_list+="_"
print(blank_list)
life = 6
eog = False
while eog == False and life!=0:
    
    guess = input("guess a letter").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            blank_list[position]=guess        
    if guess not in chosen_word:
        life-=1
        print("you choose",guess,"it is not in word,you loose a life")
    print(stage[life])
    print(blank_list)
    if blank_list.count("_") == 0:
        eog = True
        print("you win")
if life == 0:
    print("you loss")
    print("the word was",chosen_word)