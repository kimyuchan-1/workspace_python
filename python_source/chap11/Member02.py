# 스포츠 클럽 회원 클래스2

class Member:
    """스포츠 클럽 회원 클래스2"""

    def __init__(self, no: int, name: str, weight: float) -> None:
        """생성자"""
        self.no = no            # 회원 번호
        self.name = name        # 이름 
        self.weight = weight    # 체중

    def print(self) -> None:
        """데이터 출력"""
        print('{}: {} {}kg'.format(self.no, self.name, self.weight))

# 회원 클래스 테스트

kim = Member(15, '김준호', 72.7)
park = Member(37, '박지혜', 65.3)

kim.print()
park.print()
