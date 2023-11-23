import pygame,random

# klasser
class Matbit:
    def __init__(self):
        self.bilde = pygame.image.load("bilder/beer.png").convert_alpha()
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = random.randint(0,BREDDE)
        self.ramme.centery = random.randint(0,HOYDE)

    def tegn(self,vindu):
        vindu.blit(self.bilde,self.ramme)

class Celle:
    def __init__(self,navn:str,radius:int,bildesti:str):
        self.navn = navn 
        self.radius = radius
        self.bilde = pygame.image.load(bildesti)
        self.ramme = self.bilde.get_rect()

    def beveg(self):
        pass

    def spis(self):
        pass

    def tegn(self,vindu):
        vindu.blit(self.bilde,self.ramme)
        

    



#1.oppsett
pygame.init()
BREDDE=600
HOYDE=600
FPS=60
vindu= pygame.display.set_mode((BREDDE, HOYDE)) 
klokke = pygame.time.Clock()

Stag = Celle("Stag",50,"bilder/stag.jpeg")
Jets = Celle("Jets",25,"bilder/jets.jpeg")  
matbit1=Matbit()
matbit1 = Matbit()
matbit2=Matbit()

while True:
    # 2. håndtere input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    # 3. oppdatere spill
    # 4. tegn
    vindu.fill("white")
    Stag.tegn(vindu)
    Jets.tegn(vindu)
    matbit1.tegn(vindu)
    matbit2.tegn(vindu)

    pygame.display.flip()
    klokke.tick(FPS)




