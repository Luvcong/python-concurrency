"""
Chapther02-04
Parallelism with Multiprocessing - multiprocessing(3) - ProcessPoolExecutor
Keyword - ProcessPoolExecutor, as_completed, futures, timeout, dict
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import urllib.request

# 조회 URLS
URLS =  [
    'http://www.daum.net/',
    'http://www.cnn.com/',
    'http://www.naver.com/',
    'http://www.bbc.co.uk/',
    'http://some-made-up-domain.com/'
    ]

# 실행 함수
def load_url(url, timeout) :    # timeout : 특정 시간동안 응답이 없으면 연결 종료
    with urllib.request.urlopen(url, timeout=timeout) as conn :
        return conn.read()

# 메인 함수
def main() :
    # 프로세스풀 Context 영역
       with ProcessPoolExecutor(max_workers=5) as executor :
        # Future 로드 (실행x / 적재 o)
        future_to_url = {executor.submit(load_url, url, 60) : url for url in URLS}
        
        # 실행
        for future in as_completed(future_to_url) : # timeout = 1
            # key 값이 Future 객체
            url = future_to_url[future] # future_to_url.get('future')
            
            try :
                data = future.result()  # 결과
            except Exception as e :
                print('%r generated an exception: %s' % (url, e))   # 예외처리
            else :
                print('%r page is %d bytes' % (url, len(data)))   # 결과확인

# 메인시작  
if __name__ == '__main__' :
    main() 