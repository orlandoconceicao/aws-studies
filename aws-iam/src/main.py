from s3_service import listar_arquivos

if __name__ == "__main__":
    bucket = "meu-bucket-exemplo"
    arquivos = listar_arquivos(bucket)
    
    print("Arquivos encontrados:")
    for arquivo in arquivos:
        print(arquivo)
