class Distibution:
    def __init__(self,values:list[int]) -> None:
        self.values=values
        self.max=max(self.values)
        self.min=min(self.values)

    def F(self,x:int)->float:
        return (x-self.min)/(self.max-self.min)
    def div_F(self)->float:
        return 1/(self.max-self.min)
    def r(self,x:int)->float:
        return x-((1-self.F(x))/self.div_F())
if __name__ == '__main__':
    l=[10,30,30,30]
    d=Distibution(l)
    print(d.div_F(),list(map(lambda x:(d.F(x),d.r(x),d.div_F()),l)))
    l=[50,5,29]
    print(d.div_F(), list(map(lambda x: (d.F(x), d.r(x), d.div_F()), l)))
    l=[i for i in range(10,30,2)]
    print(d.div_F(), list(map(lambda x: (x,d.F(x), d.r(x), d.div_F()), l)))
    l = [10, 30]
    d = Distibution(l)
    print(d.div_F(), list(map(lambda x: (x, d.F(x), d.r(x), d.div_F()), l)))
    print(d.F(12))