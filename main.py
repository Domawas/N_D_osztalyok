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


print(etel_lista[0])


"""Hozz létre egy Alkalmatzott osztályt,amelyiben az alábbi infókat tudod tárolnii egy cég dolgozóiról:
nev
szull_datum
fizetes
pozicio

készíts hozzá egy kor metodust ami megmondja az adott ember korát
__str__

Hozz létre legalább 5embert,tedd bele őket egy listába
-mennyi az össz fizetés
-hány éves a legidősebb ember?
-hány ember van beosztott pozicioban
-kinek a legalacsonyabb a fizetese?
++ az osztálynak legyen egy fizetesemeles metodusa amelyik a fizetést megemeli a paraméterében megadott % értékkel.
A legkisebb fizetésű ember fizetését emeld meg 20%-al"""
from Alkalmazott import Alkalmazott
import fuggvenyek2
alkalmazottak=[]
alkalmazottak.append(Alkalmazott("Ferenc",2000,350000,"Raktáros"))
alkalmazottak.append(Alkalmazott("Tibor",2005,500000,"Eladó"))
alkalmazottak.append(Alkalmazott("Lívia",1985,280000,"Beosztott"))
alkalmazottak.append(Alkalmazott("Ábel",1978,550000,"Beosztott"))
alkalmazottak.append(Alkalmazott("Krisztina",2002,320000,"Tűzoltó"))

ossz=fuggvenyek2.ossz_fizetes(alkalmazottak)
print(f"Az összes fizetés: {ossz}")

max_i=fuggvenyek2.legidosebb(alkalmazottak)
print(f"A legidősebb alkalmazott: {alkalmazottak[max_i].nev}, {alkalmazottak[max_i].kor} éves")

beoszt=fuggvenyek2.beosztottak(alkalmazottak)
print(f"Összesen: {beoszt} db 'beosztott' van ")

min_i=fuggvenyek2.legalacsonyabb_fizetes(alkalmazottak)
print(f"A legalacsonyabb fizetés: {alkalmazottak[min_i].fizetes}Ft")
