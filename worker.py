import time
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Fungsi untuk menjalankan HTTP server sederhana
def start_http_server():
    # Tentukan alamat dan port (port 8000)
    host = "0.0.0.0"  # Agar bisa diakses dari luar container
    port = 8000

    # Membuat server dan handler
    httpd = TCPServer((host, port), SimpleHTTPRequestHandler)
    
    print(f"Server started at http://{host}:{port}")
    
    # Jalankan server
    httpd.serve_forever()

if __name__ == "__main__":
    start_http_server()

