"""
Chapther02-06_01
Parallelism with Multiprocessing - multiprocessing(5) - Queue, Pipe
Keyword - Queue, Pipe, Communications between processes
"""

# 프로세스 통신 구현 - Pipe (부모(recv), 자식(send)간 1대1 통신)
from multiprocessing import Process, Pipe, current_process
import time
import os

# 실행함수
def worker(id, baseNum, conn) :
    process_id = os.getpid()
    process_name = current_process().name

    # 누적
    sub_total = 0

    # 계산
    for i in range(baseNum) :
        sub_total += 1
    
    # produce
    conn.send(sub_total)
    conn.close()

    print(f'Process ID : {process_id} / Process Name : {process_name} / id : {id}')
    print(f'Result : {sub_total}')

# 메인
def main() :
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    # 출력
    print(f'Parent process ID : {parent_process_id}')

    # 시간 기록
    start_time = time.time()

    # Pipe 선언 : 2개의 값을 반환 (부모, 자식 값)
    parent_conn, child_conn = Pipe()

    t = Process(name=str(1), target=worker, args=(1, 100000000, child_conn))

    # 시작
    t.start()

    # join
    t.join()

    # 순서 계산 시간
    print('--- %s seconds ---' % (time.time() - start_time))

    print()

    print("Main Processing Total count = {}".format(parent_conn.recv()))
    print("Main Processing Done!")

if __name__ == '__main__' :
    main()