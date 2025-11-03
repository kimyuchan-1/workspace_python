# 애완동물 클래스와 로봇 클래스

class Pet:
    """애완동물 클래스"""

    def __init__(self, name: str, master: str) -> None:
        """생성자"""
        self._name = name           # 이름
        self._master = master       # 주인의 이름

    def introduce(self) -> None:
        """자기 소개"""
        print('제 이름은 {}입니다!'.format(self._name))
        print('주인의 이름은 {}입니다!'.format(self._master))

    def __str__(self) -> str:
        """문자열화"""
        return self._name + ' <<' + self._master + '>>'

    def print(self) -> None:
        """출력(__str__이 리턴하는 문자열을 출력하고 개행)"""
        print(self.__str__())

class RobotPet(Pet):
    """로봇 클래스"""

    def __init__(self, name: str, master: str, type_no: str) -> None:
        """생성자"""
        super().__init__(name, master)  # 기본 클래스의 생성자를 호출
        self._type_no = type_no         # 번호

    def introduce(self) -> None:
        """자기 소개"""
        print('◆나는 로봇. 이름은 {}'.format(self._name))
        print('◆번호는 {}.'.format(self._type_no))
        print('◆내 주인은 {}.'.format(self._master))

    def __str__(self) -> str:
        """문자열화"""
        return(self._name + ' [[' + self._type_no + ']]'
                          + ' <<' + self._master + '>>')

    def work(self, sw: int) -> None:
        """집안일을 수행"""
        if   sw == 0: print('청소합니다.')
        elif sw == 1: print('세탁합니다.')
        elif sw == 2: print('요리합니다.')

#  애완동물 클래스와 로봇 클래스 테스트

kurt = Pet('Kurt', '소영')
kurt.introduce()
print(kurt)

r2d2 = RobotPet('R2D2', '준우', 'R2')
r2d2.introduce()
print(r2d2)

def self_introduce(obj: object) -> None:
    """obj에 자기소개를 요청"""
    obj.introduce()

self_introduce(kurt)
self_introduce(r2d2)

#  애완동물 클래스와 로봇 클래스 테스트(계속)

# kurt는 Pet타입 인스턴스
kurt.print()

# r2d2는 RobotPet타입 인스턴스
r2d2.print()
r2d2.work(1)
