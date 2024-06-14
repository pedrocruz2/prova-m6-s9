Esse Readme será divido em duas seções, uma primeira de instruções para rodar o projeto e outra para responder as perguntas técnicas.



## INSTRUÇÕES PARA RODAR

- Clone o este repositório utilizando o comando git clone https:
- Baixe os dados de treinamento disponíveis ![neste link](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml)
- Faça o upload do arquivo xml na diretória raiz do projeto
- Crie um ambiente virtual utilizando o comando ```python -m venv venv``` (Windows) ou ```python3 -m venv venv``` (Linux ou MacOS)
- Acione esse ambiente virtual utilizando o comando ```./venv/Scripts/activate``` (Windows) ou ```source ./venv/bin/activate ``` (Linux ou MacOS)
- rode o comando ```pip install -r requirements.txt``` para instalar todas as dependências necessárias
- rode o comando ```python ./main.py``` (Windows) ou ```python3 ./main.py``` (Linux ou MacOS)

Será gerado um arquivo de video chamado new_video.mp4 que terá as deteccoes funcionando normalmente.



