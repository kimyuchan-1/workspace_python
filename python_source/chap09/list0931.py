"""딕셔너리에서 특정한 값을 가지는 키의 리스트 생성"""

def keys_of(dic: dict, val: 'value') -> list:
    """딕셔너리 dic에 있는 값이 val인 요소의 키를 리스트로 리턴"""
    return [k for k, v in dic.items() if v == val]

txt = input('문자열 : ')
count = {ch: txt.count(ch) for ch in txt}
print('분포=', count)

num = int(input('몇 개짜리 문자：'))
print('{}개의 문자={}'.format(num, keys_of(count, num)))
