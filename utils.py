import math
import os

def create_path():
    # Obtém o caminho atual do diretório de trabalho
    currentPath = os.getcwd()
    screenshotPath = f'{currentPath}/screenshots/'
    # Verifica se o caminho da captura de tela já existe
    if(os.path.exists(screenshotPath)):
        return f'{currentPath}/screenshots/'
    else:
        # Cria um novo diretório para capturas de tela se não existir
        path = os.path.join(currentPath, 'screenshots/')
        os.mkdir(path)
        return path

def get_area_box(boxArea) -> float:
    # Calcula e retorna a área da caixa
    return (boxArea[2] - boxArea[0]) * (boxArea[3] - boxArea[1]) // 100

def get_center_rectangle(boxArea) -> tuple[int]:
    # Calcula e retorna o centro do retângulo
    xCenter = (boxArea[0] + boxArea[2]) / 2
    yCenter = (boxArea[1] + boxArea[3]) / 2
    return xCenter, yCenter

def get_distance(indexFingerTip, middleFingerTip) -> float:
    # Calcula e retorna a distância entre a ponta do dedo indicador e a ponta do dedo médio
    xIndex, yIndex = indexFingerTip[1], indexFingerTip[2]
    xMiddle, yMiddle = middleFingerTip[1], middleFingerTip[2]
    return(math.dist([xIndex,yIndex], [xMiddle, yMiddle]))