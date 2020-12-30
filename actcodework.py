from work import model
mod=model()
x=input("Do you want to give optional path ? YES/NO : ")
if x.isalpha():
    x=x.lower()
    if x=='yes':
        path=input("Enter the path : ")
        mod.adddata(path)
    while True:
        print()
        print("Press 1 for create operation.")
        print("Press 2 for read operation.")
        print("Press 3 for Delete operation.")
        print("Press 4 for add all new data to existing json file.")
        print("Press 0 for exit operation.")
        print()
        n=int(input("Enter your choice : "))
        if n==1:
            key=input("Enter the key value : ")
            value=input("Enter the value corresponding to key : ")
            time=input("Do you want to add Time to live property ? YES/NO : ")
            if time.isalpha():
                time=time.lower()
                if time == 'yes':
                    try:
                        time = int(input("Enter the time in seconds : "))
                        mod.createoper(key, value, time)
                    except:
                        print("No.. Input is not a number. It's a string")
                else:
                    mod.createoper(key, value,1000)
            else:
                print("Error..You have given some wrong input..")
        elif n==2:
            key=input("Enter the key value to read : ")
            mod.read(key)
        elif n==3:
            key=input("Enter the key value to Delete : ")
            mod.deleteop(key)
        elif n==4:
            mod.makenewfile()
        elif n==0:
            print("Thank you.")
            exit()
        else:
            print("Error..wrong input..Try again..")
        print()
else:
    print("Error..You have given some wrong input..")
