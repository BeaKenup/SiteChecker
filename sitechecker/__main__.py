import sys
import pathlib

from sitechecker.cli import read_user_cli_args, display_check_result
from sitechecker.functions import site_health_check

def main():
    user_args = read_user_cli_args()
    urls = user_args.urls
    if not urls:
        print("Erro: sem URLs para analisar.", file=sys.stderr)
        sys.exit(1)
    _site_check(urls)
    
def _site_check(urls):
    for url in urls:
        error = "Verifique a URL"
        try:
            result = site_health_check(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)
        
if __name__ == "__main__":
    main()