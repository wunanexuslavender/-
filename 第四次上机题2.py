class two1:
    # @staticmethod    #装饰器，定义静态方法用，不需要self不依赖类的实例，也就是在不需要参数的时候用
    def __init__(self,n):  #__init__放第一个，接受参数用
        self.n=n

    def pown(self,m):
        if m==1:
            return 2**self.n
        else:
            return 2**m


class two2:
    def pown(n):
        return 2**n


a=int(input('输入一个数:'))
print(two2.pown(a))
print(two1(a).pown(4))