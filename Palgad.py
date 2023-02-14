from module1 import *
palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","f"]
while True:
    print(inimesed)
    print(palgad)
    menu=int(input("Valik:\n 1-lisa andmed\n2=Kustuta andmed\n3=Suurim palk\n4=Lühim palk\n5=Sorteerimine\n6=Võrdsed palgad\n7-otsi palka inimese nime järgi\n8-sisestatud palga põhjal kuvab inimeste madalamad ja kõrgemad palgad\n9-Leia top 3 vähem või rohkem\n10-Otsi keskmine palk ja kes on saada suurem\n11-Otsi maksuvaba palk\n12-Sort\n13-Otsige kes teenivad alla keskmise palga ja emalda nad\n14-Teeb nimekiri\n15-saate teada 5% tõusuga töötaja töötasu T-aastas\n16-Vaheta nimi kolmandale\n17 Boonus\n"))
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
        iniemsed,palgad=imja(inimesed,palgad)
    elif menu==8:
        amount = int(input("Sisestage summa, millega võrrelda: "))
        more_than = disp(palgad, inimesed, amount, "suurim")
        less_than = disp(palgad, inimesed, amount, "vähem")
        print(f"Inimesed, kellel on palk rohkem kui {amount}:", more_than)
        print(f"Inimesed, kelle palk on väiksem kui {amount}:", less_than)
    elif menu==9:
        top(inimesed,palgad)
    elif menu==10:
        kesk(inimesed,palgad)
    elif menu==11:
        tulu(inimesed,palgad)
    elif menu==12:
        inimesed,palgad=sort(inimesed,palgad)
    elif menu==13:
        inimesed,palgad=Kustuta(inimesed,palgad)
    elif menu==14:
        inimesed,palgad=tint(inimesed,palgad)
    elif menu==15:
        inimesed,palgad=year(inimesed,palgad)
    elif menu==16:
        inimesed=vahetanimikolmandale(inimesed)
    elif menu==17:
        inimesed,palgad=boonus(inimesed,palgad)
    else:
        print("Kirjuta õige arv")