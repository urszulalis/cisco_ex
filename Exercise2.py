
# coding: utf-8

# In[135]:


import re 
filepath = 'commands.txt'  

def uniquevlans(vlan):
    tmp_tab=[]
    for i in range(max(vlan)+1):
        tmp = vlan.count(i)
        #print("wystapienie",i, "->",tmp)
        if tmp !=0:
            tmp2=vlan.index(i)
            #print("indeks: ",i, "to", tmp2)
            #print(vlan[tmp2])
            tmp_tab.append(vlan[tmp2])
    #print("unique values in vlan: ",tmp_tab)        
    return tmp_tab

def valueInEveryVlan (vlan,numb):
    tmp_tab=[]
    for i in range(max(vlan)+1):
        tmp = vlan.count(i)
        #print("wystapienie",i, "->",tmp)
        if tmp>=numb:
            tmp2=vlan.index(i)
            #print("indeks: ",i, "to", tmp2)
            #print(vlan[tmp2])
            tmp_tab.append(vlan[tmp2])
    print("List_1=",tmp_tab)        
    return tmp_tab

def onlyInOneVlan (vlan,numb):
    tmp_tab=[]
    for i in range(max(vlan)+1):
        tmp = vlan.count(i)
        #print("wystapienie",i, "->",tmp)
        if tmp==numb:
            tmp2=vlan.index(i)
            #print("indeks: ",i, "to", tmp2)
            #print(vlan[tmp2])
            tmp_tab.append(vlan[tmp2])
    print("List_2=",tmp_tab)        
    return tmp_tab
    
with open(filepath) as fp:  
    line = fp.readline()
    cnt=1;
    all_uniq_matches=[]
    all_matches=[]
    
    while line:
        matches =[]
        pattern2= re.compile(r'switchport trunk allowed vlan \d+')
        m=re.match(pattern2,line)
        if m:
            pattern=re.compile( r'\d+')
            matches+=pattern.findall(line)
            matches=[int(i) for i in matches]
            all_matches+=matches
            print(format(line.strip()))
            #print(matches)
            all_uniq_matches+=uniquevlans(matches)
            cnt+=1
        line = fp.readline()
    valueInEveryVlan(all_uniq_matches,cnt-1) 
    onlyInOneVlan(all_matches,1)
    #print(all_uniq_matches)
    #print(all_matches)
file.close()              

