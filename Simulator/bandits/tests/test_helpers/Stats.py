class Stats:

    def __init__(self):
        self.result_storage = {}

    def add_result(self, test_name, case, instance, results):
        key = f"{test_name}:{case}"

        if key not in self.result_storage:
            self.result_storage[key] = []

        self.result_storage[key] += [[instance, results]]

    def export_raw(self, file_name):
        with (open(file_name, "w") as f):
            for key, values in self.result_storage.items():
                split = key.split(":")
                test_name = split[0]
                case = split[1]
                for iter_value in values:
                    instance = iter_value[0]
                    results: dict = iter_value[1]

                    summary = ""
                    for k, v in results.items():
                        summary = f"{k},{v},"

                    f.write(f"{test_name},{case},{instance},{summary}\n")

    def export_summary(self, file_name):
        with (open(file_name, "w") as f):
            for key, values in self.result_storage.items():
                split = key.split(":")
                test_name = split[0]
                case = split[1]

                summ = 0
                occurences = 0
                for iter_value in values:
                    results = iter_value[1]
                    occurences += 1
                    summ += results["cumulative reward"]

                f.write(f"{test_name},{case},cumulative reward,{summ/occurences}\n")


class StatsCombiner:
    def __init__(self):
        self.db = []

    def compose(self, file_name, cases=["still_3_container", "increasing_5_container", "extreme_still", "spikey", "bigspikey"]):
        with open(f"{file_name}.dat", "w") as f:
            f.write("Title ")
            for column in self.get_test_cases():
                f.write(f"\"{column.replace("_", "\\\\\\_")}\" ")
            f.write("\n")

            for case in cases:
                f.write(f"{case.replace("_", "\\\\\\_")} ")

                #values = ""
                for item in self.db:
                    if case == item[1]:
                        print(item)
                        #values += f"{item[3]} "
                        f.write(f"{item[3]} ")

                f.write("\n")

        self.write_plt(file_name)

    def write_plt(self, file_name):
        with open(f"{file_name}.plt", "w") as f:
            f.write("set term png size 1500,600\n"
                    f"set output 'summary.png'\n")

            f.write(f"set title 'Deployment Comparison'\n")
            colors = ["#99ffff", "#4671d5", "#ff0000", "#f36e00", "#f36e00", "#f36e00", "#f36e00"]
            for i in range(len(colors)):
                f.write(f"COLOR{i}='{colors[i]}'\n")

            f.write(f"\n\nset auto x\n"
                    f"set style data histogram\n"
                    f"set style histogram cluster gap 1\n"
                    f"set style fill solid border -1\n"
                    f"set boxwidth 0.9\n"
                    f"set xtic scale 0\n"
                    f"set ylabel 'Average Cumulative reward '\n"
                    f"set xlabel 'Scenario'\n\n")


            f.write(f"plot ")
            for i in range(len(self.get_test_cases())):
                f.write(f"'summary.dat' using {i+2}:xtic(1) ti col fc rgb COLOR{i}")
                if i < len(self.get_test_cases())-1:
                    f.write(", ")

            f.write("\n")

    def get_test_cases(self):
        columns = []

        for item in self.db:
            case = item[0]
            if case not in columns:
                columns += [case]

        return columns

    def add_file(self, file_name):
        with open(file_name, "r") as f:
            for line in f:
                splitted = line.strip().split(",")
                self.db += [splitted]

def combine(dir):
    combiner = StatsCombiner()

    combiner.add_file(f"{dir}stats_test_best_summary.csv")
    combiner.add_file(f"{dir}stats_test_random_0_summary.csv")
    combiner.add_file(f"{dir}stats_test_naive_bandit_summary.csv")
    combiner.add_file(f"{dir}stats_test_UCB_bandit_summary.csv")



    #combiner.add_file(f"{dir}stats_test_UCB_bandit_1_summary.csv")
    #combiner.add_file(f"{dir}stats_test_UCB_bandit_2_summary.csv")


    combiner.compose(f"{dir}summary")


if __name__ == "__main__":
    combine("../plots/")
