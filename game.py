import pygame

class runner():
    pass

class Game():

    # cooredores []

    def __init__(self):

        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de tortugas")
        self.background = pygame.image.load("./pista.png")

        self.runner = pygame.image.load("./runner.png")

    def competir(self):
        
        pygame.init()
        x = 0
        hayGanador = False
        
        while not hayGanador:
            # comprobación eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # refrescar/renderizar pantalla
            self.__screen.blit(self.background, (0, 0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()

            x += 3
            if x >= 250:
                hayGanador = True
        
        pygame.quit()

if __name__ == "__main__":
    juego = Game()
    juego.competir()