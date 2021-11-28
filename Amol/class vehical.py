class vehical:
  def __init__(a,milage,cost):
     a.milage=milage
     a.cost=cost 
  def show_vehical_details(a):
     print("milage of vehical is :-",a.milage)
     print("cost of vehical :-",a.cost)
     print("i am bmw")
x=float(input("Enter milage of vehical"))
y=float(input("enter cost of vehical"))
v1=vehical(x,y)
v1.show_vehical_details()
class car(vehical):
    def show_car_detail(a):
        print("i am car")
c1=car(x,y)
c1=Show_car_detail()