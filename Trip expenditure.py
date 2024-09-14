print("\033c")

def hotel_cost(night):
    return 2500*night

def plane_ride_cost(city):
    if city == "Sylhet":
        return 1500
    elif city == "Bandarban":
        return 1250
    elif city == "Cox":
        return 1800
    elif city == "STMartin":
        return 2375
    
    
def rental_car_cost(days):
    if days>=7 :
        return 800*days - 500
    elif days>=3 :
        return 800*days - 250
    else:
        return 800*days
    
    
def totalAmount (city, day):
    return hotel_cost(day) + plane_ride_cost(city) + rental_car_cost(day)

c = input("Where do you wanna go [Sylhet, Cox, STMartin, Bandarban]:")
d = int(input("How many days you want to stay:"))

total = totalAmount(c,d)

print()
print(f"Hotel cost for {d} days : {hotel_cost(d)}")
print(f"Rental car cost for {d} days : {rental_car_cost(d)}")
print(f"Plane ride cost for {d} days : {plane_ride_cost(c)}")
print(f"TOTAL cost for {d} days : {total} ")