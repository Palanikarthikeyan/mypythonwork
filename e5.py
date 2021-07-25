pn1=input("Enter a partition name:")
ps1=input("Enter {} partition Size:".format(pn1))
pn2=input("Enter a partition name:")
ps2=input("Enter {} partition Size:".format(pn2))

total=int(ps1)+int(ps2)
'''
print('Partition {}\t Size:{}'.format(pn1,ps1))
print('Partition {}\t Size:{}'.format(pn2,ps2))
print('-'*50)
print('Total partition Size:{}'.format(total))
print('-'*50)
'''
print('''Partition {}\t Size:{}
Parition {}\t Size:{}
---------------------------------
Total Partition Size:{}
---------------------------------'''.format(pn1,ps1,pn2,ps2,total))

