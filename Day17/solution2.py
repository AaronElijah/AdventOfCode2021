from typing import Tuple

def get_landing_zone() -> Tuple[Tuple[int, int], Tuple[int, int]]:
    with open("Day17/input.txt", 'r') as f:
        for line in f.read().splitlines():
            zones = line.split("target area: ")[1].split(", ")
            zones = tuple(tuple(map(lambda x: int(x), zones[i].split(axis)[1].split(".."))) for i, axis in enumerate(("x=", "y=")))
    return zones


def is_in_range(position: Tuple[int, int], x_max: int, y_min: int) -> bool:
    return position[0] <= x_max and position[1] >= y_min


def is_in_zone(position: Tuple[int, int], zone: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
    (x_min, x_max), (y_min, y_max) = zone
    return position[0] <= x_max and position[0] >= x_min and position[1] >= y_min and position[1] <= y_max

if __name__ == "__main__":
    (x_min, x_max), (y_min, y_max) = get_landing_zone()
    x_pos, y_pos, x_vel_cur, y_vel_cur, n = 0, 0, 0, 0, 0
    max_vel = 400
    starting_velocities = []
    for x_vel_start in range(1, max_vel):
        x_vel_cur = x_vel_start
        for y_vel_start in range(-max_vel, max_vel):
            y_vel_cur = y_vel_start         
            while is_in_range(position=(x_pos, y_pos), x_max=x_max, y_min=y_min):
                n += 1
                x_pos += x_vel_cur
                y_pos += y_vel_cur
                if x_vel_cur < 0:
                    x_vel_cur += 1
                elif x_vel_cur > 0:
                    x_vel_cur -= 1
                y_vel_cur -= 1
                if is_in_zone(position=(x_pos, y_pos), zone=((x_min, x_max), (y_min, y_max))):
                    print(x_vel_start, y_vel_start)
                    starting_velocities.append((x_vel_start, y_vel_start))
                    break
            # moved out of range, not valid velocity
            x_pos, y_pos, x_vel_cur, y_vel_cur, n = 0, 0, x_vel_start, 0, 0
    print(len(starting_velocities))