def AddCar():
    print("\ncreated by ahfaz khan")
    add = input("""please type to vehicle size would you like to park :)
    Car Type TO Check space 
    is Available Or Not!:
    1 = Small =	< 130 cubic feet (3,680 l)
    2 = Midsize =	130–159 cubic feet (3,680–4,500 l)
    3 = Large =	≥ 160 cubic feet (4,530 l)
    Choice is yours:""")

    i = int(add)

    if (i <= 3):
        if i == 1 or 3:
            print("yess!, Space is available")
        else:
            print("sorry!, Space is not available")
    elif (i > 3):
        print("sorry, invalid input please type correct input")
    else:
        print("you press invalid key")
    again()
def again():
    Type_again=input('''
       Do you want to Vehicle size type again
       please type yess for 'y' and no for 'n'
       ''')

    if Type_again=='y':
        AddCar()
    elif Type_again=='n':
        print("see you later")
    else:
        again()
AddCar()