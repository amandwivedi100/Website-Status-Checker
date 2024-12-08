import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict

def check_status(url: str) -> None:
    response: Response = requests.get(url)

    try:

        #Information
        status_code: int = response.status_code
        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status code: {status_code}')
        print(f'Content Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time:,.2f} seconds')

    except RequestException as e:
        print(f'Error: {e}')

def main() -> None:
    url_to_check: str = 'https://www.python.org'
    check_status(url=url_to_check)

if __name__ == '__main__':
    main()

