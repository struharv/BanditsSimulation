import random

def generate_context(context_length: int):
    res = []

    for _ in range(context_length):
        res += [random.random()]

    return res



def create(filename = "max_schedule_CPU_fractions.txt", amount = 5000, choices=5, test=False):
    with open(filename, "w") as f:
        for _ in range(amount):
            array = generate_context(choices)
            if test:
                choice_arm = min(range(len(array)), key=array.__getitem__)
            else:
                choice_arm = random.randint(0, choices - 1)

            f.write(f"{choice_arm} {1-array[choice_arm]} ")

            for i in range(choices):
                f.write(f"{array[i]} ")

            f.write("\n")


create(filename="../data/max_schedule_CPU_fractions.txt", amount = 5000, choices=5, test=False)
create(filename="../data/max_schedule_CPU_fractions_test.txt", amount = 1000, choices=5, test=True)

create(filename="../data/max_schedule_big_CPU_fractions.txt", amount = 100000, choices=30, test=False)
create(filename="../data/max_schedule_big_CPU_fractions_300000.txt", amount = 300000, choices=30, test=False)
create(filename="../data/max_schedule_big_CPU_fractions_test.txt", amount = 1000, choices=30, test=True)




