from egzP6btesty import runtests 

def compare(x,y):
    return x[0]==y[0] and x[1]==y[1]

def jump ( M ):
    x, y = 0, 0
    jumps=[[x,y]]

    for el in M:
        if el=='UL':
            x, y = x-1, y-2
        elif el=='UR':
            x, y = x+1, y-2   
        elif el=='RU':
            x, y = x+2, y-1   
        elif el=='RD':
            x, y = x+2, y+1
        elif el=='DR':
            x, y = x+1, y+2   
        elif el=='DL':
            x, y = x-1, y+2   
        elif el=='LD':
            x, y = x-2, y+1   
        elif el=='LU':
            x, y = x-2, y-1

        jumps.append([x,y])

    jumps.sort(key=lambda x:(x[0], x[1]))

    n=len(jumps)
    lastJump=jumps[0]
    cntr=1

    res=1

    for i in range(1,n):
        if compare(lastJump, jumps[i]):
            cntr+=1

        else:
            if cntr%2:
                res+=1
            
            lastJump=jumps[i]
            cntr=1        


    return res
    

#jd=['UL', 'UR', 'UL', 'DR']

runtests(jump, all_tests = True)