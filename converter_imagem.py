import cv2
import os

def transformar_desenho(arquivo, qtde_filtro):
    imagem = cv2.imread(f"imagens/{arquivo}")
    imagem_pb = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    imagem_invertida = cv2.bitwise_not(imagem_pb)
    imagem_blur = cv2.GaussianBlur(imagem_invertida, (qtde_filtro,qtde_filtro), 0)
    imagem_blur_invertida = cv2.bitwise_not(imagem_blur)
    imagem_desenho = cv2.divide(imagem_pb, imagem_blur_invertida, scale=256.0)

    cv2.imwrite(f"img_tratado/{arquivo}", imagem_desenho)

lista_arquivos = os.listdir("imagens")

for arquivo in lista_arquivos:
    transformar_desenho(arquivo, 55)