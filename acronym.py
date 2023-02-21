# Write the function acronym which computes the acronym
# from a phrase, i.e. acronym('random access memory')
# must return 'RAM'

def acronym(phrase):
    phrase=phrase.split()
    acronym=[]
    for i in phrase:
        acronym.append(i[0].capitalize())

    return "".join(acronym)



print(acronym('random access memory'))


