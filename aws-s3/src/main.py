from src.upload_service import upload_file

if __name__ == "__main__":
    url = upload_file("uploads/exemplo.txt", "arquivos/exemplo.txt")
    print("Arquivo enviado com sucesso!")
    print("URL:", url)