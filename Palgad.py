from module1 import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","f"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-lisa andmed\n2=Kustuta andmed\n3=Suurim palk\n4=Lühim palk\n5=Sorteerimine\n6=Võrdsed palgad\n13=Kustuta\n"))
    if menu==0:
        break 
    elif menu==1:
        inimesed,palgad=lisa_andmed(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==2:
        inimesed,palgad=delete_nimi(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==3:
        palk,nimi=suurim_palk(inimesed,palgad)
        print(f"Suurim palk on {palk} {nimi}")
    elif menu==4:
        palk,nimi=luhim_palk(inimesed,palgad)
        print(f"Lühim palk on {palk} {nimi}")
    elif menu==5:
        inimesed,palgad=sorteerimine(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==6:
        inimesed,palgad=vordsed_palgad(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif menu==7:
        inimesed,palgad=lepani(inimesed,palgad)
        print(inimesed)
        print(palgad)
    elif
    elif menu==12:
        palgad,inimesed=Sorteerimine(palgad,inimesed)
        print(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=Kustuta(inimesed,palgad)
        print(inimesed,palgad)