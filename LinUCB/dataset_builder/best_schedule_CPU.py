import random


def create(filename = "best_schedule_CPU.txt", amount = 5000, choices=5, test=False):
    with open(filename, "w") as f:
        for _ in range(amount):
            correct_arm = random.randint(0, choices - 1)
            if test:
                choice_arm = correct_arm
            else:
                choice_arm = random.randint(0, choices - 1)

            if correct_arm == choice_arm:
                f.write(f"{choice_arm} 1 ")
            else:
                f.write(f"{choice_arm} 0 ")

            for choice_i in range(choices):
                if choice_i == correct_arm:
                    f.write(f"0 ")
                else:
                    f.write(f"1 ")

            f.write("\n")


create(filename = "../data/best_schedule_CPU.txt", amount = 5000, choices=5, test=False)
create(filename = "../data/best_schedule_CPU_test.txt", amount = 1000, choices=5, test=True)

create(filename = "../data/best_schedule_big_CPU.txt", amount = 100000, choices=30, test=False)
create(filename = "../data/best_schedule_big_CPU_test.txt", amount = 1000, choices=30, test=True)




