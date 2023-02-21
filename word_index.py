# Example: word_index('the spider indexes the spider web') must return
# {'the': [0,3],'spider': [1,4], 'indexes': [2], 'web': [5]}

def word_index(string):
    min_dict={}
    string=string.split()
    print(string)
    plats=0
    for i in string:
        if i in min_dict:
            min_dict[i]+=[plats]
            pass
        else:
            min_dict[i]=[plats]
        #print(min_dict)
        plats+=1
    return min_dict

word_index('the spider indexes the spider web')
