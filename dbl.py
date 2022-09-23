import json

file = open('dbl.json', encoding='UTF-8') #dansk fil skal omdannes til engelsk
dbl = json.load(file)
#print(dbl)

#%%
def ratio(persons):
    m = 0
    f = 0
    for item in dbl:
        if item["g"] == "m":
            m += 1
        elif item["g"] == "f":
            f += 1
    print( m/(m+f)*100,"% men" )
    print( f/(m+f)*100,"% women" )

# print(ratio(dbl))

#%%
def born_in(persons,city):
    persons2 = []
    for item in persons:
        if item["p"] == city:
            persons2.append(item)
    return persons2

print(born_in(dbl,"Odense"))
    
#%%
def occupied_as(persons,occupation):
    persons2 = []
    for p in persons:
        if occupation in p['o']:
            persons2.append(p)
    return persons2

print(occupied_as(dbl, "writer"))  #obs med at ikke skrive med stort


#%% 
# What is the gender ratio in the DBL?
ratio()

# What persons were born in Odense?
print(born_in(dbl,"Odense"))

# What persons were occupied as writers?
print(occupied_as(dbl,"writer"))

# What persons born in Copenhagen were occupied as writers?
bornInCopenhagen = born_in(dbl,"Copenhagen")
print(occupied_as(bornInCopenhagen,"judge"))