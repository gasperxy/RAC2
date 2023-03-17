# =============================================================================
# Žabica
# =====================================================================@033082=
# 1. podnaloga
# Žabica se je izgubila v močvari in želi kar se da hitro odskakljati ven. Na
# srečo močvara vsebuje veliko muh, s katerimi si lahko povrne energijo, kajti
# utrujena žabica ne skoči daleč.
# 
# S funkcijo `zabica(mocvara)` želimo ugotoviti, kako hitro lahko žabica
# odskaklja iz močvare. Močvaro predstavimo s tabelo, kjer žabica prične na
# ničtem polju. Če je močvara dolžine `k`, je cilj žabice priskakljati vsaj na
# `k`-to polje ali dlje (torej prvo polje, ki ni več vsebovano v tabeli).
# 
# Energičnost žabice predstavimo z dolžino najdaljšega možnega skoka. Torej
# lahko žabica z količino energije `e` skoči naprej za katerokoli razdaljo med
# `1` in `e`, in če skoči naprej za `k` mest ima sedaj zgolj `e - k` energije.
# Na vsakem polju močvare prav tako označimo, koliko energije si žabica povrne,
# ko pristane na polju. Tako se včasih žabici splača skočiti manj daleč, da
# pristane na polju z več muhami. Predpostavimo, da ima vsako polje vrednost
# vsaj `1`, da lahko žabica v vsakem primeru skoči naprej.
# 
# V primeru `[2, 4, 1, 2, 1, 3, 1, 1, 5]` lahko žabica odskaklja iz močvare v
# treh skokih, v močvari `[4, 1, 8, 2, 11, 1, 1, 1, 1, 1]` pa potrebuje zgolj
# dva.
# =============================================================================
from functools import lru_cache
def zabica(mocvara):
    st_lokvanjev = len(mocvara)
    energija = mocvara[0]
    lokvanj = 0
    if st_lokvanjev == 0:
        return 0
    @lru_cache(maxsize=None)
    def zabica2(lokvanj,energija):
        najmanjsi = float('inf')
        for razdalja in range(1,energija+1):
            if razdalja+lokvanj < st_lokvanjev:
                najmanjsi = min(najmanjsi, zabica2(lokvanj+razdalja,energija-razdalja+mocvara[lokvanj+razdalja]))
            else:
                return 1
        return najmanjsi+1
    return zabica2(lokvanj,energija)