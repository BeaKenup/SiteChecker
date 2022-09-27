from http.client import HTTPConnection
from urllib.parse import urlparse

#Verifica se há um conexão HTTP/HTTPS com o site passado por parametro
def site_health_check (url):
    parser = urlparse(url)
    host = parser.netloc or parser.path.split("/")[0]
    for port in (80, 443):
        connection = HTTPConnection(host=host, port=port, timeout=2)
        try:
            connection.request("HEAD", "/")
            return True
        except Exception as e:
            return False
        finally:
            connection.close()