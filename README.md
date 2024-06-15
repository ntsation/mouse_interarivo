# Reconhecimento e controle de gestos manuais

Este projeto Python permite o controle baseado em gestos de um mouse virtual usando uma webcam. Ele utiliza técnicas de visão computacional para detectar gestos manuais em tempo real e mapeia esses gestos para ações como movimento do mouse, clique, rolagem e captura de tela.

## Requisitos

Para executar este projeto, certifique-se de ter as seguintes dependências instaladas, utilize o requeriments.txt
```
pip install -r requeriments.txt
```

## Arquivos

- **main.py**

    O script principal que interage com o feed da webcam, realiza rastreamento manual usando HandTracking.py e controla as ações do mouse por meio do gestureControl.py.

- **HandTracking.py**

    Contém a classe HandDetector, que usa a biblioteca mediapipe para detectar e rastrear pontos de referência manuais (pontos-chave) e gestos em vídeo ao vivo.

- **gestureControl.py**

    Implementa a classe GestureControl, aproveitando pyautogui para simular movimentos do mouse, cliques, rolagem e fazer capturas de tela com base em comandos de entrada.

- **utils.py**

    Funções utilitárias usadas em main.py para diversas tarefas, incluindo criação de caminho de arquivo, cálculos geométricos (área, centro) e medição de distância entre pontos.

## Uso

Rode **main.py**:

```
python main.py
```

### Siga as instruções na tela:

Posicione sua mão dentro da moldura da webcam.
Execute gestos definidos em main.py (por exemplo, três dedos para cima para rolar, mão fechada para fazer uma captura de tela).
### Saia do aplicativo:

**Pressione q no teclado para sair do programa.**

## Funcionalidades

- **Detecção de gestos**: reconhece gestos de mão predefinidos (por exemplo, três dedos para cima/para baixo, mão fechada).

- **Controle do mouse**: move o cursor do mouse e executa cliques com base nos gestos detectados.

- **Rolagem**: rola a roda do mouse para cima/para baixo com movimentos das mãos.

- **Captura de tela**: faz uma captura de tela quando um gesto de mão fechada é detectado.
