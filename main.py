"""
osztalyzatok_lista=[1,4,2,3]
nevek=["Béla","Jenő","Ági","Rozi",3]

nevek és a nevekhez tartozó osztályzatok összetartoznak

etelek=["húsleves","krumplis"]
ar=[1234,3456]

új adatszerkezet

szemely = {név: "Béla", osztályzat:3 }

kaja1 = {nev: "húsleves", ar:1234, elk_ido:2 }
kaja2 = {nev: "krumplis", ar:12345 elk_ido:0.5 }

objektumok - tulajdonságokkal(főnevek) és viselkedéssel(cselekvés) bíró adatszrkezet

készítünk egy sablont ami alapján letudjuk gyártani a konkrét egyedeket(ételeket,emberek).
OSZTÁLY - sablon - osztály - tervrajz
OBJEKTUM - konkrét egyedek - objektumok - konkrét termék


"""

from Etel import Etel
import fuggvenyek

"""2. lépés létrehozzuk a konkrét példányít a tervrajz alapján"""

etel_lista=[] #berakjuk listába
etel_lista.append(Etel("Húsleves",1234))
etel_lista.append(Etel("Krumplis",2345))
etel_lista.append(Etel("Rántott hús",2145))
etel_lista.append(Etel("Palacsinta",1450))


print("Szia én vagyok a " + etel_lista[0].nev + " Az állapotom " + etel_lista[0].allapot ) #folyamatban kiir 
"""
etel1.keszul()
print("Szia én vagyok a " + etel1.nev + " Az állapotom " + etel1.allapot ) #megváltozik készre az állapot
print("Szia én vagyok a " + etel2.nev + " Az állapotom " + etel2.allapot ) 

"""
"""Írj metódust ami paraméterében megkapja a listát és kiirja az ételek neveit és árait látványosan"""


fuggvenyek.etlap(etel_lista)

"""Írj metódust ami paraméterében megkapja a listát és megmondja az ételek átlagárát"""
atlagar=fuggvenyek.atlag_ar(etel_lista)
print(f"Az ételek átlagára: {atlagar}")

"""Írj metódust ami paraméterében megkapja a listát és megmondja a a legdrágább étel nevét"""
max_i=fuggvenyek.legdragabb(etel_lista)
print(f"A legdrágább étel neve: {etel_lista[max_i].nev} {etel_lista[max_i].ar}Ft")
