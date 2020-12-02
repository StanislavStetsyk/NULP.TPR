import pandas as pd
df = pd.read_csv('variant23.csv')
df = df.drop('можливі стани',axis='columns')
columns = list(df)

#Критерій Вальда
print('Критерій Вальда')
vald = []
for i in columns:
    vald.append(df[i].min())
print(vald)
print('Найкращим з найгірших є: ', max(vald))
print()

#Максимальний 
print('Максимальний')
max_ = []
for i in columns:
    max_.append(df[i].max())
print(max_)
print('Найкращим з найкращих є: ', max(max_))
print()

#Гурвіца а=0.5
print('Гурвіца а=0.5')
a = 0.5
gur = {}
for i in columns:
    gur[i] = max(df[i])*0.5+min(df[i])*(1-a)
gur = list(gur.values())
print(gur)
print('Найкращий:', max(gur))
print()

#Лапласса при рівномірних умовах
print('Лапласса при рівномірних умовах')
laplass = {}
for i in columns:
    for j in range(len(df[i])):
        if i not in laplass:
            laplass[i] = 0
        laplass[i] += df[i][j]/len(columns)
laplass = list(laplass.values())
print(laplass)
print('Найкращий:',max(laplass))
print()

#Лапласса при p1=0.5, p2=0.35, p3=0.15
print('Лапласса при p1=0.5, p2=0.35, p3=0.15')
laplass2 = {}
p = [0.5,0.35,0.15]
for i in columns:
    for j in range(len(df[i])):
        if i not in laplass2:
            laplass2[i] = 0
        laplass2[i] += df[i][j]*p[j]
laplass2 = list(laplass2.values())
print(laplass2)
print('Найкращий:',max(laplass2))
print()

results = pd.DataFrame(list(zip(vald, max_, gur,laplass,laplass2)), 
               columns =['Max', 'Vald','Gur','Laplas','Laplas2'],index = columns) 
print(results)
results.to_csv(r'Results.csv')