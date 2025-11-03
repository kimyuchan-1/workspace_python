# map의 예시2(모든 요소의 단위를 센치미터에서 인치로 변환하기)

x = [1, 2, 3, 4]

print(list(map(lambda n: 2.54 * n , x)))
