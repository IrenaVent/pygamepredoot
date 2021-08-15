import pygame
import random

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("./runner.png")
        self.position = (x, y)
        self.name = "Tortuga"

    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():

    runners = []
    __startLine = 5
    __finishLine = 620

    def __init__(self):

        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de tortugas")
        self.background = pygame.image.load("./pista.png")

        firstRunner= Runner(self.__startLine, 240)
        firstRunner.name = "Speedy"
        self.runners.append(firstRunner)

    def competir(self):
        
        pygame.init()
        x = 0
        gameOver = False
        

        while not gameOver:
            # comprobación eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True

            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            
            pygame.display.flip()

        pygame.quit()

if __name__ == "__main__":
    juego = Game()
    juego.competir()