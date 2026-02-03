"""
Chapther03-05-04
Concurrency, CPU Bound vs I/O Bound - I/O Bound(4) - threading vs asyncio vs multiprocessing
Keyword - I/O Bound, asyncio
"""

# I/O-Bound Asyncio 예제 (https://realpython.com/python-concurrency/#synchronous-version)
# threading 보다 높은 코드 복잡도 -> Async, Await 적절하게 코딩

import asyncio
import aiohttp
import time


# 실행함수(1) - 다운로드
async def request_stie(session, url) :
    async with session.get(url) as response :
        print("Read Contents {0}, from {1}".format(response.content_length, url))

# 실행함수(2) - 요청
async def request_all_site(urls) :
    async with aiohttp.ClientSession() as session :
        # 작업 목록
        tasks = []
        for url in urls :
            # 테스크 목록 생성
            task = asyncio.ensure_future(request_stie(session, url))
            tasks.append(task)

        # 테스크 확인
        print(*tasks)
        print(tasks)

        await asyncio.gather(*tasks, return_exceptions=True)

 # 최초로 실행되는 시점의 함수는 async를 붙이지 않아도 비동기로 실행 가능
def main() :
    # 테스트 URLS
    urls = [
            "https://www.jython.org",
            "http://olympus.realpython.org/dice",
            "https://realpython.com/"
    ] * 3  # 총 9번 요청 테스트

    # 실행 시간 측정
    start_time = time.time()

    # async 실행
    asyncio.run(request_all_site(urls))
    # asyncio.get_event_loop().run_until_complete(request_all_site(urls))

    # 종료 시간
    duration = time.time() - start_time
    
    print()
    # 결과 출력
    print(f'Download {len(urls)} sites in {duration} seconds')


if __name__ == '__main__' :
    main()