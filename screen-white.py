import glfw
from OpenGL.GL import *
import random

def mouse_button_callback(window, button, action, mods):
    global points

    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        # Obtendo coordenadas do cursor do mouse
        x, y = glfw.get_cursor_pos(window)
        width, height = glfw.get_window_size(window)

        # Convertendo para coordenadas do sistema de coordenadas OpenGL
        x = x / width * 2 - 1
        y = 1 - y / height * 2

        # Gerando cor aleatória
        color = (random.random(), random.random(), random.random())

        # Adicionar ponto e cor às coordenadas
        points.append((x, y, color))

    elif button == glfw.MOUSE_BUTTON_RIGHT and action == glfw.PRESS:
        # Limpar pontos com o clique direito do mouse.
        points.clear()

def draw_points():
    global points
    glPointSize(50) # Definindo o tamanho do ponto
    glBegin(GL_POINTS)

    for x, y, color in points:
        glColor3f(*color)  # Definindo cor aleatória para cada botão adicionado
        glVertex2f(x, y)

    glEnd()

def main():
    global points
    points = []

    # Inicializar glfw
    if not glfw.init():
        return

    # Criando janela e definindo a resolução da Janela
    window = glfw.create_window(800, 600, "Marcar Pontos - OpenGL", None, None)
    if not window:
        glfw.terminate()
        return

    # Definindo o contexto atual
    glfw.make_context_current(window)

    # Habilitar mistura (blending), para que os pontos fiquem arredondados
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Habilitar suavizado de pontos (point smoothing)
    glEnable(GL_POINT_SMOOTH)
    glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)

    # Definir função de callback do mouse
    glfw.set_mouse_button_callback(window, mouse_button_callback)

    # Loop principal
    while not glfw.window_should_close(window):
        # Limpar a tela com a cor branca
        glClearColor(1.0, 1.0, 1.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Desenhar pontos
        draw_points()

        # Trocar buffers
        glfw.swap_buffers(window)
        glfw.poll_events()

    # Terminar GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
