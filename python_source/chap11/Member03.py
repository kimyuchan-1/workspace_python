# 스포츠 클럽 회원 클래스3

class Member:
    """스포츠 클럽 회원 클래스3"""

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

# 회원 클래스 테스트

kim = Member(15, '김준호', 72.7)
park = Member(37, '박지혜', 65.3)

kim.lose_weight(3.5)     # 김준호 회원이 3.5kg 감량
park.lose_weight(5.3)     # 박지혜 회원이 5.3kg 감량

kim.print()
park.print()
