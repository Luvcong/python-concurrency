"""
Chapther03-05-03
Concurrency, CPU Bound vs I/O Bound - I/O Bound(4) - Asyncio basic
Keyword - I/O Bound, requests, threading
"""

"""
동시 프로그래밍 패러다임 변화
- 싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그램 대두 -> CPU연산, DB연동, API호출 대기 시간이 늘어남
- python 3.4 비동기(asyncio) 표준 라이브러리 등장
"""

import time
import asyncio

async def exe_calculate_async(name, n) :
    for i in range(1, n + 1) :
        print(f'{name} -> {i} of {n} is calculating...')
        asyncio.sleep(1)
    print(f'{name} - {n} working done!')


async def process_async() :
    start = time.time()
    # 여러 개의 함수를 실행하는 경우 wait()로 묶어서 처리할 수 있음
    await asyncio.wait([
        exe_calculate_async('One', 3),
        exe_calculate_async('Two', 2),
        exe_calculate_async('Three', 1)
    ])

    end = time.time()
    print(f'>>> total seconds : {end - start}')

def exe_calculate_sync(name, n) :
    for i in range(1, n + 1) :
        print(f'{name} -> {i} of {n} is calculating...')
        time.sleep(1)
    print(f'{name} - {n} working done!')

def process_sync() :
    start = time.time()

    exe_calculate_sync('One', 3)
    exe_calculate_sync('Two', 2)
    exe_calculate_sync('Three', 1)

    end = time.time()

    print(f'>>> total seconds : {end - start}')

if __name__ == '__main__' :
    # 1) Sync 실행
    # process_sync()

    # 2) Async 실행
    # python3.7 이상
    asyncio.run(process_async())

    # python 3.7 미만
    # asyncio.get_event_loop().run_until_complete(process_async())