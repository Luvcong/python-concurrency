"""
Chapther03-06
Concurrency, CPU Bound vs I/O Bound - CPU Bound(1) - Synchronous
Keyword - CPU Bound
"""

# CPU-Bound 예제 (https://realpython.com/python-concurrency/#synchronous-version)

import time

def cpu_bound(number) :
    return sum(i * i for i in range(number))

def find_sums(numbers) :
    result = []
    for number in numbers :
        result.append(cpu_bound(number))
    return result

def main() :
    numbers = [3_000_000 + x for x in range(30)]

    # 실행시간
    start_time  = time.time()

    # 실행
    total = find_sums(numbers)

    print()

    # 결과출력
    print(f'total list : {total}')
    print(f'sum : {sum(total)}')

    # 종료시간
    duration = time.time() - start_time
    print(f'duration : {duration} seconds')

if __name__ == '__main__' :
    main()