
# coding: utf-8

# In[27]:


access_template = ['switchport mode access','switchport access vlan {}','switchport nonegotiate','spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q','switchport mode trunk','switchport trunk allowed vlan {}']

mode_in= input("Enter interface mode(access/trunk):")
mode_inter= input('Enter interface type and number:')
if mode_in =="access":    
    mode_acc_vlan= input("Enter VLAN number:")
    print("Interface:",mode_inter)
    for i in range (len(access_template)):
        if access_template[i]=='switchport access vlan {}' :
            print(access_template[i].replace("{}", mode_acc_vlan))
        else:
            print(access_template[i])        
else:
    mode_trunk_vlan= input("Enter allowed VLAN") 
    print("Interface:",mode_inter)
    for i in range (len(trunk_template)):
        if (trunk_template[i]=='switchport trunk allowed vlan {}'):
            print(trunk_template[i].replace("{}", mode_trunk_vlan))
        else:
            print(trunk_template[i])
            
       

