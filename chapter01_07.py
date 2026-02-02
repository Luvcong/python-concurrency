"""
Chapther01-07
Multithreading - Thread(5) - Prod vs Cons Using Queue
Keyword - 생산자 소비자 패턴 (Producer / Consumer Pattern)
"""

"""
Producer-Consumer Pattern
1. 멀티스레드 디자인 패턴의 정석
2. 서버측 프로그래밍의 핵심
3. 주로 허리역할 (중요)

Python Event 객체
1) .Flag 초기값 : 0
2) .Set() 초기값 : 1
3) Clear() 초기값 : 0
4) Wait : 1인 경우 return / 0인 경우 waiting
5) inSet() : 현재 flag 상태
"""

import concurrent.futures
import logging
import queue
import random
import threading
import time

# 생산자
def producer(queue, event) :
    """ 네트워크 대기 상태라 가정 (서버) """
    while not event.is_set() : 
        message = random.randint(1, 11)
        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info('Producer received event Exiting')

# 소비자
def consumer(queue, event) :
    """ 응답 받고 소비하는 것으로 가정 or DB 저장 """
    while not event.is_set() or not queue.empty() :
        message = queue.get()
        logging.info("Consumer storing message: %s (size=%d)", message, queue.qsize())

    logging.info('Producer received event Exiting')

if __name__ == '__main__' :
    # Logging format 설정
    format = '(%(asctime)s) %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # Queue 사이즈 설정 (중요)
    # 적절한 사이즈로 지정하지 않는 경우 병목현상, 성능저하 등의 현상이 나타나게 됨
    pipeline = queue.Queue(maxsize=10)

    # Event Flag 초기값 0
    event = threading.Event()

    # With Context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor :
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        # 실행 시간 조정
        time.sleep(0.1) 
        logging.info('Main : about to set event')
        
        # 프로그램 종료
        # while True :
            # pass
        event.set()