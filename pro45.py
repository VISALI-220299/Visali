new=input()
if new==new[::-1]:
    print("yes")
else:
    value=new.strip("0")
    
    if value==value[::-1]:
        print("yes")
    else:
        value=new.lstrip("0")
        
        if value==value[::-1]:
            print("yes")
        else:
            print("no")
