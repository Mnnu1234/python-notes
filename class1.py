class car:
    name=""
    ex_room_price=0
    third_party_price=0
    taxes=0
    def on_road_price(self):
        on_road=self.ex_road_price+self.third_party_price+self.taxes
        return on_road
car1=car()
car1.name="Alto"
car1.ex_road_price=50000
car1.third_party_price=50000
car1.taxes=20000
print(f'car 1 name :{car1.name}')
print(f'car 1 price:{car1.ex_road_price}')
#print(fcar1.third_party_price)
#print(car1.taxes)

car2=car()
car2.name="BMW"
car2.ex_road_price=600000
car2.third_party_price=6000
car2.taxes=30000
print(f'car 2 name :{car2.name}')
print(f'car 2 price:{car2.ex_road_price}')
#print(fcar1.third_party_price)
#print(car1.taxes)

