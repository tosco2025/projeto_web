# Dockerfile para aplicação Django com SQLite3
FROM python:3.11-slim


# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os requisitos e instala as dependências
COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && pip install -r /app/requirements.txt


# Expõe a porta da aplicação
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
