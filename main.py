class Distibution:
    def __init__(self,values:list[int]) -> None:
        self.values=values
        self.max=max(self.values)
        self.min=min(self.values)
        self.d=dict.fromkeys(values,0)
        for i in values:
            self.d[i]+=1

    def F(self,x:int)->float:
        sum=0
        for i,j in self.d.items():
            if i <x:
                sum+=j
        return sum/len(self.values)
        # return (x-self.min)/(self.max-self.min)
    def div_F(self)->float:
        return 1/(self.max-self.min)
    def r(self,x:int)->float:
        return x-((1-self.F(x))/self.div_F())

