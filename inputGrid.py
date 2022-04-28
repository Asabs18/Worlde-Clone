from mimetypes import guess_all_extensions
import pygame, random, time
from words import *
from assets import *

pygame.init()

class InputGrid:
    def __init__(self):

        self.numColumns = NUM_COLUMNS
        self.numRows = NUM_ROWS

        self.numBoxes = self.numColumns * self.numRows

        self.boxSize = BOX_SIZE

        self.borderColor = BOX_C

        self.boxColors = [BACKGROUND_C for i in range(self.numBoxes)]
        self.boxCoords = self.initBoxCoords()
        self.boxValues = [0 for i in range(self.numBoxes)]
        self.words = [[" " for i in range(self.numColumns)] for i in range(self.numRows)]

        self.answer = random.choice(wordleAnswers)
        print(self.answer)

        self.rowsGuessed = 0
        self.colsGuessed = 0

    def initBoxCoords(self):
        boxCoords = []
        for i in range(self.numRows):
            for j in range(self.numColumns):
                boxCoords.append((BOX_X + (j * BOX_X) + (BOX_GAP * j), BOX_Y + (i * BOX_Y)  + (BOX_GAP * i)))
        return boxCoords

    def drawBox(self, WIN, boxX, boxY):
        boxIndex = (boxX * self.numColumns) + boxY
        pygame.draw.rect(WIN, self.borderColor, pygame.Rect(self.boxCoords[boxIndex][BOX_COORDS_X], self.boxCoords[boxIndex][BOX_COORDS_Y], self.boxSize, self.boxSize))
        pygame.draw.rect(WIN, self.boxColors[boxIndex], pygame.Rect(self.boxCoords[boxIndex][BOX_COORDS_X] + LINE_WIDTH, self.boxCoords[boxIndex][BOX_COORDS_Y] + LINE_WIDTH, self.boxSize - LINE_WIDTH * 2, self.boxSize - LINE_WIDTH * 2))
        letter = FONT.render(self.words[boxX][boxY], False, LETTER_C, None)
        letterRect = pygame.Rect(self.boxCoords[boxIndex][BOX_COORDS_X] + 20, self.boxCoords[boxIndex][BOX_COORDS_Y], self.boxSize - 40, self.boxSize)
        WIN.blit(letter, letterRect)

    def draw(self, WIN):
        for i in range(self.numRows):
            for j in range(self.numColumns):
                self.drawBox(WIN, i, j)

    def colorBoxes(self):
        for x, box in enumerate(self.boxValues):
            if box == IN_WORD_WRONG_PLACE:
                self.boxColors[x] = YELLOWBOX_C
            elif box == IN_WORD_RIGHT_PLACE:
                self.boxColors[x] = GREENBOX_C
            elif box == NOT_IN_WORD:
                self.boxColors[x] = DARK_GREY

    def wordDiff(self, guess):
        wordDiff = [NOT_A_WORD for i in range(WORD_LENGTH)]
        if guess in wordleAllowedGuesses or guess in wordleAnswers:
            wordDiff = [NOT_IN_WORD for i in range(WORD_LENGTH)]
            #Check for in word wrong place
            for x, letter in enumerate(guess):
                if letter in self.answer:
                    wordDiff[x] = IN_WORD_WRONG_PLACE
            #Check for in word right place
            for x, letter in enumerate(guess):
                if letter == self.answer[x]:
                    wordDiff[x] = IN_WORD_RIGHT_PLACE
        return wordDiff

    def guess(self, guess):
        guess.lower()
        guess.strip()
        self.words[self.rowsGuessed] = []
        guessStr = ""
        for letter in guess:
            if letter != " ":
                self.words[self.rowsGuessed].append(letter)
                guessStr = f"{guessStr}{letter}"
        self.recolorBoxes(guessStr)

    def recolorBoxes(self, guess):
        wordDiff = self.wordDiff(guess)
        wordDiffIndex = 0
        for x in range(self.rowsGuessed * NUM_COLUMNS, (self.rowsGuessed + 1) * NUM_COLUMNS):
            self.boxValues[x] = wordDiff[wordDiffIndex]
            wordDiffIndex += 1
        self.colorBoxes()
        if self.rowsGuessed < 5:
            self.rowsGuessed += 1
            self.colsGuessed = 0
        
    def updateRow(self, letter):
        self.words[self.rowsGuessed][self.colsGuessed] = letter
        self.colsGuessed += 1
        return letter

    def deleteLetter(self):
        self.words[self.rowsGuessed][self.colsGuessed - 1] = " "
        self.colsGuessed -= 1

    def isValidGuess(self, guess):
        isValidGuess = False
        guess = self.stringifyArray(guess)
        if guess in wordleAllowedGuesses or guess in wordleAnswers:
            isValidGuess = True
        return isValidGuess

    def stringifyArray(self, guess):
        guessStr = ""
        for letter in guess:
            guessStr = f"{guessStr}{letter}"
        return guessStr

    def checkWin(self, guess):
        win = False
        guess = self.stringifyArray(guess)
        if guess == self.answer:
            win = True
            print("You Win!")
        return win

    def isEnd(self, win):
        end = False
        if win or self.words[5][0] != " ":
            end = True
        return end