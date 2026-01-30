import utils.clients
import utils.http_session
import utils.transport
import utils.session
import requests
import time
from typing import Optional, Dict


def fetch_with_retry(url: str, max_retries: int = 3) -> Optional[Dict]:
    """
    Fetch data from URL with exponential backoff retry logic.
    """
    response = requests.get(url)

    pass


# Test cases
if __name__ == "__main__":
    print("Test 1: Valid URL")
    result = fetch_with_retry("https://jsonplaceholder.typicode.com/users")
    print(f"Success: {result is not None}\n")

    print("Test 2: 500 Error (should retry)")
    result = fetch_with_retry("https://httpstat.us/500")
    print(f"Result: {result}\n")

    print("Test 3: 404 Error")
    result = fetch_with_retry("https://httpstat.us/404")
    print(f"Result: {result}\n")

    print("Test 4: Invalid URL")
    result = fetch_with_retry("https://invalid-url-12345.com")
    print(f"Result: {result}\n")
