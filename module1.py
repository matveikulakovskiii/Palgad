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

def lepani(i:list,p:list):
    nimi=input("Kelle palk tahad leia? ").title()
    while nimi not in i:
        nimi = input("Palun kirjutage õige nimi: ").title
    n=i.count(nimi)
    if n!=1:
        print(f"Siis in mõned inimesed kes nimi on {nimi}")
        kopia=i.copy()
        for i in range(n):
            ind=kopia.index(nimi)
            kopia.remove(nimi)
            kopia.insert(ind,"")
            print(f"{i+1} {nimi} saab {p[ind]}")
    else:
        ind=i.index(nimi)
        print(f"{nimi} saab {p[ind]}")

def Sorteerimine(i:list,p:list):

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

 