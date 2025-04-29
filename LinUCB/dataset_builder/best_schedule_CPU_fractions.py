import random

def create(filename = "best_schedule_CPU_fractions.txt", amount = 5000, choices=5, test=False):
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

            for i in range(choices):
                if i == correct_arm:
                    f.write(f"0 ")
                else:
                    f.write(f"{min(1, random.random()+0.3)} ")

            f.write("\n")


create(filename="../data/best_schedule_CPU_fractions.txt", amount = 5000, choices=5, test=False)
create(filename="../data/best_schedule_CPU_fractions_test.txt", amount = 1000, choices=5, test=True)

create(filename="../data/best_schedule_big_CPU_fractions.txt", amount = 100000, choices=30, test=False)
create(filename="../data/best_schedule_big_CPU_fractions_test.txt", amount = 1000, choices=30, test=True)




