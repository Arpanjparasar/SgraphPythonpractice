class hello:
    def __init__(self,foo):
        self.foo=foo


    def dis(self):
        print(self.foo)


obj = hello([1,2,3,4,5])
obj.dis()