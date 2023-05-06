from elt import Elt
class Vrsta:

    def __init__(self, zacetni_elti=None):
        self._zacetni = Elt(None, dummy=True)
        self._koncni = self._zacetni
        if zacetni_elti:
            for x in zacetni_elti:
                self.vstavi(x)

    def prazna(self):
        return self._zacetni.dummy

    def vstavi(self, vsebina):
        self._koncni.naslednji = Elt(None, dummy=True)
        self._koncni.vsebina = vsebina
        self._koncni.dummy = False
        self._koncni = self._koncni.naslednji

    def zacetek(self):
        if self.prazna():
            raise IndexError('vrsta je prazna')
        return self._zacetni.vsebina

    def odstrani(self):
        if self.prazna():
            raise IndexError('vrsta je prazna')
        self._zacetni = self._zacetni.naslednji

    def __repr__(self):
        seznam = []
        p = self._zacetni
        while not p.dummy:
            seznam.append(repr(p.vsebina))
            p = p.naslednji
        return 'Vrsta([{0}])'.format(', '.join(seznam))

    def __str__(self):
        if self.prazna():
            return 'ZACETEK : KONEC'
        seznam = []
        p = self._zacetni
        while not p.dummy:
            seznam.append(str(p.vsebina))
            p = p.naslednji
        return 'ZACETEK : ' + ' : '.join(seznam) + ' : KONEC'