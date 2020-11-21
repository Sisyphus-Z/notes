def test(x=99,y=100,*args,**kwargs):
    print('x=',x,'y=',y)
    print("args =",args)
    print("kwargs =",kwargs)
    print("----------------------------------")

test(1,5,94,564)
test(a=1,b=2,c=3)
test(1,2,3,4,a=1,b=2,c=3)
# 输出：
# args = (1, 5, 94, 564)
# kwargs = {}
# ----------------------------------
# args = ()
# kwargs = {'a': 1, 'b': 2, 'c': 3}
# ----------------------------------
# args = (1, 2, 3, 4)
# kwargs = {'a': 1, 'b': 2, 'c': 3}
# ----------------------------------


def kw_dict(**kwargs):
    return kwargs
print(kw_dict(k1='v1',k2='v2',k3='v3'))
# 执行结果：
# {'k3': 'v3', 'k2': 'v2', 'k1': 'v1'}
