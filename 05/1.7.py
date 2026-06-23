from collections import namedtuple


plane_1 = ("Boeing 747", 400, 1999, "AER-1234")
plane_2 = ("Airbus A80", 380, 1897, "AER-5678")
plane_3 = ("Cessna 172", 4, 2005, "AER-9012")
plane_4 = ("Embraer E195", 120, 2004, "AER-3456")

new_park = []
for plane in [plane_1, plane_2, plane_3, plane_4]:
    if plane[2] > 300:
        new_park.append(plane)

print(new_park)

# Plane = namedtuple("Plane", "name sits year reg_number")
Plane = namedtuple('Plane', ['name', 'sits', 'year', 'reg_number'])  #можна робити і так, різниці не має

plane_new_1 = Plane("Boeing 747", 400, 1999, "AER-1234")
plane_new_2 = Plane("Airbus A80", 380, 1897, "AER-5678")
plane_new_3 = Plane("Cessna 172", 4, 2005, "AER-9012")
plane_new_4 = Plane("Embraer E195", 120, 2004, "AER-3456")

new_park_2 = []
for plane in [plane_new_1, plane_new_2, plane_new_3, plane_new_4]:
    #if plane[1] > 300:
    if plane.sits > 300:  #стукаємось до sits і нам видає лише ті літаки, де місць більше ніж 300
        new_park_2.append(plane)

print(new_park_2)
