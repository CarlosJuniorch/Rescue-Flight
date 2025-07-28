import pygame 
import random

largura = 1000
altura = 650
gravidade = 0.5    
impulso = -10
velocidade_cano = 3
distancia_cano = 200

class Pato():

    def __init__(self):
        self.x = 50
        self.y = altura // 2
        self.velocidade = 0
        self.raio = 20
   
    def pular(self):
        self.velocidade = impulso
   
    def atualizar (self):
        self.velocidade += gravidade
        self.y += self.velocidade
   
    def desenhar(self, tela):
        pygame.draw.circle(tela, (255, 0, 0), (int(self.x), int(self.y)), self.raio)

    def get_rect(self):
        return pygame.Rect(self.x - self.raio, self.y - self.raio, self.raio * 2, self.raio * 2)

class Rochas():
    

    def __init__(self, x):
        self.x = x
        self.largura = 100
        self.altura_topo = random.randint(100, 400)
        self.espaco = 180

         

    def atualizar(self):
        self.x -= velocidade_cano

    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 255, 255), (self.x, 0, self.largura, self.altura_topo))
        pygame.draw.rect(tela, (255, 255, 255), (self.x, self.altura_topo + self.espaco, self.largura, altura))


    def colidiu(self, pato: Pato):
        rect = pato.get_rect()
        topo = pygame.Rect(self.x, 0, self.largura, self.altura_topo)
        base = pygame.Rect(self.x, self.altura_topo + self.espaco, self.largura, altura)
        return rect.colliderect(topo) or rect.colliderect(base)

    def passou(self, pato: Pato):
        return self.x + self.largura < pato.x and not hasattr(self, 'pontuado')
