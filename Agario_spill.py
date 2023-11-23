import pygame

# klasser
class Matbit:
    def __init__(self):
        self.bilde = pygame.image.load("").convert_alpha()
        self.ramme = self.bilde.get.rect()
        self.ramme.centerx = 100
        self.ramme.centery = 200 

    def tegn(self,vindu):
        vindu.blit(self.bilde,self.ramme)

#1oppsett

pygame.init()
BREDDE=600
HOYDE=600
FPS=60
vindu= pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()

matbit1=Matbit()
matbit2=Matbit()

while True:
    # 2. håndtere input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # 3. oppdatere spill
    # 4. tegn
    vindu 
    matbit1.tegn(vindu)
    matbit2.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)




