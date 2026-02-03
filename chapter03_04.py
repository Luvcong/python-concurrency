"""
Chapther03-04
Concurrency, CPU Bound vs I/O Bound - I/O Bound(1) - Synchronous
Keyword - I/O Bound, request
"""

# I/O-Bound Sync 예제 (https://realpython.com/python-concurrency/#synchronous-version)

import requests
import time

# 실행함수(1) - 다운로드
def request_stie(url, session) :
    # 세션 확인
    with session.get(url) as response :
        print(f"[Read Contents : {len(response.content)}, Status Code : {response.status_code}] from {url}")

# 실행함수(2) - 요청
def request_all_site(urls) :
    with requests.Session() as session :
        for url in urls :
            request_stie(url, session)

def main() :
    # 테스트 URLS
    urls = [
        'https://www.jython.org',
        'http://olympus.realpython.org/dice',
        'https://realpython.com'
    ] * 3   # 총 9번 요청 테스트

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    request_all_site(urls)

    # 종료 시간
    duration = time.time() - start_time
    
    print()
    # 결과 출력
    print(f'Download {len(urls)} sites in {duration} seconds')


if __name__ == '__main__' :
    main()