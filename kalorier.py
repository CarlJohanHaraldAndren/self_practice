# For example kcals({'ägg': 137}, [(2,'ägg')]) should return
# 137*2=274 kilocalories for a receipe which includes only two eggs.

def kcals(dict,list):
    kalorier=0
    for line in list:
        if line[1] in dict:
            kalorier+=line[0]*dict.get(line[1])

    return kalorier

print(kcals({'ägg': 137}, [(2,'ägg')]))