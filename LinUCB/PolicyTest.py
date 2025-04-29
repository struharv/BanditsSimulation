import unittest


from matplotlib import pyplot as plt


class MyTestCase(unittest.TestCase):
    def test_best_schedule_CPU(self):
        self.do_test("data/best_schedule_CPU.txt", "data/best_schedule_CPU_test.txt")


    def test_best_schedule_big_CPU(self):
        self.do_test("data/best_schedule_big_CPU.txt", "data/best_schedule_big_CPU_test.txt", K_arms=30, context_size=30)

    #def test_best_schedule_CPU_fraction(self):
    #    self.do_test("data/best_schedule_CPU_fractions.txt", "data/best_schedule_CPU_fractions_test.txt")

    def test_best_schedule_big_CPU_fraction(self):
        self.do_test("data/best_schedule_big_CPU_fractions.txt", "data/best_schedule_big_CPU_fractions_test.txt", K_arms=30, context_size=30)

    ###
    def test_max_schedule_CPU(self):
        self.do_test("data/max_schedule_CPU_fractions.txt", "data/max_schedule_CPU_fractions_test.txt")

    def test_max_schedule_big_CPU_fraction(self):
        self.do_test("data/max_schedule_big_CPU_fractions.txt", "data/max_schedule_big_CPU_fractions_test.txt", K_arms=30, context_size=30)

    def test_max_schedule_big_CPU_fraction_300000(self):
        self.do_test("data/max_schedule_big_CPU_fractions_300000.txt", "data/max_schedule_big_CPU_fractions_test_300000.txt", K_arms=30, context_size=30)

    def do_test(self, data_path, data_path_test, K_arms=5, context_size=5, verbose=False):
        alpha_input = 1.5

        simulator = PolicySimulator()
        aligned_time_steps, cum_rewards, aligned_ctr, policy = simulator.learn(K_arms=K_arms, context_size=context_size, alpha=alpha_input,
                                                                               data_path=data_path)
        attempts = 0
        success = 0
        with open(data_path_test, "r") as f:
            for line_data in f:
                line_data=line_data.strip()

                correct_arm = int(line_data.split(" ")[0])
                covariate_string_list = line_data.split(" ")[2:]

                data_x_array = [float(covariate_elem) for covariate_elem in covariate_string_list]

                guess = simulator.guess(data_x_array)

                if verbose:
                    print(line_data, covariate_string_list, correct_arm, guess)

                cnt_better = 0
                value = 1-data_x_array[guess]
                s_values = sorted(data_x_array)
                for i in s_values:
                    if value < i:
                        cnt_better += 1

                print(guess, correct_arm, cnt_better)



                if guess == correct_arm:
                    success += 1

                attempts += 1

        print(f"data_len:{attempts} success:{success} sucess_rate:{100*success/attempts}")
        plt.plot(aligned_ctr)
        plt.title("alpha = " + str(alpha_input))
        plt.show()

if __name__ == '__main__':
    unittest.main()
