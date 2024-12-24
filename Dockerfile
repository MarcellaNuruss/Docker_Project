# Gunakan image dasar Python
FROM python:3.11-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin semua file ke dalam container
COPY . /app

# Install dependensi yang diperlukan (misalnya Flask) secara langsung, jika diperlukan
RUN pip install --no-cache-dir flask 

# Atur command untuk menjalankan aplikasi
CMD ["python", "worker.py"]

