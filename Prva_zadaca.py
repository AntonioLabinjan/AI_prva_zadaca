## PRVI ZADATAK
# numpy ima i automatic funkciju za dijagonalni array
'''
import numpy as np
dijagonale = []
for i in range(3):
    brojevi = int(input("unesite brojeve za na dijagonalu arraya "))
    dijagonale.append(brojevi)

novi_array = np.diag(dijagonale)

print(novi_array)
''' 
# a moremo i ručno ako ćemo
'''
import numpy as np

dijagonale = []
for i in range(3):
  brojevi = int(input("unesite brojeve za na dijagonalu arraya "))
  dijagonale.append(brojevi)

novi_array_2 = np.zeros((3,3))
for i in range(3):
  novi_array_2[i, i] = dijagonale[i]

print(novi_array_2)
'''   
## DRUGI ZADATAK
'''
import numpy as np
random_seed = int(input("unesite proizvoljni seeed: "))
np.random.seed(random_seed)

array = np.random.randint(0, 10, size=(5,10))
print(array)
sortirani_array = np.sort(array.flatten())
print(sortirani_array)
'''
# lakša verzija
'''
import numpy as np
random_seed = int(input("unesite proizvoljni seed: "))
np.random.seed(random_seed)

array = np.random.randint(0, 10, size=(5,10))
print(array)
sortirani_array = np.sort(array, axis=None)
print(sortirani_array)
 '''
'''
## TREĆI ZADATAK
import numpy as np
random_seed_2 = int(input("unesite proizvoljni seed:"))
np.random.seed(random_seed_2)

array_2 = np.random.randint(1,10, size=(3,4))
print(array_2)
print(array_2[1, 2:]) # more i -2: (isto će delat)
'''

'''
## ČETVRTI ZADATAK
import numpy as np

last_seed = int(input("unesite proizvoljni seed: "))
np.random.seed(last_seed)

last_array = np.random.random((5,5))

print(last_array)

najmanje = np.min(last_array, axis = 1)
najveće = np.max(last_array, axis = 1)
ar_sred = np.mean(last_array, axis = 1)

print(" ")
print("Array najmanjih", najmanje)
print("  ")
print("Array najvećih: ", najveće)
print(" ")
print("Array aritmetičke sredine: ", ar_sred)
