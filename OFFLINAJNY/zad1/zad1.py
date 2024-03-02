#Mateusz Bobula

#Dla każdej litery, którą traktuje jako środek palindromu, szukam najdłuższego dla niej palindromu
#nastepnie zwracam dlugość najdłuższego z najdłuższych znalezionych palindromow
#Złozonosc O(n^2)


from zad1testy import runtests

def ceasar( s ):
    def UpdatedString(string):
        newString = ['#']
        for char in string:
            newString += [char, '#']
        return ''.join(newString)
        
    def Manachen(string):
        string = UpdatedString(string)
        LPS = [0 for _ in range(len(string))]
        C = 0
        R = 0

        for i in range(len(string)):
            iMirror = 2*C - i
            if R > i:
                LPS[i] = min(R-i, LPS[iMirror])
            else:
                LPS[i] = 0
            try:
                while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                    LPS[i] += 1
            except:
                pass
            
            if i + LPS[i] > R:
                C = i
                R = i + LPS[i]
        
        r=1
        for i in range(len(LPS)):
            if LPS[i]>r and LPS[i]%2==1:
                r=LPS[i]
                
        return r
    
    return Manachen(s)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )
