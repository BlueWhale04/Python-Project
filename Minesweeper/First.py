import random
#jadval = araye to dar to ######Part1
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

#moshakhas kardane khone haye min dar #######Part2
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

#moshakhas kardane shomare khone ########Part3
while True:
    x1 , y1 = map(int , input().split())
    khone_entekhabi = (x1 , y1)
    ''' x va y khona ro tahvil migirim '''

    def tedad_min_dore_khone(khone_entekhabi):
        Numkhone = 0  #shomare khone ke baiad neshon bedim
        if (x1 -1 , y1) in shomarekhone:
            Numkhone += 1
        if (x1 +1 , y1) in shomarekhone:
            Numkhone += 1

        if (x1 -1 , y1 -1) in shomarekhone:
            Numkhone += 1
        if (x1 +1 , y1 -1) in shomarekhone:
            Numkhone += 1    

        if (x1 -1 , y1 +1) in shomarekhone:
            Numkhone += 1
        if (x1 +1 , y1 +1) in shomarekhone:
            Numkhone += 1 

        if (x1 , y1 -1) in shomarekhone:
            Numkhone += 1
        if (x1 , y1 +1) in shomarekhone:
            Numkhone += 1
        #print (Numkhone)
        return Numkhone        

    if khone_entekhabi in shomarekhone:
        print ("Bakhti Feshar Bokhor Ahmagh")
        break
        '''برای اینکه درست بشه باید یدونه break اینجا بزارین و یه حلقه ایجاد کنیم برای این پارت سوم '''
    else:
        adade_khone = tedad_min_dore_khone(khone_entekhabi)

    #falan nemidonam chera jodash kardam
    def nemdonam(khone_entekhabi):
        khonehaye_atraf = [ (x1 -1 , y1) , (x1 +1 , y1) , (x1 -1 , y1 -1) , (x1 +1 , y1 -1) , (x1 -1 , y1 +1) , (x1 +1 , y1 +1) , (x1 , y1 -1) , (x1 , y1 +1) ] 
        return khonehaye_atraf
    list_khonehaye_atraf = nemdonam (khone_entekhabi) 

    def tashkhis_khali_bodan(list_khonehaye_atraf):
        list1 = [] #tedade min haye dore har khone az list 
        for x in range (len(list_khonehaye_atraf)):
            sefre_yana = tedad_min_dore_khone (list_khonehaye_atraf[x])
            list1.append(sefre_yana)
        return list1    
    list_sefre_yana = tashkhis_khali_bodan (list_khonehaye_atraf)


    #baraye vghti ke shomare khone sefre
    if adade_khone != 0:
        javab_shomare_khone = adade_khone
    else:
        tem = 0 
        list2 = [] #shomare khone hayi ke poche
        while True :
            yoyo = list_sefre_yana.count(0)
            if yoyo == 0:
                break
            else:
                if list_sefre_yana[tem] != 0 :
                    continue
                else:
                    tmp = nemdonam(list_khonehaye_atraf[tem])
                    list2.append(list_khonehaye_atraf[tem])
                    list_khonehaye_atraf.pop(tem)
                    list_sefre_yana.pop(tem)
                    tashkhis_khali_bodan(tmp)
                    yoyo -= 1
                    tem -= 1
                tem += 1  

print(list_khonehaye_atraf)          
print(list_sefre_yana)
print(list2)
        
