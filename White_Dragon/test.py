def funA(fn):
    print('A')
    fn() # 执行传入的fn参数
    return 'fkit'
'''
下面装饰效果相当于：funA(funB)，
funB 将会替换（装饰）成 funA() 语句的返回值；
由于funA()函数返回 fkit，因此 funB 就是 fkit
'''
@funA
def funB():
    print('B')
print(funB) # fkit