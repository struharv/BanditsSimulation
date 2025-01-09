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
                for iter_value in values:
                    results = iter_value[1]
                    summ += results["cumulative reward"]

                f.write(f"{test_name},{case},cumulative reward,{summ}\n")


class StatsCombiner:
    def __init__(self):
        self.db = []

    def compose(self, file_name, cases=["still", "spikey", "bigspikey"]):
        with open(file_name, "w") as f:
            f.write("Title ")
            for column in self.get_test_cases():
                f.write(f"\"{column.replace("_", "\\\\\\_")}\" ")
            f.write("\n")

            for case in cases:
                f.write(f"{case} ")

                #values = ""
                for item in self.db:
                    if case == item[1]:
                        print(item)
                        #values += f"{item[3]} "
                        f.write(f"{item[3]} ")

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


if __name__ == "__main__":
    combiner = StatsCombiner()

    combiner.add_file("../plots/test_random_summary.csv")
    combiner.add_file("../plots/test_naive_bandit_summary.csv")
    combiner.add_file("../plots/test_UCB_bandit_summary.csv")

    combiner.compose("../plots/summary.dat")
