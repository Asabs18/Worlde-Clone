
# READ IN LIST OF WORDLE ALLOWED GUESSES 
wordleAllowedGuesses_F = open('Words/wordle-allowed-guesses.txt', 'r')
wordleAllowedGuesses = wordleAllowedGuesses_F.readlines()

# STRIP NEW LINE CHARACTER FROM WORDLE ALLOWED GUESSES 
for x, word in enumerate(wordleAllowedGuesses):
    wordleAllowedGuesses[x] = word.strip()

# READ IN LIST OF WORDLE ANSWERS
wordleAnswers_F = open('Words/wordle-answers.txt', 'r')
wordleAnswers = wordleAnswers_F.readlines()

# STRIP NEW LINE CHARACTER FROM WORDLE ALLOWED GUESSES 
for x, word in enumerate(wordleAnswers):
    wordleAnswers[x] = word.strip()