class Klasa:
    def __init__(self,k,tab):
        self.k=k
        self.tab=tab
        self.aux=[0 for _ in range(k+1)]

        for el in self.tab:
            self.aux[el]+=1

        for i in range(1,k+1):
            self.aux[i] = self.aux[i] + self.aux[i-1]    

    def count_num_in_range(self, a, b):
        return self.aux[b]-self.aux[a-1]        