pris = input('Varans pris?')
momsSats = input('Hur många procent är momssatsen?')
int_pris = int(pris)
int_momsSats = int(momsSats)
moms = int_momsSats * int_pris / 100
exklMoms = int_pris - moms
print ('Varans pris är', pris)
print ('Moms:', moms)
print ('Exklusive moms:', exklMoms)