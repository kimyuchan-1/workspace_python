# 아이덴티티가 있는 장군 클래스

class Commander:
    """장군 클래스"""

    __counter = 0   # 몇 번까지 아이덴티티를 사용하는지

    def __init__(self, name: str) -> None:
        """생성자"""
        self.__name = name
        Commander.__counter += 1
        self.__id = Commander.__counter

    def id(self) -> int:
        """"아이덴티티 받기"""
        return self.__id

    @classmethod
    def max_id(cls) -> int:
        """"지금까지 아이덴티티를 몇 번까지 부여했는가"""
        return cls.__counter

    def print(self) -> None:
        """데이터 출력"""
        print('{}:{}번'.format(self.__name, self.__id))

kim = Commander('김유신')			# 아이덴티티는 1
yi = Commander('이순신')			# 아이덴티티는 2
kang = Commander('강감찬')			# 아이덴티티는 3

print('kim.id() = {}'.format(kim.id()))
print('yi.id() = {}'.format(yi.id()))
print('kang.id() = {}'.format(kang.id()))

print('Commander.max_id() = {}'.format(Commander.max_id()))
print('kim.max_id() = {}'.format(kim.max_id()))
