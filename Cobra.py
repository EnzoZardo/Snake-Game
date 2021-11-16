#Jogo da Cobrinha, uma tentativa
import os
import pygame
import random
from CobraClass import *

PATH = os.path.dirname(os.path.abspath(__file__))
def get_path(*slices):
	return os.path.join(PATH, *slices)

def main(Flux, Paus, Inicia):
	pygame.init()

	#Ajusta a cor PRETA pra Tela
	PRETO = (0, 0, 0)
	ROXO = (155, 0, 155)

	#Ajusta a Tela
	pygame.display.set_caption("Cobrinha")
	TamanhoDaTela = (1000, 800)
	Tela = pygame.display.set_mode(TamanhoDaTela)
	Tela.fill(PRETO)

	#Escreve
	cont = 0

	#Pega classes
	Snake = Cobra()
	Filhin = Filho()
	Point = NewQuadrado()


	#Ajusta o Tempo
	clock = pygame.time.Clock()

	all_sprites = pygame.sprite.Group()
	all_sprites.add(Snake)
	all_sprites.add(Point)


	#Fluxo
	Fluxo = Flux
	Pause = Paus
	Inicial = Inicia
	
	while Inicial:
		Teclas = pygame.key.get_pressed()
		
		TempoPassando = clock.tick(100)
		
		txt = 'Snake'
		pygame.font.init()
		Fonte = pygame.font.get_default_font()
		FonteSys = pygame.font.SysFont(Fonte, 100)
		TextoTela = FonteSys.render(txt, 1, (255,255,255))
		Tela.blit(TextoTela, (400, 200))	
		
		pygame.draw.rect(Tela, (100, 100, 150), (295, 395, 400, 45))
		txtI = 'Aperte aqui para iniciar'
		pygame.font.init()
		Fonte = pygame.font.get_default_font()
		FonteSys = pygame.font.SysFont(Fonte, 50)
		TextoTelaI = FonteSys.render(txtI, 1, (255,255,255))
		Tela.blit(TextoTelaI, (300, 400))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				
		
		if pygame.mouse.get_pressed()[0]:
			if pygame.mouse.get_pos()[0] >= 295 and pygame.mouse.get_pos()[0] <= 695 and pygame.mouse.get_pos()[1] >= 395 and pygame.mouse.get_pos()[1] <= 440:
				Inicial = False
				Fluxo = True
		
		elif pygame.mouse.get_pos()[0] >= 295 and pygame.mouse.get_pos()[0] <= 695 and pygame.mouse.get_pos()[1] >= 395 and pygame.mouse.get_pos()[1] <= 440:
			pygame.draw.rect(Tela, (255, 50, 50), (295, 395, 400, 45))
			pygame.draw.rect(Tela, (0, 0, 0), (295, 440, 400, 2))
			txtI = 'Aperte aqui para iniciar'
			pygame.font.init()
			Fonte = pygame.font.get_default_font()
			FonteSys = pygame.font.SysFont(Fonte, 50)
			TextoTelaI = FonteSys.render(txtI, 1, (255,255,255))
			Tela.blit(TextoTelaI, (300, 400))
				
		pygame.display.flip()
		Tela.fill(ROXO)

			
	while Fluxo:
		
		#Aqui fica todo o rodapé
		pygame.draw.rect(Tela, (80, 80, 80), (0, 760, 1000, 40))
		txt = str(cont)
		txtI = 'Aperte ESC para pausar'
		pygame.font.init()
		Fonte = pygame.font.get_default_font()
		FonteSys = pygame.font.SysFont(Fonte, 30)
		TextoTela = FonteSys.render(txt, 1, (255,255,255)) 
		TextoTelaII = FonteSys.render(txtI, 1, (255,255,255)) 
		Tela.blit(TextoTela, (960, 770))
		Tela.blit(TextoTelaII, (25, 770))
		
		#Variável que detecta teclas
		Teclas = pygame.key.get_pressed()
		
		TempoPassando = clock.tick(10)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				Fluxo = False
			
		
		if Snake.rect.colliderect(Point.rect):
			Point.rect.centerx = random.randint(0, 987)
			Point.rect.centery = random.randint(0, 747)
			cont += 1
			Filhin = Filho()
			Filhin.rect.centerx = Snake.rect.centerx
			Filhin.rect.centery = Snake.rect.centery
			Snake.filhos.append(Filhin)
			Lis = Snake.filhos
			all_sprites.add(Filhin)		

		elif Teclas[pygame.K_ESCAPE]:
			Pause = True
		
		elif cont >= 1:	
			for i in range(0 , len(Lis)):
				if Snake.rect.colliderect(Lis[i]):
					Bah = True
					while Bah:
						
						TempoPassando = clock.tick(10)
						
						Teclas = pygame.key.get_pressed()
						
						Will_Smith = pygame.image.load(get_path('img/William.png'))
						
						
						
						txt = 'Você Perdeu'
						pygame.font.init()
						Fonte = pygame.font.get_default_font()
						FonteSys = pygame.font.SysFont(Fonte, 100)
						TextoTela = FonteSys.render(txt, 1, (255,255,255))
						Tela.blit(TextoTela, (300, 300))	
						
						pygame.draw.rect(Tela, (150,150,150), (295, 395, 290, 30))
						txtI = 'Aperte aqui para jogar novamente'
						pygame.font.init()
						Fonte = pygame.font.get_default_font()
						FonteSys = pygame.font.SysFont(Fonte,25)
						TextoTelaI = FonteSys.render(txtI, 1, (255,255,255))
						Tela.blit(TextoTelaI, (300, 400))	
						
						pygame.draw.rect(Tela, (150,150,150), (295, 495, 290, 30))
						txtII = '           Aperte aqui para sair'
						pygame.font.init()
						Fonte = pygame.font.get_default_font()
						FonteSys = pygame.font.SysFont(Fonte,25)
						TextoTelaII = FonteSys.render(txtII, 1, (255,255,255))
						Tela.blit(TextoTelaII, (300, 500))	
						
						
						
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								pygame.quit()
							
						if pygame.mouse.get_pressed()[0]:	
							if pygame.mouse.get_pos()[0] >= 295 and pygame.mouse.get_pos()[0] <= (295+290) and pygame.mouse.get_pos()[1] >= 395 and pygame.mouse.get_pos()[1] <= (395+30):
								main(True, False, False)
								
							
							elif pygame.mouse.get_pos()[0] >= 295 and pygame.mouse.get_pos()[0] <= (295+290) and pygame.mouse.get_pos()[1] >= 495 and pygame.mouse.get_pos()[1] <= (495+30):
								quit()
								
						elif pygame.mouse.get_pos()[0] >= 295 and pygame.mouse.get_pos()[0] <= (295+290) and pygame.mouse.get_pos()[1] >= 395 and pygame.mouse.get_pos()[1] <= (395+30):
							pygame.draw.rect(Tela, (255,255,255), (295, 395, 290, 30))
							pygame.draw.rect(Tela, (150, 150, 255), (295, (395+30), (290), 2))
							txtI = 'Aperte aqui para jogar novamente'
							pygame.font.init()
							Fonte = pygame.font.get_default_font()
							FonteSys = pygame.font.SysFont(Fonte, 25)
							TextoTelaI = FonteSys.render(txtI, 1, (0,0,0))
							Tela.blit(TextoTelaI, (300, 400))
						
						elif pygame.mouse.get_pos()[0] >= 295 and pygame.mouse.get_pos()[0] <= (295+290) and pygame.mouse.get_pos()[1] >= 495 and pygame.mouse.get_pos()[1] <= (495+30):	
							pygame.draw.rect(Tela, (255,255,255), (295, 495, 290, 30))
							pygame.draw.rect(Tela, (150, 150, 255), (295, (495+30), (290), 2))
							txtII = '           Aperte aqui para sair'
							pygame.font.init()
							Fonte = pygame.font.get_default_font()
							FonteSys = pygame.font.SysFont(Fonte,25)
							TextoTelaII = FonteSys.render(txtII, 1, (0, 0, 0))
							Tela.blit(TextoTelaII, (300, 500))	
						
						
						
						pygame.display.flip()
						Tela.fill(PRETO)
						Tela.blit(TextoTela, (780, 980))
						Tela.blit(Will_Smith, (30, 30))
						
			
		while Pause:
			pygame.draw.rect(Tela, (150,150,150), (395, 395, 233, 30))
			txt = 'Você está pausado'
			txtii =  'Aperte aqui para voltar'
			pygame.font.init()
			Fonte = pygame.font.get_default_font()
			FonteSys = pygame.font.SysFont(Fonte, 100)
			TextoTela = FonteSys.render(txt, 1, (255,255,255)) 
			Tela.blit(TextoTela, (200, 300))
			FonteSys = pygame.font.SysFont(Fonte, 30)
			TextoTelaI = FonteSys.render(txtii, 1, (255,255,255))
			Tela.blit(TextoTelaI, (400, 400))
		
			Teclas = pygame.key.get_pressed()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Fluxo = False
					Pause = False
					
			if pygame.mouse.get_pressed()[0]:
				if pygame.mouse.get_pos()[0] >= 395 and pygame.mouse.get_pos()[0] <= (395+233) and pygame.mouse.get_pos()[1] >= 395 and pygame.mouse.get_pos()[1] <= (395+30):
					Snake.Dir = False
					Snake.Esq = False
					Snake.Sob = False
					Snake.Des = False
					Fluxo = True
					Pause = False
				
			elif pygame.mouse.get_pos()[0] >= 395 and pygame.mouse.get_pos()[0] <= (395+233) and pygame.mouse.get_pos()[1] >= 395 and pygame.mouse.get_pos()[1] <= (395+30):
				pygame.draw.rect(Tela, (255,255,255), (395, 395, 233, 30))
				pygame.draw.rect(Tela, (150, 150, 255), (395, (395+30), (233), 2))
				TextoTelaI = FonteSys.render(txtii, 1, (0,0,0))
				Tela.blit(TextoTelaI, (400, 400))
				
		
			pygame.display.flip()
			Tela.fill(PRETO)
			Tela.blit(TextoTela, (780, 980))


		
		all_sprites.update()
		all_sprites.draw(Tela)
				
		
		pygame.display.flip()
		Tela.fill(PRETO)
		Tela.blit(TextoTela, (780, 980))

	pygame.quit()

main(False, False, True)
