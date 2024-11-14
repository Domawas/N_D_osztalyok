"""Hozz létre egy Alkalmatzott osztályt,amelyiben az alábbi infókat tudod tárolnii egy cég dolgozóiról:
nev
szull_datum
fizetes
pozicio
"""

class Alkalmazott:
    def __init__(self, nev:str="",szull_datum:int=2000, fizetes:int=350000, pozicio:str=""):
        self.nev=nev
        self.szull_datum=szull_datum
        self.fizetes=fizetes
        self.pozicio=pozicio
        self.korok()

    def korok(self):
        self.kor=2024-self.szull_datum

    def __str__(self):
        """String metódus, amely visszaadja az alkalmazott adatait"""
        return f"Alkalmazott: {self.nev}, Születési dátum: {self.szull_datum}, Fizetés: {self.fizetes} Ft, Pozíció: {self.pozicio}, Kor: {self.kor}"