hour=int(input("enter the hour the vechile parked;"))
charge=2 if hour<=5 else(2+(hour-5)*1.5)
print(f"parking charge:{charge}")
