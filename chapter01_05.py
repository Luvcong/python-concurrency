"""
Chapther01-05
Multithreading - Thread(3) - ThreadPoolExcutor
Keyword - Many Threads, concurrent.futures, (xxx)PoolExcutor
"""

"""
그룹 스레드
1. Python 3.2 이상 표준 라이브러리 사용
2. concurrent.futures
3. with 사용으로 생성, 소멸 라이프 사이클 관리 용이
4. 디버깅 어려움 (단점)
5. 대기중인 작업 -> Queue -> 완료 상태 조사 -> 결과 또는 예외 -> 단일화(캡슐화)
"""

import logging
from concurrent.futures import ThreadPoolExecutor
import threading
import time

# 스레드 실행 함수
def task(name) :
    logging.info('Sub Thread %s : staring', name)

    result = 0
    
    for i in range(1, 10001) :
        result += i
    
    logging.info('Sub Thread %s : finishing result : %d', name, result)
    
    return result

# 메인 영역
def main() :
    # Logging format 설정
    format = '(%(asctime)s) %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info('Main Thread : before creating and running thread')

    # 실행 방법 (1)
    # max_workes : 작업의 개수가 넘어가면 직접 설정이 유리
    # excutor = ThreadPoolExecutor(max_workers=3)

    # task1 = excutor.submit(task, ('First', ))
    # task2 = excutor.submit(task, ('Two', ))

    # print(task1.result())
    # print(task2.result())

    # 실행 방법 (2)
    with ThreadPoolExecutor(max_workers=3) as excutor :
        tasks = excutor.map(task, ['First', 'Second', 'Third'])
        # 결과 확인
        print(list(tasks))

if __name__ == '__main__' :
    main( )