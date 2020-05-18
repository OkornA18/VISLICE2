STEVILO_DOVOLJENIH_NAPAK = 10

#konstante za rezultate ugibanj
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPAČNA_CRKA = '-'

#konstante za zmago in poraz
ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

bazen_besed = []
with open("besede.txt", encoding = "UTF-8") as datoteka_bazena:
    for beseda in datoteka_bazena:
        bazen_besed.append(beseda.strip().lower())

class Igra:
    def __init__(self, geslo, crke=None):
        self.geslo = geslo.lower()
        if crke is None:
            self.crke = []
        else:
            self.crke = [crka.lower() for crka in crke]

    def pravilne_crke(self):
        return[crka for crka in self.crke if crka in self.geslo]
    
    def napacne_crke(self):
        return[crka for crka in self.crke if crka not in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        trenutno = ''
        for crka in self.geslo:
            if crka in self.crke:
                trenutno += crka
            else:
                trenutno += '_'
        return trenutno
    
    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())    

    def ugibaj(self, ugibana_crka):
        ugibana_crka = ugibana_crka.lower()
        if ugibana_crka in self.crke:
            return PONOVLJENA_CRKA

        self.crke.append(ugibana_crka)

        if ugibana_crka in self.geslo:
            #uganil je
            if self.zmaga():
                return ZMAGA
            else :
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                    return NAPAČNA_CRKA

def nova_igra():
    import random
    izbrana_beseda = random.choice(bazen_besed)
    return Igra(izbrana_beseda)