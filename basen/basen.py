i=0
c='0'
tab=[]
print('Wprowadź liczby akceptując każdą enterem (zakończ wprowadzanie nie cyfrą):')
while (c.isdigit()):
    c=input()
    if (c.isdigit()):
        tab.append(int(c))
    i+=1
i=0
a=0
c='s'
pc=''
for i in range(0,len(tab)):
    if (i!=len(tab)-1):
        if(tab[i]==tab[i+1]):
            if (i==0):
                c='r'
            else:
                c=pc
        elif (tab[i] < tab[i + 1]):
            c='r'
        elif (tab[i] > tab[i + 1]):
            c='m'
        if(c!=pc):
            a+=1
            pc=c
print(a)
