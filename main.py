import numpy as np
from PIL import Image


size = 1024
ant_position = [512, 512]
ant_direction = 0 # 0 = вверх, 1 = вправо, 2 = вниз, 3 = влево

field = np.zeros((size, size))
def move_ant(ant_position, ant_direction, field):
    x, y = ant_position

    if field[y, x] == 0:
        field[y, x] = 1
        ant_direction = (ant_direction + 1) % 4 # Поворачиваем по часовой стрелке
    else:
        field[y, x] = 0
        ant_direction = (ant_direction - 1) % 4

    if ant_direction == 0: ant_position[1] -= 1
    elif ant_direction == 1: ant_position[0] += 1
    elif ant_direction == 2: ant_position[1] += 1
    else: ant_position[0] -= 1

    return ant_position, ant_direction, field

while 0 <= ant_position[0] < size and 0 <= ant_position[1] < size:
    ant_position, ant_direction, field = move_ant(ant_position, ant_direction, field)


image = Image.fromarray(np.uint8((1-field)*255))
image.save('ant_path.png')

black_cells = np.sum(field)

print("Число черных клеток на пути муравья:", int(black_cells))
