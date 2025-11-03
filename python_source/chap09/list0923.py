# 딕셔너리에 저장된 사람의 정보 출력하기

def put_person(**person):
    """딕셔너리 person에 있는 정보를 출력"""
    if 'name' in person: print('이름 =', person['name'], end='  ')
    if 'visa' in person: print('국적 =', person['visa'], end='  ')
    if 'age'  in person: print('연령 =', person['age'],  end='  ')
    print()  # 개행

put_person(name='손지형', visa='한국', age=27)
put_person(name='조탁', visa='중국')
