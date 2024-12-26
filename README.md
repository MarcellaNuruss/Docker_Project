# UASP AKSO 2024

### Langkah-langkah

1. **Masuk ke Direktori**
   ```bash
   cd <NAMA-DIREKTORI>
   ```

2. **Periksa File Konfigurasi**
   Pastikan file `docker-compose.yml` ada di dalam direktori utama.

3. **Jalankan Layanan**
   Gunakan perintah berikut untuk menjalankan layanan:
   ```bash
   docker-compose up -d
   ```

4. **Periksa Status Kontainer**
   ```bash
   docker ps
   ```

5. **Hentikan Layanan**
   Untuk menghentikan layanan, gunakan perintah berikut:
   ```bash
   docker-compose down
   ```

### Layanan yang Tersedia
1. **NGINX** - Sebagai web server.
   - Port: `8080:80`

2. **MySQL** - Sebagai database server.
   - Port: `3307:3306`

3. **Adminer** - GUI untuk mengelola MySQL.
   - Port: `8081:8080`

4. **Redis** - Sebagai message queue.
   - Port: `6379:6379`

5. **RabbitMQ** - Sebagai message broker.
   - Ports: 
     - `5672:5672` (Messaging Port)
     - `15672:15672` (Management UI)

6. **Prometheus** - Monitoring system.
   - Port: `9090:9090`

7. **Grafana** - Dashboard visualisasi.
   - Port: `3000:3000`

### Konfigurasi
- **NGINX**: File konfigurasi dapat ditemukan di `./nginx/default.conf`.

### Akses Layanan
   - **NGINX**: `http://localhost:8080`
   - **Adminer**: `http://localhost:8081`
   - **Prometheus**: `http://localhost:9090`
   - **Grafana**: `http://localhost:3000`
   - **RabbitMQ Management**: `http://localhost:15672`

