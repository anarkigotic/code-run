# Usa la imagen base de Python
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos de tu aplicación al contenedor
COPY requirements.txt .
COPY app.py .

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080
EXPOSE 8080

# Define la variable de entorno PORT
ENV PORT 8080

# Ejecuta la aplicación Flask cuando el contenedor se inicie
CMD ["python", "app.py"]
