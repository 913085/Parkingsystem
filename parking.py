class OurParkingSystem:
    def __init__(self,big,medium,small):
        print("\n Thise is develop by ahfaz khan ")

        self.sp=[0,big,medium,small]
    def addCar(self,CarType):
        if (self.sp[CarType] > 0):
            self.sp[CarType] -= 1
            return True
        return False



ps = OurParkingSystem(2, 0, 1)
add = input("""Please choose your 
Car Type TO Check space 
is Available Or Not!:
1 = Small =	< 130 cubic feet (3,680 l)
2 = Midsize =	130–159 cubic feet (3,680–4,500 l)
3 = Large =	≥ 160 cubic feet (4,530 l)
Choice is yours """)
i= int(add)
if (i<=3):
    if i== True:
        print("yess!, Space is available")
    else:
        print("sorry!, Space is not available")
elif (i>3):
    print("sorry, invalid input please type correct input")


    # def again():
    #     global Type_again
    #     Type_again = input("Doy you wan to again type size Please type y for YES or n for NO")
    #     if again == 'y':
    #         OurParkingSystem()
    #     else:
    #         again()
    #     if Type_again == 'y':
    #         OurParkingSystem()
    #     elif Type_again == 'n':
    #         print("Good bye")
    #     else:
    #         again()








