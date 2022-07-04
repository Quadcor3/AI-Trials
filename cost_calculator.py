

days = 0
weight = 1

class person:
    def __init__(self, name, days, cont):
        self.days = days
        self.name = name
        self.cont = cont


def inputs():
    person.days = int(input("Gün sayısı: "))
    person.cont = int(input("Any contribution: "))
    a = int(input("ort insan:"))
    ave_p = a
    person.calc = 667*days / ave_p * weight - cont
    print(calc)



inputs()