# %%
print("Hola Mundo!")

#%%
print("Adios amigos!")
# %%
arreglo = [12, 56, 34, 23, 87, 47]

def mean(dataset) :
    return sum(dataset) / len(dataset)

print(mean(arreglo))

#%%
import statistics
arreglo = [12, 56, 34, 23, 87, 47]

med = statistics.median(arreglo)

print(med)

#%%
import statistics
arreglo = [12, 56, 34, 23, 87, 47, 47]

med = statistics.mode(arreglo)

print(med)

#%%
import statistics

df = pd.read_excel("insurance.csv", header = None)

print(df)