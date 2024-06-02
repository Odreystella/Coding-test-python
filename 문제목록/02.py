'''
문제 02 배열 제어하기 

난이도: ⭐️⭐️
저자 권장 시간: 10분
권장 시간 복잡도: O(NlogN)
출제: 저자 출제
날짜: 2024-05-28 화요일

제약조건:
    - 배열 길이는 2 이상 1,000 이하입니다.
    - 각 배열의 데이터 값은 -100,000 이상 100,000 이하 입니다.

입출력의 예: 입력 -> 출력
    - [4, 2, 2, 1, 3, 4] -> [4, 3, 2, 1]
    - [2, 1, 1, 3, 2, 5, 4] -> [5, 4, 3, 2, 1]
'''


# 정수 배열을 하나 받고, 중복값을 제거하여 데이터를 내림차순으로 정렬하여 반환하는 solution() 함수를 완성하세요.
def solution(arr):
    modified_arr = list(set(arr)) # O(N)
    modified_arr.sort(reverse=True) # O(NlogN)
    return modified_arr


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([4, 2, 2, 1, 3, 4])) # 반환값 : [4, 3, 2, 1]
# print(solution([2, 1, 1, 3, 2, 5, 4])) # 반환값 : [5, 4, 3, 2, 1]


'''
Note:
- 배열의 길이가 1,000이라 짧은편이다.
- set()은 집합을 생성하는 파이썬의 내장함수로 중복값을 제거한다.
- 반복문을 통해 일일이 데이터를 확인해서 중복값이 있는지 확인하는 알고리즘은 for문과 in을 사용하게되면 시간복잡도가 O(N²)
- set()함수는 해시 알고리즘으로 데이터를 저장하기 때문에 시간복잡도 O(N)을 보장한다.
- O(1) < O(logN) < O(N) < O(NlogN) < O(N²) < O(N³)
- 최종 시간복잡도는 O(NlogN)
''' 
