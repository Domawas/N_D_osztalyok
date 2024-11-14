def ossz_fizetes(alkalmazottak):
    osszeadas=0
    for i in range (0,len(alkalmazottak),1):
        osszeadas+=(alkalmazottak[i].fizetes)

    return osszeadas

def legidosebb(alkalmazottak):
    max_index=0
    for i in range(0,len(alkalmazottak),1):
        if (alkalmazottak[i].kor > alkalmazottak[max_index].kor):
            max_index=i
    return max_index

"""hány ember van beosztott pozicioban"""

def beosztottak(alkalmazottak):
    beoszt=0
    for i in range(0,len(alkalmazottak),1):
        if(alkalmazottak[i].pozicio =="Beosztott"):
            beoszt+=1
    return beoszt