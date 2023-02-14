def lisa_andmed(i:list,p:list):
    """
    param list i: Inimeste järjend
    param list p: Palgade järjend
    :rtype: list, list
    """
    n=int(input("Mitu inimesed: "))
    for j in range(n):
        nimi=input("Sisesta nimi: ")
        palk=int(input("Sisesta palk: "))
        i.append(nimi)
        p.append(palk)
    return i,p

def delete_nimi(i:list,p:list):
    """
    param list i: Inimeste järjend
    param list p: Palgade järjend
    :rtype: list, list
    """
    nimi=input("Sisesta nimi:")
    if nimi in i:
        n=i.count(nimi)
        for j in range(n):
            ind=i.index(nimi)
            i.pop(ind)
            p.pop(ind)
        return i,p

def suurim_palk(i:list,p:list):
    """
    param list i: Inimeste järjend
    param list p: Palgade järjend
    :rtype: int, str
    """

    palk=max(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def luhim_palk(i:list,p:list):
    """
    param list i: Inimeste järjend
    param list p: Palgade järjend
    :rtype: int, str
    """
    palk=min(p)
    ind=p.index(palk)
    nimi=i[ind]
    return palk,nimi

def sorteerimine(i:list,p:list):

    v=int(input("palk 1-kahaneb,2-kasvab? "))
    if v==1:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]>p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    elif v==2:
        n=len(p)
        for j in range(0,n-1):
            for k in range(j+1,n):
                if p[j]<p[k]:
                    abi=p[j]
                    p[j]=p[k]
                    p[k]=abi
                    abi=i[j]
                    i[j]=i[k]
                    i[k]=abi
    return i,p

def vordsed_palgad(i:list,p:list):

    dublikatid=[x for x in p if p.count(x)>1]
    dublikatid=list(set(dublikatid))
    for palk in dublikatid:
        n=p.count(palk)
        k=-1
        print(f"{palk} saavad kätte järgmised inimesed: ")
        for j in range (n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(nimi)

def imja(i:list,p:list):
    nimi=input("Kelle palk tahad leia? \n")
    while nimi not in i:
        nimi=input("Palun kirjuta õige nimi \n")
    n=i.count(nimi)
    if n!=1:
        print(f'Siin on mõned inimesed kes nimi on {nimi} \n')
        kopia=i.copy()
        for j in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,'')
            print(f'{j+1} {nimi} saab {p[ind]} \n')
    else:
        ind=i.index(nimi)
        print(f'{nimi} saab {p[ind]} \n')
    return i,p

def disp(palgad, inimesed, amount, compare):
    result = []
    for i in range(len(palgad)):
        if compare == "suurim" and palgad[i] > amount:
            result.append((inimesed[i], palgad[i]))
        elif compare == "vähem" and palgad[i] < amount:
            result.append((inimesed[i], palgad[i]))
    return result

def top(i:list,p:list): 
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(min(kopia))
        print(f"{i+1} inimene - {i[ind]} saab väikse palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,max(p)+1)
    kopia=p.copy()
    for j in range(3):
        ind=kopia.index(max(kopia))
        print(f"{j+1} inimene - {i[ind]} saab suur palk: {p[ind]}")
        kopia.pop(ind)
        kopia.insert(ind,min(p)+1)

def kesk(i:list,p:list): 
    kesk=sum(p)/len(p)
    print(f"Keskmine palk on {kesk}")
    for j in range(len(i)):
        if p[j]>=kesk:
            print(f"{i[j]} saab suurem kui keskmine palk, ta saab {p[j]}")

def tulu(i:list,p:list): 
    for j in range(0,len(p)):
        if i[j]<500:
            palk=p[j]
        elif 500>=p[i]<=1200:
            palk=(p[i]-500)-(p[j]-500)*0.2
        elif 1200>p[i]>=2099:
            palk=(500-(5/9)*(p[j]-1200))-(500-(5/9)*(p[j]-1200))*0.2
        else:
            palk=p[j]*0.2
        print(f"{i[j]} on maksuvaba palk {palk}")

def sort(i:list,p:list):
    vali=input("Sorteeri nime (1) või palga järgi (2) ")
    while vali not in ["1","2"]:
        vali=input("Kirjuta ainult 1 või 2 ")
    if vali=="1":
        vali_2=input("A–Z või Z–A ").upper()
        while vali_2 not in ["A-Z","Z-A"]:
            vali_2=input("A–Z või Z–A ").upper()
        for l in range(0,len(i)):
            for o in range(0,len(i)):
                if i[l]==i[o] and l!=o:
                    for u in range(0,len(i)):
                        i[o]+=f"_{u+1}"
                        break
        kopia=i.copy()
        i.sort()
        p1=[]
        for j in range(0,len(i)):
            ind=kopia.index(i[j])
            p1.insert(j,p[ind])
        p=p1
        if vali_2=="Z-A":
            i.reverse()
            p.reverse()
    else:
        for l in range(0,len(i)):
            for o in range(0,len(i)):
                if p[l]<p[o]:
                    abi=p[l]
                    p[l]=p[o]
                    p[o]=abi
                    abi=i[l]
                    i[l]=i[o]
                    i[o]=abi
        vali_2=input("Kasvav või kahanev järjekord ").title()
        while vali_2 not in ["Kasvav","Kahanev"]:
            vali_2=input("Kasvav või kahanev! ").title()
        if vali_2=="Kahanev":
            i.reverse()
            p.reverse()
    return i,p 

def Kustuta(i:list,p:list):
    kesk_palk=sum(p)/len(p)
    print(kesk_palk)
    v=int(input("palk 1-suurem,2-väiksem? "))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    else:
        for palk in p:
            if palk<kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    return i,p

def tint(i:list,p:list):

    for j in range(0,len(i)):
        i[j]=i[j].title()
        p[j]=round(p[j],1) 
        p[j]=int(p[j])
    return i,p

def year(i:list,p:list):
    T = int(input('Mitu aastat? '))
    for j in range(len(p)):
        p[j] = p[j] * 1.05 ** T
    return i,p

def vahetanimikolmandale(lst):
    for i in range(2, len(lst), 3):
        uusnimi = input(f"Millise nimele vahetada {lst[i]}? ")
        lst[i] = uusnimi
    return lst

def boonus(i:list,p:list):
    T = int(input('Palju boonus on? '))
    for j in range(len(p)):
        p[j] = p[j] + T
    return i,p


def Kustuta(i:list,p:list):
    kesk_palk=sum(p)/len(p)
    print(kesk_palk)
    v=int(input("palk 1-suurem,2-väiksem? "))
    if v==1:
        for palk in p:
            if palk>kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    else:
        for palk in p:
            if palk<kesk_palk:
                ind=p.index(palk)
                p.remove(palk)
                i.pop(ind)
    return i,p

 