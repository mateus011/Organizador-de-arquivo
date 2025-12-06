import os  #biblioteca que permite interação com o sistema operacional
#mostrar os arquivos na pasta 
import shutil


# for arquivo in os.listdir('C:\\Users\\adm\\Downloads'):# lista a pasta dwoload
#     print(arquivo)
pasta_base = "C:\\Users\\adm\\Downloads"  #pasta que sera organizada 
#crianção de pastas

tiposPastas = ['pdf','jpg','word'] # quantidade e nomes das pastas

for nome in tiposPastas:
    pasta = os.path.join(pasta_base,nome) #junção de arquivos e pastas
    os.makedirs(pasta, exist_ok=True) #comando de criação de pasta usando "os"(local onde sera criado a pasta)
    print(f'pasta {nome} criada com sucesso !!')


#pasta que sera organizada
#crianção de regras
#tipos de arquivos organizados
regras = {
    "pdf":[".pdf"],
    "jpg": [".jpg",".png"],
    "word": [".docx", ".doc"]
}

#verificar arquivos dentro da pasta 
for arquivo in os.listdir(pasta_base):
    caminho = os.path.join(pasta_base, arquivo) 
    if os.path.isdir(caminho):  #verifica se tem uma pasta dentro do caminho 
        continue    #faz o loop continuar
    

    nomeTupla,  ext = os.path.splitext(arquivo) # separa o nome da extenção [nome][.png]
    #percorrer as regras
    for pastaRegras, extensoes in regras.items(): # percorre dicionario
        if ext.lower() in extensoes:
            destino = os.path.join(pasta_base,pastaRegras)
            destino_arquivo = os.path.join(destino, arquivo)
            if not os.path.exists(destino_arquivo):
              shutil.move(caminho,destino_arquivo)
              print(f"arquivos movidos: {arquivo} para {pastaRegras}")
            else:
                print(f"arquivo {arquivo} ja existe {pastaRegras}")
                break
            
           
           
            

