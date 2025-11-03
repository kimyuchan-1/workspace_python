# 애완동물 클래스

class Pet:
    """애완 동물 클래스"""

    def __init__(self, name: str, master: str) -> None:
        """생성자"""
        self._name = name           # 이름
        self._master = master       # 주인의 이름

    def introduce(self) -> None:
        """자기소개"""
        print('제 이름은 {}입니다!'.format(self._name))
        print('주인의 이름은 {}입니다!'.format(self._master))

    def __str__(self) -> str:
        """문자열화"""
        return self._name + ' <<' + self._master + '>>'

    def print(self) -> None:
        """출력(__str__이 리턴하는 문자열을 출력하고 개행)"""
        print(self.__str__())

# 애완동물 클래스 테스트
kurt = Pet('Kurt', '소영')
kurt.introduce()
print(kurt)
print('str(Kurt) = ' + str(kurt))
kurt.print()
