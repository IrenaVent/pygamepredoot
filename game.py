import pygame
import random

class Runner():
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("./runner.png")
        self.position = [x, y]
        self.name = "Tortuga"

    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():

    runners = []
    __posY = (130, 200, 270, 340)
    __names = ("Irena", "Óscar", "Kun", "Alejandro")
    __startLine = 5
    __finishLine = 620

    def __init__(self):

        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de tortugas")
        self.background = pygame.image.load("./pista.png")

        for i in range (4):
            theRunner= Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)

    def close(self):
        pygame.quit()

    def competir(self):
        
        gameOver = False

        while not gameOver:
            # comprobación eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True

            for activeRunner in self.runners:
                activeRunner.avanzar()
                if activeRunner.position[0] >= self.__finishLine:
                    print(f"{activeRunner.name} ha ganado!")
                    gameOver = True
        
            self.__screen.blit(self.background, (0, 0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome,runner.position)
            
            pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()


if __name__ == "__main__":
    pygame.init()
    juego = Game()
    juego.competir()