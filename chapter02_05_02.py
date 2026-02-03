"""
Chapther02-05_02
Parallelism with Multiprocessing - multiprocessing(4) - Sharing state
Keyword - memory sharing, array, value
"""

# 프로세스 동기화 관련 참고
# https://docs.python.org/3/library/multiprocessing.html#synchronization-between-processes

from multiprocessing import Process, current_process, Value, Array
import os

# 2. 프로세스 메모리 공유 예제 (공유o)

# 실행함수
def generate_update_number(v : int) :
    for _ in range(50) :
        v.value += 1
    print(current_process().name, 'data', v.value)

# 메인
def main() :
    # 부모 프로세스 아이디
    parent_process_id = os.getpid()
    #  출력
    print(f'Parent process ID {parent_process_id}')

    # 프로세스 리스트 선언
    processes = list()

    # 프로세스 메모리 공유 변수
    # from multiprocess import shared_memory 사용 가능 (python 3.8)
    # from multiprocess omport Manager 사용 가능

    # Value('타입', 초기값)
    # 'i' : int / 'f' : float ' / 'c' : char ...등

    # 배열 사용시
    # share_numbers = Array('i', range(50))
    share_value = Value('i', 0)


    for _ in range(9) :
        # 생성
        p = Process(target=generate_update_number, args=(share_value,))
        # 배열에 담기
        processes.append(p)
        # 실행
        p.start()

    # Join
    for p in processes :
        p.join()

    # 최종 프로세스 부모 변수 확인
    print('Final Data in parrent process : ', share_value.value)  # 0 출력 (프로세스는 독립적(공유x)이므로 메모리 공유변수 값이 0으로 출력)

if __name__ == '__main__' :
    main()