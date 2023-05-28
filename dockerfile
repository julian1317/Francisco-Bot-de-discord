# Utiliza la imagen base de Python
FROM python:3.8-slim-buster

# Establece el directorio de trabajo en /app
WORKDIR /Chat

# Copia los archivos del proyecto al directorio /app
COPY . .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecuta el bot
CMD [ "python", "Chat.py" ]
