# Dockerfile para aplicação Django com SQLite3
FROM python:3.11-slim


# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os requisitos e instala as dependências
COPY ./docker/requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt


# Copia todo o projeto para o diretório de trabalho
COPY . /app

# Expõe a porta da aplicação
EXPOSE 8000

# Volume para persistir o banco de dados SQLite3
VOLUME ["/app/db.sqlite3"]

# Comando para iniciar a aplicação
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
