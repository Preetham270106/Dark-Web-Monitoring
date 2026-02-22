from crawler.tor_session import get_tor_session
from crawler.content_parser import extract_text
from datetime import datetime

def crawl_onion(url):
    session = get_tor_session()

    try:
        response = session.get(url, timeout=30)

        if response.status_code == 200:
            text = extract_text(response.text)

            return {
                "source_url": url,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "raw_text": text
            }

    except Exception as error:
        print("Error crawling", url, error)

    return None