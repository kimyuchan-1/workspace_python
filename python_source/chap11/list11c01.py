# 네임 맹글링 확인

class C():
    __abc = 5

# 변경 후의 이름으로 액세스 불가
print(C._C__abc)

# 원래 이름으로는 액세스 불가
print(C.__abc)
