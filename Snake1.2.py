# Creación de la pantalla:

import pygame # Traemos la librería para juegos
import random # Traemos la librería para generar números aleatorios.

ancho_pantalla = 800 
largo_pantalla = 600
pygame.init() # Inicializamos los módulos (objetos y funciones)
pantalla = pygame.display.set_mode((ancho_pantalla,largo_pantalla)) #Crea una superficie y la guardamos en una variable.
pygame.display.update() #Actualiza la pantalla
pygame.display.set_caption("Snake")  #Le da un título a la pantalla.

#Declaración de los colores que vamos a usar:
azul=(0, 191, 255)
rojo=(255, 0, 0)
negro=(0, 0, 0)                      # RGB= Red, green, black.
blanco=(225, 225, 225)

#Declaración del reloj
clock = pygame.time.Clock()

#Declaración de la variable que contiene la velocidad de la serpiente.
velocidad_serpiente = 60 #60 fotogramas por segundo.
#Tamaño de la serpiente:
snake_size = 10
#Creación de la lista que contiene el cuerpo de la serpiente.
snake_List= []
#Definición del tipo de letra para los mensajes y de la función que muestra los mensajes.
fuente_letra = pygame.font.SysFont(None, 30)
def mostrar_mensaje(texto, color):
    mensaje = fuente_letra.render(texto,True, color)#Crea el mensaje final a mostrar.
    pantalla.blit(mensaje, [ancho_pantalla/5, largo_pantalla/3]) #Imprime el mensaje en la pantalla rápidamente.
#A continuación se crea un bucle que sólo se rompe cuando el jugador le haya dado a la X de salir.
#El bucle está vigilando constantemente qué es lo que hace el jugador.

def crea_snake(snake_size, snake_List):
    for x in snake_List:
        pygame.draw.rect(pantalla, negro, [x[0], x[1], snake_size, snake_size])


def gameLoop():
    #Declaración de las variables que  tienen la posición de la serpiente:
    x = 100
    y = 100

    #Declaración de las variables que van a contener los incrementos en las posiciones.
    x1=0
    y1=0
    #Declaración de las variables aleatorias para generar la comida.
    comidaX = round(random.randrange(0, ancho_pantalla - snake_size) / 10.0) * 10.0
    comidaY = round(random.randrange(0, largo_pantalla - snake_size) / 10.0) * 10.0
    
    game_over = False #Crea un booleano, será True cuando haya perdido.
    game_close = False #Es True cuando el usuario decide salir del juego presionando q.


    ## Bucle para ejecutar el juego.
    while not game_over:
        while game_close == True:
            pantalla.fill(azul)
            mostrar_mensaje("You Lost! Press C to Play Again or press Q to quit.", blanco)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        game_close == False
                        gameLoop()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()   
        for event in pygame.event.get():  #Va a recorrer toda la lista de los eventos.
            if event.type==pygame.QUIT:  # Si hay un evento que sea presionar la X, entonces game over.
                game_over = True
            if event.type==pygame.KEYDOWN: # Si hay algún evento de presionar teclas, entra.
                if event.key==pygame.K_LEFT: 
                    x1 = -snake_size
                    y1 = 0
                elif event.key==pygame.K_RIGHT: # Cuando presiona la tecla derecha, aumenta sus coordenadas en x. NO aumenta nada en y.
                    x1 = snake_size
                    y1 = 0
                elif event.key==pygame.K_UP:
                    y1 = -snake_size
                    x1 = 0
                elif event.key==pygame.K_DOWN:
                    y1 = snake_size
                    x1 = 0
        if x>= ancho_pantalla or x <= 0 or y>=largo_pantalla or y<=0:
            game_close=True

        x = x + x1
        y = y + y1
        pantalla.fill(blanco)
        pygame.draw.rect(pantalla, azul, [x, y, snake_size, snake_size]) #En la tupla [x, y, ancho, alto]
        pygame.draw.rect(pantalla, rojo, [comidaX, comidaY, snake_size, snake_size] ) #Dibuja la comida

        # Condicional para mostrar Yummy cada vez que come.
        if x == comidaX and y == comidaY:
            comidaX = round(random.randrange(0, ancho_pantalla - snake_size) / 10.0) * 10.0
            comidaY = round(random.randrange(0, largo_pantalla - snake_size) / 10.0) * 10.0
       
        pygame.display.update() #Actualiza la pantalla para mostrar el cuadrado

        clock.tick(velocidad_serpiente) #Vuelve más lento el bucle, 35 veces por segundo.

    pygame.display.update()
    pygame.quit()

gameLoop()

