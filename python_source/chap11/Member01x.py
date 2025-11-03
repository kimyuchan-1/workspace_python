# 스포츠 클럽 회원 클래스1(오류)

class Member:
    """스포츠 클럽 회원 클래스1"""
    pass

# 회원 클래스 테스트

kim = Member()
kim.no = 15
kim.name = '김준호'
kim.weight = 72.7

park = Member()
park.no = 38
park.name = '박지혜'
park.weigth = 65.3    # 변수명 오류

print('{}: {} {}kg'.format(kim.no, kim.name, kim.weight))
print('{}: {} {}kg'.format(park.no, park.name, park.weight))
