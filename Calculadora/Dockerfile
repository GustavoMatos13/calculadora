# Usando a imagem oficial do Python
FROM python:3.12.6-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências para o contêiner
COPY requirements.txt /app/

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . /app/

# Expõe a porta do Django
EXPOSE 8000

# Comando para rodar o Django (ajuste conforme sua configuração)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
