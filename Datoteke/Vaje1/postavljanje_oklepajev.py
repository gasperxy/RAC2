def oklepaji(izraz):
    ''' rekurzivno poišče največjo in najmanjšo vrednost, ki ju lahko dosežemo
    z dodajanjem oklepajev izrazu izraz '''
    if not izraz:  # izraz je prazen niz
        return (0, 0)
    
    izraz = izraz.split()  # sestavimo seznam števil in operatorjev
    if len(izraz) == 1:  # izraz vsebuje le eno število
        return (int(izraz[0]), int(izraz[0]))
    
    n = len(izraz) // 2  # število operatorjev, ki nastopa v izrazu
    # nastavimo začetna ekstrema na nekaj zelo majhnega in nekaj zelo velikega
    najvecja = -float('inf')
    najmanjsa = float('inf')
    
    for i in range(n):
        op = izraz[2*i+1]  # operator
        levo_max, levo_min = oklepaji(' '.join(izraz[:2*i+1]))  # leva stran tabele=niz od trenutnega operatorja
        desno_max, desno_min = oklepaji(' '.join(izraz[2*i+2:]))  # niz desne strani tabele
        if op == '+':
            kandidat1 = levo_max + desno_max
            kandidat2 = levo_min + desno_min
            max_vrednost = max(kandidat1, kandidat2)
            min_vrednost = min(kandidat1, kandidat2)
        elif op == '-':
            kandidat1 = levo_max - desno_min
            kandidat2 = levo_min - desno_max
            max_vrednost = max(kandidat1, kandidat2)
            min_vrednost = min(kandidat1, kandidat2)
        elif op == '*':
            kandidat3 = levo_max * desno_max
            kandidat4 = levo_min * desno_min
            max_vrednost = max(kandidat3, kandidat4)
            min_vrednost = min(kandidat3, kandidat4)
            
        if max_vrednost > najvecja:
            najvecja = max_vrednost
        if min_vrednost < najmanjsa:
            najmanjsa = min_vrednost
    
    return najvecja, najmanjsa
