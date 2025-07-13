class TestClass:
    def __init__(self , x , y):
        self.x = x 
        self.y = y 
        self.safe_globals = locals()
        print(locals())
        print(self.safe_globals)
        del self.safe_globals['x']
        print(locals())
        print(self.safe_globals)


#TestClass(1 , 2)
print(type(eval("True")))  # ▶ 15