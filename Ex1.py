
# coding: utf-8

# In[10]:


import re
v=1
va=1
while v==1 :
    a= input("Enter IP address:")
    pattern = r'((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]?[0-9])'

    m= re.match(pattern,a)
    if m:
        break
    else:
        print ("Invalid IP address")
   

while va==1 :
    b= input ("Enter subnet mask in decimal format:")
    sec_pattern= r'(^\/([0-9]|[1-2][0-9]|3[0-2])$)'
    n=re.match(sec_pattern,b)
    if n:
        break
    else: 
        print("Subnetmask is invalid")        

#print (a,b)

c=a.split(".")
IPfirst_o='{0:08b}'.format(int(c[0]))
IPsecond_o='{0:08b}'.format(int(c[1]))
IPthird_o='{0:08b}'.format(int(c[2]))
IPfourth_o='{0:08b}'.format(int(c[3]))



mask=b[1:3]
binarymask=""
for i in range(32):
    if(i<=int(mask)-1):
        binarymask+="1"
    else:
        binarymask+="0"

first_bm=binarymask[:8] 
second_bm=binarymask[8:16] 
third_bm=binarymask[16:24] 
fourth_bm=binarymask[-8:]


def and_op (str1, str2):    
    network_IP_bin=""
    for i in range(len(str1)):
        tmp=int(str1[i])&int(str2[i])
        network_IP_bin+=str(tmp)
    return network_IP_bin        
 
net1=int(and_op(first_bm,IPfirst_o),2)
net2=int(and_op(second_bm,IPsecond_o),2)
net3=int(and_op(third_bm,IPthird_o),2)
net4=int(and_op(fourth_bm,IPfourth_o),2)
netfull=""
netfull+=and_op(first_bm,IPfirst_o)
netfull+=and_op(second_bm,IPsecond_o)
netfull+=and_op(third_bm,IPthird_o)
netfull+=and_op(fourth_bm,IPfourth_o)

print('network address is: ',net1,'.',net2,'.',net3,'.',net4,b, sep='')

def broadcast(str1, strMask):
    str_broad=""
    for i in range(len(str1)):
        if strMask[i]=="1":
           str_broad+=str1[i]
        else:
            str_broad+="1"
    return str_broad
            
brod_bin=broadcast(netfull,binarymask)

broad1=int(brod_bin[:8],2)
broad2=int(brod_bin[8:16],2)
broad3=int(brod_bin[16:24],2)
broad4=int(brod_bin[-8:],2)
print('broadcast address is: ',broad1,'.',broad2,'.',broad3,'.',broad4,b, sep='')

