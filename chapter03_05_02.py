"""
Chapther03-05-02
Concurrency, CPU Bound vs I/O Bound - I/O Bound(3) - threading vs asyncio vs multiprocessing
Keyword - I/O Bound, requests, threading
"""

# I/O-Bound Multiprocessing 예제 (https://realpython.com/python-concurrency/#synchronous-version)

import multiprocessing
import threading  
import requests
import time

# 각 프로세스 메모리 영역에 생성되는 객체 (독립적)
# 함수 실행 할 때마다 객체 생성은 좋지 않음 -> 각 프로세스마다 할당

session = None

# 세션제공
def set_global_session() :
    global session
    if not session :
        session = requests.Session()

# 실행함수(1) - 다운로드
def request_stie(url) :
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"[{name} -> Read Contents : {len(response.content)} / Status Code : {response.status_code}] from {url}")

# 실행함수(2) - 요청
def request_all_site(urls) :
    # multiprocessing 실행
    # 반드시 processes 개수 조절 후 session 객체 및 실행 시간 확인
    with multiprocessing.Pool(initializer=set_global_session, processes=4) as pool :
        pool.map(request_stie, urls)

def main() :
    # 테스트 URLS
    urls = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
            "https://realpython.com/"
    ] * 3  # 총 9번 요청 테스트

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