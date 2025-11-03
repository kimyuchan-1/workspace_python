# 스포츠 클럽 회원 클래스4

class Member:
    """스포츠 클럽 회원 클래스4"""

    def __init__(self, no: int, name: str, weight: float) -> None:
        """생성자"""
        self.__no = no
        self.__name = name
        self.__weight = weight

    def lose_weight(self, loss: float) -> None:
        """loss킬로그램 감량"""
        self.__weight -= loss

    def print(self) -> None:
        """데이터 출력"""
        print('{}: {} {}kg'.format(self.__no, self.__name, self.__weight))

    @property
    def weight(self) -> float:
        """체중 획득(게터)"""
        return self.__weight

    @weight.setter
    def weight(self, weight: float) -> None:
        """체중 설정(세터)"""
        self.__weight = weight if weight > 0.0 else 0.0

# 회원 클래스 테스트

kim = Member(15, '김준호', 72.7)

kim.weight = 67.3                        # 김준호 회원의 체중 설정
print('kim.weight =', kim.weight)    	 # 김준호 회원의 체중 확인
