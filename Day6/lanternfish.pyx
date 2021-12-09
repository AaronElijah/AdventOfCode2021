#cython: language_level=3

def get_initial_fish():
    initial_fish = []
    with open("input.txt", 'r') as f:
        for fish in f.readline().split(','):
            initial_fish.append(int(fish))
    return initial_fish

# another optimization is to have a list of the number of each fish_life to keep track of what is present
# I've just been quite lazy and I'm only doing the cache optimization here 
def simulate(int initial, int days):
    cdef int day_count = 0
    fishes = [initial]
    while day_count < days:
        day_count += 1
        new_fish = []
        for index, fish in enumerate(fishes):
            if fish == 0:
                fishes[index] = 6
                new_fish.append(8)
            else:
                fishes[index] = fishes[index]-1
        fishes += new_fish
    print(len(fishes))
    return len(fishes)

def solution():
    initial_fish = get_initial_fish()
    
    # map of initial life to fish to how many extra fish that fish creates
    fish_production = {
        1: None,
        2: None,
        3: None,
        4: None,
        5: None,
    }
    for key in fish_production.keys():
        fish_production[key] = simulate(key, 256)
    total = 0
    for fish_life in initial_fish:
        total += fish_production[fish_life]
    print(total)

if __name__ == "__main__":
    solution()