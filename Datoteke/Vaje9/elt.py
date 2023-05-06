class Elt:

    def __init__(self, vsebina, dummy=False):
        self.dummy = dummy
        if not dummy:
            self.vsebina = vsebina
    
    def __str__(self):
        return str(self.vsebina)