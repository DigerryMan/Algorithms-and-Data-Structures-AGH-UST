class Employee:
    def __init__(self, fun):
        self.emp=[] #lsita dzieci
        self.fun=fun
        self.f= -1 #wartosc funa calej imprezy dla aktualnego pracownika
        self.g= -1 #gdy nie idzie


def f(v:Employee):
    if v.f>=0: return v.f

    x=v.fun
    for u in v.emp:
        x+=g(u)

    y=g(v)
    v.f=max(x,y)

    return v.f

def g(v:Employee):
    if v.g>=0: return v.g

    x=0
    for u in v.emp:
        x+=f(u)

    v.g=x
    return v.g



























