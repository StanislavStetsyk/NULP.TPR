import pandas as pd
df = pd.read_csv('Specs.csv')

names = ['HyperX', 'G.Skill', 'GoodRam', 'Patriot','Crucial','AMD']
def fun(row,name):
    return row['Вага']*row[name]
list_=[]
for i in range(len(names)):
    list_.append(round(sum(df.apply(fun,name=names[i], axis = 1)),2))
result = list(zip(names,list_))

result_df = pd.DataFrame(result,columns=['Планка памяті','Оцінка'])
result_df = result_df.sort_values('Оцінка',ascending = False)
result_df.to_csv(r'results.csv')
print(result_df)