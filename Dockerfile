# 1️⃣ Imagen base con Python 3.9
FROM python:3.9

# 2️⃣ Definir el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3️⃣ Copiar los archivos del proyecto al contenedor
COPY . /app

# 4️⃣ Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Exponer el puerto de la aplicación
EXPOSE 5000

# 6️⃣ Definir el comando para ejecutar la aplicación
CMD ["python", "app/main.py"]
