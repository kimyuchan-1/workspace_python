class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def show(self):
        print(f'이름: {self.name}, 나이: {self.age}, 평균점수: {self.average():.2f}')

    def is_passed(self):
        return self.average() >= 60

    def __str__(self):
        return f'이름: {self.name}, 나이: {self.age}, 점수: {self.scores}'


if __name__ == "__main__":
    students = [
        Student("홍길동", 18, [80, 75, 90]),
        Student("김유신", 17, [55, 60, 58]),
        Student("유관순", 18, [95, 88, 92]),
        Student("강감찬", 19, [40, 50, 45])
    ]

    for s in students:
        print(s)
        s.show()
        print()