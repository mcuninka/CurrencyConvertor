import random

words = ['python', 'java', 'kotlin', 'javascript']
print('H A N G M A N')

while True: 
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice == 'play':
        random_word = random.choice(words)
        guessed_word = "-" * len(random_word)
        letters = set()
        lives = 8
        
        while lives > 0:
            print(f'\n{guessed_word}')
            guess = input('Input a letter: ')

            if len(guess) != 1:
                print('You should input a single letter')
            else:
                if not guess.islower():
                    print('Please enter a lowercase English letter')
                else:
                    if guess not in random_word:
                        if guess not in letters:
                            print("That letter doesn't appear in the word")
                            lives -= 1
                            letters.add(guess)
                            if lives == 0:
                                print('You lost!\n')
                                break
                        else:
                            print("You've already guessed this letter")
                    elif guess in guessed_word:
                        print("You've already guessed this letter")
                    else:
                        for i in range(len(random_word)):
                            if random_word[i] == guess:
                                guessed_word = guessed_word[:i] + guess + guessed_word[i + 1:]
                    if guessed_word == random_word:
                                    print('You guessed the word!\nYou survived!\n')
                                    break
    elif choice == 'exit':
        break
    
