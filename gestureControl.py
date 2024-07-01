import pyautogui as pygui


class GestureControl():
    def __init__(self) -> None:
        # Inicializa a classe GestureControl, obtendo o tamanho da tela
        self.sizeScreen = pygui.size()

    def mouse_move(self, posx, posy):
        # Move o cursor do mouse para as coordenadas (posx, posy)
        pygui.moveTo(posx, posy)

    def scroll_wheel(self, num_times, upOrDown):
        # Rola a roda do mouse num_times vezes na direção upOrDown
        pygui.scroll(num_times * upOrDown)

    def mouse_click(self, posx, posy):
        # Clica no ponto (posx, posy) na tela
        pygui.click()

    def take_screenshot(self, path):
        # Tira uma captura de tela e salva no caminho especificado por 'path'
        pygui.screenshot(path)
