# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:13:17 2020

@author: Goettcke
"""
#%%
import json

file = open('dbl.json', encoding='UTF-8') #dansk fil skal omdannes til engelsk
dbl = json.load(file)
#print(dbl)

#%% Utility functions
def person_age(person):
    try: 
        birth, death = person['l'].split("-") # Unpacking 
        person_age = int(death) - int(birth)
        return person_age
    except: 
        return -1 

def print_people(persons): 
    for person in persons: 
        print(f"\n{person['name']}, \nage : {person_age(person)}, \nlife span : {person['l']}, \noccupations: {person['o']}")

#%% Aristocrats 

def aristocrats(persons): 
    people = []
    sub_names = [" af ", " von ", " van ", " de "]
    for person in persons: 
        for sub_name in sub_names: 
            if sub_name in person['name']:
                people.append(person)
                break
    return people
    
    
#%% Test aristocrats
#print_people(aristocrats(dbl))
print(len(aristocrats(dbl)))

#%% First name 
def first_name(persons, name): 
    people = []
    for person in persons: 
        #print(person['name'])
        name_list = person['name'].split(" ")
        first_name = name_list[0]
        if first_name == name: 
            people.append(person)
    return people
        
        
#%% Testing first name 
print_people(first_name(dbl, "Per"))

#%% born_rural 

def born_rural(persons): 
    people = []
    big_cities = ["Copenhagen", "Odense", "Aarhus"]
    
    for person in persons: 
        if person["p"] not in big_cities: 
            people.append(person)
    return people


#%% born_rural_using_two_for_loops

def born_rural_v2(persons): 
    people = []
    for person in persons: 
        if person["p"] != "Copenhagen" and person["p"] != "Odense" and person["p"] != "Aarhus": 
            people.append(person)
    return people 


#%% Testing born rural 
x = born_rural(dbl)
y = born_rural_v2(dbl)

#print(x)    
#print(y)
print(len(x) == len(y))
#%% older than 

def older_than(persons, age): 
    people = []
    for person in persons: 
        try: 
            birth, death = person['l'].split("-") # Unpacking 
            person_age = int(death) - int(birth)
            if person_age >= 90: 
                people.append(person)
            #print(person_age)
        except: 
            pass # pass = fuck it and continue
    return people 

#%% older than using utility function 

def older_than_using_util(persons, age): 
    people = []
    for person in persons: 
        if person_age(person) >= 90: 
            people.append(person)
            
    return people 
#%% Test older than 
print_people(older_than_using_util(dbl,90))


#%% death between

def death_between(persons, year_min=1940, year_max=1945): 
    people = []
    for person in persons: 
        try: 
            time_of_death = person['l'].split("-")[1]
            if year_min <= int(time_of_death) <= year_max: 
                people.append(person)
                print(person)
        except: 
            pass
    return people 



#%% Testing death between 
#death_between(dbl,1940,1945)
print_people(death_between(persons=dbl, year_min=1940, year_max=1945)) #This is the same, as the above
        
    
#%% fun(tion) painters 

def painters(persons): 
    people = []
    #year_min = 1800 # If you don't like magic constants 
    #year_max = 1850
    for person in persons:
        if 1800 <= person["y"] <= 1850 and "painter" in person["o"]:
            people.append(person)
            
    return people 
        
        

#%% test painters 
print_people(painters(dbl))

#%% occupations 

def occupations(persons, olist): 
    people = []
    
    for person in persons: 
        has_occupations = True
        for occupation in olist: 
            if occupation not in person['o']: 
                has_occupations = False 
        
        if has_occupations == True: 
            people.append(person)
            
    return people
            

#%% testing occupations 
        
print_people(occupations(dbl, ["writer", "judge"]))

#%% occupation_stats 
def occupation_stats(persons): 
    occupation_dict = {}
    
    for person in persons: 
        for occupation in person['o']:
            if occupation in occupation_dict.keys():
                occupation_dict[occupation] += 1
            else: 
                occupation_dict[occupation] = 1
    return occupation_dict

    

#%% Testing occupation stats 

occupation_dict = occupation_stats(dbl)

#%% incomplete 
def incomplete(persons): 
    
    people_without_bd = []
    people_with_b = []
    people_with_d = []
    
    for person in persons: 
        if person['l'] == "-": 
            people_without_bd.append(person)
        elif person['l'][0] == "-": 
            people_with_d.append(person)
        elif person['l'][-1] == "-": 
            people_with_b.append(person)
        
    return [people_without_bd, people_with_b, people_with_d]


#%% testing incomplete

print(incomplete(dbl)[2])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


