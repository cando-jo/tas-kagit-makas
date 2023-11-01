import time
import random
oyuncu_puani = 0
bilgisayar_puani = 0
while True:
    oyuncu = input("taş,kağıt,makas mı?")
    if oyuncu == "taş" or oyuncu == "kağıt" or oyuncu == "makas": 
        bilgisayar = random.randint(1, 3)
        if bilgisayar == 1:
            bilgisayar = "taş"
            
        elif bilgisayar == 2:
            bilgisayar = "kağıt"
            
        elif bilgisayar == 3:
            bilgisayar = "makas"
            
        if oyuncu == bilgisayar:
            print("Berabere")
            time.sleep(2)
            
        elif (oyuncu == "taş" and bilgisayar == "makas") or (oyuncu == 'kağıt' and bilgisayar == 'taş') or (oyuncu == 'makas' and bilgisayar == 'kağıt'):
            oyuncu_puani = oyuncu_puani + 1
            print("Tebrikler! Kazandın :D")
        
        else:
            bilgisayar_puani = bilgisayar_puani + 1
            print("Kaybettin! Noob :(")
            
        print("Bilgisayar seçimi:", bilgisayar)
        
    else:
        print("Lütfen tekrar seçenek yapınız...")
        
    print("Bilgisayar:", bilgisayar_puani)
    print("Oyuncu:", oyuncu_puani)
    time.sleep(4)
        
        
        
