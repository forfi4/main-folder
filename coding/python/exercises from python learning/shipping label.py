# shipping label program

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
         print(f"{kwargs.get('street')}")   
         print(F"pobox num {kwargs.get('pobox')}") 
    else:
          print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('state')} {kwargs.get('city')} {kwargs.get('zip')}")


shipping_label("Dr.","spongebob","squarepants","III",state="isreal",city="tel aviv",street="123 fake street",zip="12345",pobox=1001)