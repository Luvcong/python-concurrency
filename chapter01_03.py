"""
Chapther01-03
Multithreading - Thread(1) - Basic
Keyword - threading basic
"""

import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name) :
    logging.info('Sub Thread %s : starting', name)
    time.sleep(3)
    logging.info('Sub Thread %s : finishing', name)

# 메인 영역
if __name__ == '__main__' :
    # Logging Format 설정
    format = '(%(asctime)s) %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info('Main Thread : before creating thread')

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First', ))
    logging.info('Main Thread : before running thread')

    # 서브 스레드 시작
    x.start()
    logging.info('Main Thread : wait for the thread to finish')

    # join()을 사용하면 자식 스레드의 작업이 다 끝날 떄까지 기다린 후 부모 스레드 종료
    # x.join()

    logging.info('Main Thread : all done!')