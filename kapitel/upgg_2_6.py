tid = input('Ange antal sekunder: ')
tid = int(tid)
tim = tid // 3600
min = (tid % 3600) // 60
sek = (tid % 3600) % 60 

print('Antal timmar:', tim, 'Antal minuter:', min, 'Antal sekunder', sek)
