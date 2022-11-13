from day_1 import data_reader

dive_instructions = data_reader("day_2")

dive_route = []
for instruction in dive_instructions:
    direction, speed = instruction.split(" ")
    dive_route.append((direction, int(speed)))

ship_x, ship_y = 0, 0
for route in dive_route:
    direction, speed = route
    if direction == "forward":
        ship_x += speed
    elif direction == "down":
        ship_y += speed
    elif direction == "up":
        ship_y -= speed

print(ship_x * ship_y)

ship_x, ship_y = 0, 0
aim = 0
for route in dive_route:
    direction, speed = route
    if direction == "forward":
        ship_x += speed
        ship_y += aim * speed
    elif direction == "down":
        aim += speed
    elif direction == "up":
        aim -= speed

print(ship_x * ship_y)
