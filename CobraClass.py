#TentaCriarCobra

import pygame
import random

X = random.randint(0, 987)
Y = random.randint(0, 747)
 


class Cobra(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface((40, 40))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.centerx = 1000 / 2
		self.rect.centery = 800 - 60
		self.Dir = False
		self.Esq = False
		self.Sob = False
		self.Des = False
		self.filhos = []
		self.posiX = []
		self.posiY = []

	def update(self):
		Tec = pygame.key.get_pressed()

		
		if self.Dir and self.rect.centerx + 21 <= 1000:
			self.posiX.append(self.rect.centerx)
			self.posiY.append(self.rect.centery)
			for i in range(0, len(self.filhos)):
				self.filhos[i].rect.centerx = self.posiX[i-len(self.filhos)]
				self.filhos[i].rect.centery = self.posiY[i-len(self.filhos)]
				
			self.rect.centerx += 40
		elif self.Esq and self.rect.centerx - 21 > 0:
			self.posiX.append(self.rect.centerx)
			self.posiY.append(self.rect.centery)
			for i in range(0, len(self.filhos)):
				self.filhos[i].rect.centerx = self.posiX[i-len(self.filhos)]
				self.filhos[i].rect.centery = self.posiY[i-len(self.filhos)]
			
			self.rect.centerx -= 40 
		elif self.Sob and self.rect.centery > 40:
			self.posiX.append(self.rect.centerx)
			self.posiY.append(self.rect.centery)
			for i in range(0, len(self.filhos)):
				self.filhos[i].rect.centerx = self.posiX[i-len(self.filhos)]
				self.filhos[i].rect.centery = self.posiY[i-len(self.filhos)]
			
			self.rect.centery -= 40
		elif self.Des and self.rect.centery < 740:
			self.posiX.append(self.rect.centerx)
			self.posiY.append(self.rect.centery)
			for i in range(0, len(self.filhos)):
				self.filhos[i].rect.centerx = self.posiX[i-len(self.filhos)]
				self.filhos[i].rect.centery = self.posiY[i-len(self.filhos)]
			
			self.rect.centery += 40
		
		
		if Tec[pygame.K_RIGHT] or Tec[pygame.K_d] and self.rect.centerx + 21 <= 1000 and self.Esq == False:
			self.Esq = False
			self.Sob = False
			self.Des = False
			self.Dir = True 
		elif Tec[pygame.K_LEFT] or Tec[pygame.K_a] and self.rect.centerx - 21 > 0 and self.Dir == False:
			self.Esq = True
			self.Sob = False
			self.Des = False
			self.Dir = False
		elif Tec[pygame.K_UP] or Tec[pygame.K_w] and self.rect.bottom > 40 and self.Des == False:
			self.Esq = False
			self.Sob = True
			self.Des = False
			self.Dir = False
		elif Tec[pygame.K_DOWN] or Tec[pygame.K_s] and self.rect.bottom < 760 and self.Sob == False:
			self.Esq = False
			self.Sob = False
			self.Des = True
			self.Dir = False
			
			
class NewQuadrado(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface((25, 25))
		self.image.fill((100, 100, 100))
		self.rect = self.image.get_rect()
		self.rect.centerx = X
		self.rect.centery = Y
		
class Filho(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface((40, 40))
		self.image.fill((255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.centerx = self.rect.centerx
		self.rect.centery = self.rect.centery
		
		
		
