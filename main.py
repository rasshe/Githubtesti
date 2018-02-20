from Car import car

def Test():
    i=0
    
    print("Test Start Toinen")
    
    while i<=100:
        print(i, ". Test Toinen")
        i=i+1
        
    print("Test Done Toinen")
    
    
    
def main():
    Test()
    uus = car("Olaa", 20)
    print("|----------------|")
    print(uus.get_col)
    print("|----------------|")
    print(uus.get_txt)
    print("|----------------|")
    
    
main()