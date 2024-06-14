Esse Readme será divido em duas seções, uma primeira de instruções para rodar o projeto e outra para responder as perguntas técnicas.



### INSTRUÇÕES PARA RODAR

- Clone o este repositório utilizando o comando git clone https:
- Baixe os dados de treinamento disponíveis ![neste link](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_alt.xml)
- Faça o upload do arquivo xml na diretória raiz do projeto
- Crie um ambiente virtual utilizando o comando ```python -m venv venv``` (Windows) ou ```python3 -m venv venv``` (Linux ou MacOS)
- Acione esse ambiente virtual utilizando o comando ```./venv/Scripts/activate``` (Windows) ou ```source ./venv/bin/activate ``` (Linux ou MacOS)
- rode o comando ```pip install -r requirements.txt``` para instalar todas as dependências necessárias
- rode o comando ```mkdir new_video``` para criar a pasta onde serão colocados os frames do novo vídeo 
- rode o comando ```python ./main.py``` (Windows) ou ```python3 ./main.py``` (Linux ou MacOS)

Será gerado um arquivo de video chamado new_video.mp4 que terá as deteccoes funcionando normalmente.



### PERGUNTAS TÉCNICAS

## (2.1)

O método escolhido foi o haar cascade, que funciona da seguinte forma: Primeiramente um algoritmo é treinando para saber reconhecer o objeto que nós queremos. Nesse caso são utilizadas várias imagens com faces e várias imagens sem faces, cada uma com uma classificação de positiva (tem face) ou negativa (não tem face).  Com base nisso ele passa vários filtros retangulares pelas imagens de treinamento e vê as regiões em comum das imagens positivas que não aparecem nas imagens negativas, detectando essas regiões pela intensidade de pixels em cada uma das regiões. Com o modelo treinado, esses mesmos filtros retangulares são passados pela imagem que deve ser detectada e eles "Procuram" esses padrões de intensidade de pixels nas imagens e marcam o retângulo na área onde o padrão foi encontrado (face). Um bom exemplo de como funciona é que os olhos de rostos humanos costumam ter uma discrepância muito grande de intensidade de cor, assim sendo um padrão facilmente reconhecido pelo haar cascade.

## (2.2)

  # Primeiro lugar: Haar Cascade
  O Haar cascade foi escolhido no primeiro lugar pelos seguintes motivos. Desempenha muito bem o papel de deteccão de objetos, é extremamente simples de se implementar e é muito rápido, então pode facilmente ser implementado em transmissões ao vivo.
  # Segundo Lugar: CNN e Filtros de Correlação cruzada (empate!)
  Primeiro é necessário explicar o porque do empate, no caso escolhi colocar as duas no mesmo tier pois são operações extremamente similares, onde a única diferença se dá que a CNN inverte o kernel de convolução em relação ao kernel utilizado na correlação cruzada.
  
O segundo lugar foi cedido pois apesar de conseguir desempenhar a tarefa tão bem quanto o haar cascade, são consideravelmente mais difíceis de se implementar e de manter.
# Terceiro Lugar: NN Linear
A NN Linear foi escolhida no terceiro lugar pois a idéia de reconhecer objetos iguais em posições diferentes é bastante problemática para ela, oque pode deixa-lá muito suscetível a overfitting, como por exemplo reconhecer objetos apenas em um lugar específico.
  
## (2.3)
# Primeiro lugar: Correlação Cruzada / CNN (Empate denovo)
CNNs desempenharão ridiculamente melhor do que o Haar cascade quando estamos tratando de diferenças entre objetos (Que as CNNs conseguem reconhecer com muito mais facilidade), novamente eu coloquei como empate pois a única diferença é a da inversão do kernel citada anteriormente, que não afeta nesse quesito.
# Segundo Lugar: Haar Cascade
O Haar cascade funciona muito bem quando estamos falando de detecção de um padrão de objeto, como uma face, porém distinguir diferenças entre esses mesmos objetos (face feliz, face triste) seria mais problemático, pois não necessariamente a intensidade de pixels será diferente para um olho / boca feliz ou triste.
# Quarto Lugar: NN Linear
Como a NN Linear já tem problemas para passar do primeiro passo (Reconhecer faces) seria mais problemático ainda realizar operações de analise de emoções com ela.
## (2.4)
Sim! CNNs Tri-Dimensionais tem conseguem realizar esse tipo de análise. Utilizando Kernels Tri-dimensionais é possivel analisar informações em tempos diferentes, não se limitando a uma análise que acontece apenas a cada instante ou frame do vídeo, e sim uma análise que consegue considerar padrões que aconteceram em instantes ou frames anteriores ao atual.
## (2.5) vinicios Junor           (vinicius jr)


