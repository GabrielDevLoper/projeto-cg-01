## Projeto Computação Gráfica Parte 01.

- 1: Criar tela Branca
- 2: Detectar cliques com o botão esquerdo do mouse e desenhar um ponto preto de tamanho 50 no local que foi clicado na tela.
- 3: Ao pressionar o botão direito, limpar a tela.

---

## Novas Funcionalidades adicionadas

- 1: Pontos redondos
- 2: Alteração na cor dos pontos geradas aleatoriamente.

---

## Passo a passo montagem do ambiente no windows

- 1: Instalação do python: https://www.python.org/downloads/
- 2: Instalação das bibliotecas: 
```py 
pip install PyOpenGL glfw
```
- 3: Executar arquivo da pasta: 
```py
python screen-white.py
```

---

#### Não conseguir instalar a biblioteca PyOpenGL_accelerate foi apresentado o seguinte erro: 
``Failed to build PyOpenGL_accelerate ERROR: Could not build wheels for PyOpenGL_accelerate, which is required to install pyproject.toml-based projects``
#### Porém o código executou normalmente sem a lib PyOpenGL_accelerate