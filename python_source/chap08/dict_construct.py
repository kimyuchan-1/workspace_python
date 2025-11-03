# 사전 생성하기

dict01 = {}                     # {}    빈 사전
dict02 = {'Korea': 408, 'China': 156, 'Japan': 392, 'Taiwan': 158}

dict03 = dict()                 # {}    빈 사전

lst = [('Korea', 408), ('China', 156), ('Japan', 392), ('Taiwan', 158)]
dict04 = dict(lst)

key = ['Korea', 'China', 'Japan', 'Taiwan']
value = [408, 156, 392, 158]
dict05 = dict(zip(key, value))

print('dict01 =', dict01)
print('dict02 =', dict02)
print('dict03 =', dict03)
print('dict04 =', dict04)
print('dict05 =', dict05)
