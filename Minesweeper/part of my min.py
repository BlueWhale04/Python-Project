import random
#jadval = araye to dar to
levelgames = int(input())
if levelgames == 1:
    levelgame = 9
elif levelgames == 2:
    levelgame = 16
elif levelgames == 3:
    levelgame = 24        

khonelist = []
for x in range (1 , levelgame+1):
    khonelist.append(x)
starlist = []    
for x in range (1 , levelgame+1):
    starlist.append(khonelist)
#print(starlist)

#moshakhas kardane khone haye min dar
if levelgame == 9:
    tmp = 10 
elif levelgame == 16:
    tmp = 40
elif levelgame == 24:
    tmp = 99            
shomarekhone = []
while len(shomarekhone) != tmp:
    x = random.choice(khonelist)
    y = random.choice(khonelist)
    min = (x , y)
    if shomarekhone.count(min) == 0:
        shomarekhone.append(min)
    else:
        continue    
print(shomarekhone)    

#moshakhas kardane shomare khone 
x1 , y1 = map(int , input().split())
khone_entekhabi = (x1 , y1)
''' x va y khona ro tahvil migirim '''

def tedad_min_dore_khone(khone_entekhabi):
    Numkhone = 0  #shomare khone ke baiad neshon bedim
    if (x1 -1 , y1) or (x1 +1 , y1) in shomarekhone:
        Numkhone += 1
    if (x1 -1 , y1 -1) or (x1 +1 , y1 -1) in shomarekhone:
        Numkhone += 1
    if (x1 -1 , y1 +1) or (x1 +1 , y1 +1) in shomarekhone:
        Numkhone += 1   
    if (x1 , y1 -1) or (x1 , y1 +1) in shomarekhone:
        Numkhone += 1
    #print (Numkhone)
    return Numkhone        

if khone_entekhabi in shomarekhone:
    print ("Bakhti Feshar Bokhor Ahmagh")
else:
    adade_khone = tedad_min_dore_khone(khone_entekhabi)

