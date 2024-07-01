import cv2 as cv2
import time
import numpy as np
from datetime import datetime
import utils
import HandTracking as ht
import gestureControl as gc

# Variáveis para controle do movimento do mouse
controlMovement = gc.GestureControl()
WIDTH_SCREEN, HIGHT_SCREEN = (controlMovement.sizeScreen)
wCam, hCam = 640, 480
FRAME_RATE = 150

# Variáveis para detecção de gestos
TWO_FINGERSs = [0, 1, 1, 0, 0]
TWO_FINGERS = [1, 1, 1, 0, 0]
THREE_FINGERS = [1, 1, 1, 1, 0]
FOUR_FINGERS = [1, 1, 1, 1, 1]
CLOSED_HAND = [0, 0, 0, 0, 0]
INDEX_FINGER = 8

# Caminho para salvar screenshots
PATH = utils.create_path()


def virtual_mouse():
    # Inicializa o tempo anterior para cálculo do FPS
    pTime = 0

    # Configura a câmera
    capCam = cv2.VideoCapture(0)
    capCam.set(3, wCam)
    capCam.set(4, hCam)

    # Configura o rastreamento de mãos usando o Mediapipe do Google
    handTracking = ht.HandDetector(detectionCon=0.6)
    lastPositionY = 0

    while True:
        # Lê a imagem da câmera
        (success, img) = capCam.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Espelha a imagem e desenha um retângulo nela
        img = cv2.flip(img, 1)
        cv2.rectangle(img, (FRAME_RATE, FRAME_RATE),
                      (wCam - FRAME_RATE, hCam - FRAME_RATE), (255, 0, 255), 2)

        # Encontra as mãos na imagem e desenha as landmarks
        img = handTracking.findHands(img, draw=True)
        imgList, handBox = handTracking.findPositionFingers(img, draw=True)

        up = False
        down = False
        if (len(imgList) != 0):
            # Calcula a área da mão e desenha na imagem
            handArea = utils.get_area_box(handBox)
            cv2.putText(img, f'Hand Area: {
                        handArea}', (100, 440),
                        cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 0), 1)

            # Calcula o centro da mão e verifica quais dedos estão levantados
            xCenter, yCenter = utils.get_center_rectangle(handBox)
            fingerUp = handTracking.fingersUp()

            # Verifica se a mão está se movendo para cima ou para baixo
            if (lastPositionY > yCenter):
                up = True
                lastPositionY = yCenter
            if (lastPositionY < yCenter):
                down = True
                lastPositionY = yCenter

            # Se três dedos estão levantados, rola a tela para cima ou para
            # baixo
            if (fingerUp == THREE_FINGERS):
                if (up):
                    controlMovement.scroll_wheel(5, 1)
                    up = False
                elif (down):
                    controlMovement.scroll_wheel(5, -1)
                    down = False

            # Se a mão está fechada, tira uma screenshot
            if (fingerUp == CLOSED_HAND):
                now = datetime.now()
                current_time = now.strftime(
                    "%H-%M-%S-%f")[:-3]  # Format: HH-MM-SS-fff
                current_path = PATH + f'image_{current_time}.png'
                controlMovement.take_screenshot(current_path)
                print('Screenshot saved successfully')

            # Se dois dedos estão levantados, move o mouse para a posição do
            # dedo indicador
            if (fingerUp == TWO_FINGERS or fingerUp == TWO_FINGERSs):
                x, y = imgList[INDEX_FINGER][1], imgList[INDEX_FINGER][2]
                x3 = np.interp(
                    x, (FRAME_RATE, wCam - FRAME_RATE), (0, WIDTH_SCREEN))
                y3 = np.interp(
                    y, (FRAME_RATE, hCam - FRAME_RATE), (0, HIGHT_SCREEN))
                controlMovement.mouse_move(x3, y3)
                if (fingerUp[0] == 1):
                    controlMovement.mouse_click(x3, y3)

        # Calcula e desenha o FPS na imagem
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 2)
        cv2.imshow("Gesture Recognition", img)

        # Se a tecla 'q' for pressionada, encerra o programa
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    virtual_mouse()
