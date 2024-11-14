def etlap(etel_lista):
    """itt irjuk ki az ételek neveit"""
    for i in range (0,len(etel_lista),1):
        print (f"**{etel_lista[i].nev}{etel_lista[i].ar:>10} Ft **")

def atlag_ar(etel_lista):
    osszeadas=0
    for i in range (0,len(etel_lista),1):
        osszeadas+=(etel_lista[i].ar)
    atlagar= osszeadas/len(etel_lista)
    return atlagar
    
def legdragabb(etel_lista):
    max_index = 0
    for i in range (0,len(etel_lista),1):
        if (etel_lista[i].ar < etel_lista[max_index].ar):
            max_index+=1
    return max_index