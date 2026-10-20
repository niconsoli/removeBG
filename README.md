## RemoveBG

Este projeto simples remove o fundo de imagens automaticamente utilizando Python!
Não é garantido que funcione cem por cento das vezes, e a detecção do fundo pode depender da imagem utilizada. Entretanto, este é um exercício utilizando as bibliotecas rembg e PIL do Python para realizar a leitura de uma imagem e uma criação desta, com o fundo removido!

## Tecnologias
- Python 3.13
> Esta versão específica é exigida, uma vez que o rembg ainda não recebeu suporte completo compatível com as versões mais recentes do Python
- Bibliotecas rembg e PIL

## Como executar
- Instale o Python 3.13 em sua máquina e adicione-o ao Path no processo de instalação.
- Verifique se a instalação do mesmo foi bem sucedida digitando no terminal `py -3.13 --version`.
- Clone o repositório com `git clone https://github.com/niconsoli/removebg.git` e acesse a pasta do repositório clonado.
- Nesta pasta, insira a sua foto *necessariamente com a extensão de JPG* com o nome exato de `foto.jpg`.
- Utilize os comandos: `python -m pip install --upgrade pip`, `python -m pip install rembg` e `pip install "rembg[cpu]" `
- Em seguida, nesta pasta, execute `python.exe removebg.py`
- Sua foto estará salva sob o nome `removeBG.png`!