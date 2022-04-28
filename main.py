from locale import windows_locale
import pygame, sys
from assets import *
from inputGrid import InputGrid

pygame.init()

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Wordle!')

inputGrid = InputGrid()

def main():
    run = True
    guess = []
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(guess) == 5 and inputGrid.isValidGuess(guess):
                    guessStr = " "
                    inputGrid.guess(guessStr.join(guess))
                    win = inputGrid.checkWin(guess)
                    if inputGrid.isEnd(win):
                        run = False
                    guess = []
                if pygame.key.name(event.key).isalpha() and len(guess) < 5 and len(pygame.key.name(event.key)) == 1:
                    guess.append(inputGrid.updateRow(pygame.key.name(event.key)))
                elif event.key == pygame.K_BACKSPACE and len(guess) > 0:
                    guess.pop()
                    inputGrid.deleteLetter()


        WIN.fill(BACKGROUND_C)
        inputGrid.draw(WIN)
        pygame.display.update()         
    pygame.quit()

if __name__ == "__main__":
    main()