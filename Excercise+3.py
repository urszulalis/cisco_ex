
# coding: utf-8

# In[103]:


import re
filepath='ShowIpRoute.txt'
with open(filepath) as fp:  
    line = fp.readline()
    cnt = 1  
    while line:
        if "via" in line or "directly" in line :
            print(format(line.strip())) 
            cnt += 1
            routOutput(line)
        line = fp.readline()
        
fp.close()  

#ex="O 10.110.0.0  [160/5] via 10.119.254.6 , 0:01:00, Ethernet2"
#ex2="C 10.69.232.32  255.255.255.240  is directly connected, Ethernet0"
def routOutput (line):
    tmp1=line.split(",")
    tmp2=tmp1[0].split()
    #print(tmp2)
    my_dict= {'L' : 'local', 'C' : 'connected', 'S': 'static', 'R' : 'RIP', 'M' : 'mobile', 'B' : 'BGP',
                    'D' : 'EIGRP', 'EX' : 'EIGRP external', 'O' : 'OSPF', 'IA': 'OSPF inter area',
                    'N1' : 'OSPF NSSA external type 1',' N2' : 'OSPF NSSA external type 2',
                    'E1' : 'OSPF external type 1', 'E2' : 'OSPF external type 2', 'E' : 'EGP',
                    'i': 'IS-IS', 'su' : 'IS-IS summary', 'L1' : 'IS-IS level-1', 'L2' : 'IS-IS level-2',
                    'ia' : 'IS-IS inter area', '*' : 'candidate default', 'U' : 'per-user static route',
                    'o' : 'ODR', 'P ': 'periodic downloaded static route', 'H' : 'NHRP', 'l ': 'LISP',
                    'a' : 'application route', '+' : 'replicated route', '%' : 'next hop override'}
    
    
#protocol    
    if tmp2[0] in my_dict:
        tmpProtocol=my_dict.get(tmp2[0])
    if tmp2[1]=='E2':
        tmpProtocol='OSPF external type 2'
    elif tmp2[1]=='E1':
        tmpProtocol='OSPF external type 1'
    elif tmp2[1]=='EX':
        tmpProtocol='EIGRP external'    
    elif tmp2[1]=='L2':
        tmpProtocol='IS-IS level-2'
    elif tmp2[1]=='L1':
        tmpProtocol='IS-IS level-1'
    elif tmp2[1]=='IA':
        tmpProtocol='OSPF inter area'
    elif tmp2[1]=='N1':
        tmpProtocol='OSPF NSSA external type 1'  
    elif tmp2[1]=='N2':
        tmpProtocol='OSPF NSSA external type 1'
    
    if tmpProtocol!='connected':   
        # prefix, AD, next hop  
        pattern = r'((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])'
        m= re.match(pattern,tmp2[1])
        n= re.match(pattern,tmp2[2])
        if m:
            tmpIP1=m
            prefix=tmp2[2]
            nexthop=tmp2[4]
        else: 
            tmpIP1=n
            prefix=tmp2[3]
            nexthop=tmp2[5]

        print("Protocol:", tmpProtocol)
        print("Prefix:", format(tmpIP1.group(0)))
        print("AD/Metric",prefix)
        print ("Next-hop:",nexthop)
        print ("Last Update:", tmp1[1])
        print ("Outbound Interface:",tmp1[2])
        #print(tmp1)
    else: 
        pattern = r'((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])'
        m= re.match(pattern,tmp2[1])
        n= re.match(pattern,tmp2[2])
        tmpIP1=m
        tmpIP2=n
            
        print("Protocol:", tmpProtocol)
        print("Prefix:", format(tmpIP1.group(0)))
        print("AD/Metric")
        print ("Next-hop:",format(tmpIP2.group(0)))
        print ("Last Update:", )
        print ("Outbound Interface:",tmp1[1])
        #print(tmp1)
    return 0       
#routOutput(ex)
#routOutput(ex2)

