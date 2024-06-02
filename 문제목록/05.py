'''
문제 05 행렬의 곱셈

난이도: ⭐️
저자 권장 시간: 40분
권장 시간 복잡도: O(N³)
출제: 프로그래머스
정답률: 63%
날짜: 2024-06-02 일요일

제약조건:
    - 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
    - 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
    - 곱할 수 있는 배열만 주어집니다.

입출력의 예: 입력 -> 출력
    - arr1: [[1, 4], [3, 2], [4, 1]], arr2: [[3, 3], [3, 3]] -> [[15, 15], [15, 15], [15, 15]]
    - arr1: [[2, 3, 2], [4, 2, 4], [3, 1, 4]], arr2: [[5, 4, 3], [2, 4, 1], [3, 1, 1]] -> [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
'''


# 다른 사람 풀이
def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0]) # 1. arr1, arr2가 ? X ? 행렬인지 계산하기
    r2, c2 = len(arr2), len(arr2[0])
    answer = [[0] * c2 for _ in range(r1)] # 2. 두 행렬을 곱한 결과 ? X ? 행렬이 나올지 초기화하기 r1 X c2 크기를 가짐

    for i in range(r1): # 3. 행렬 곱 공식에 맞게 계산하기 arr1의 각 행과
        for j in range(c2): # 4. arr2의 각 열에 대해 
            for k in range(c1): # 5. 결과 행렬에 값을 구한다.
                answer[i][j] += arr1[i][k] * arr2[k][j]

    return answer


# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# arr1, arr2 = [[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]
# print(solution(arr1, arr2)) # 반환값 : [[15, 15], [15, 15], [15, 15]]
# arr1, arr2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
# print(solution(arr1, arr2)) # 반환값 : [[22, 22, 11], [36, 28, 18], [29, 20, 14]]


'''
Note:
- 행렬의 곱셈에 대해 기억이 안나서 공부가 필요했다. 
- https://ko.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-matrices/v/matrix-multiplication-intro
- 책에 있는 풀이를 보면서 내가 계산한 행렬 곱에 맞게 값이 나오는지 코드를 이해했다.
- 이 문제에서는 문제를 쪼개서 생각하는 방법을 배웠다.
    - 1. 행렬을 곱하려면 곱한 결과의 행렬의 크기를 알아야 하기 때문에 주어진 arr1, arr2의 크기를 먼저 구한다.
    - 2. 두 행렬의 크기로 결괏값이 어떤 크기를 가질지 계산하고 초기화한다.
    - 3. 결괏값의 크기만큼 반복문을 돌고, 초기화한 행렬의 값을 하나씩 채워간다.
- 최종 시간복잡도는 O(N³)
''' 
