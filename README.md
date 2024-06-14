Esse Readme será divido em duas seções, uma primeira de instruções para rodar o projeto e outra para responder as perguntas técnicas.



## INSTRUÇÕES PARA RODAR

- Clone o este repositório utilizando o comando git clone https:
- Baixe os dados de treinamento disponíveis ![neste link](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml)
- Faça o upload do arquivo xml na diretória raiz do projeto
- Crie um ambiente virtual utilizando o comando ```python -m venv venv``` (Windows) ou ```python3 -m venv venv``` (Linux ou MacOS)
- Acione esse ambiente virtual utilizando o comando ```./venv/Scripts/activate``` (Windows) ou ```source ./venv/bin/activate ``` (Linux ou MacOS)
- rode o comando ```pip install -r requirements.txt``` para instalar todas as dependências necessárias
- rode o comando ```mkdir new_video``` para criar a pasta onde serão colocados os frames do novo vídeo 
- rode o comando ```python ./main.py``` (Windows) ou ```python3 ./main.py``` (Linux ou MacOS)

Será gerado um arquivo de video chamado new_video.mp4 que terá as deteccoes funcionando normalmente.



## PERGUNTAS TÉCNICAS

- (2.1) O método escolhido foi o haar cascade, que funciona da seguinte forma: Primeiramente um algoritmo é treinando para saber reconhecer o objeto que nós queremos. Nesse caso são utilizadas várias imagens com faces e várias imagens sem faces, cada uma com uma classificação de positiva (tem face) ou negativa (não tem face).  Com base nisso ele passa vários filtros retangulares pelas imagens de treinamento e vê as regiões em comum das imagens positivas que não aparecem nas imagens negativas, detectando essas regiões pela intensidade de pixels em cada uma das regiões. Com o modelo treinado, esses mesmos filtros retangulares são passados pela imagem que deve ser detectada e eles "Procuram" esses padrões de intensidade de pixels nas imagens e marcam o retângulo na área onde o padrão foi encontrado (face). Um bom exemplo de como funciona é que os olhos de rostos humanos costumam ter uma discrepância muito grande de intensidade de cor, assim sendo um padrão facilmente reconhecido pelo haar cascade.

- (2.2)

- (2.5) Vinicius Jr

