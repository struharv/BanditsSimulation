import random

import numpy as np
import matplotlib.pyplot as plt



# Create class object for a single linear ucb disjoint arm
class linucb_disjoint_arm():

    def __init__(self, arm_index: int, d: int, alpha: float):
        # Track arm index
        self.arm_index = arm_index

        # Keep track of alpha
        self.alpha = alpha

        # A: (d x d) matrix = D_a.T * D_a + I_d.
        # The inverse of A is used in ridge regression
        self.A = np.identity(d)

        # b: (d x 1) corresponding response vector.
        # Equals to D_a.T * c_a in ridge regression formulation
        self.b = np.zeros([d, 1])

    def calc_UCB(self, x_array):
        # Find A inverse for ridge regression
        A_inv = np.linalg.inv(self.A)

        # Perform ridge regression to obtain estimate of covariate coefficients theta
        # theta is (d x 1) dimension vector
        self.theta = np.dot(A_inv, self.b)

        # Reshape covariates input into (d x 1) shape vector
        x = x_array.reshape([-1, 1])

        # Find ucb based on p formulation (mean + std_dev)
        # p is (1 x 1) dimension vector
        p = np.dot(self.theta.T, x) + self.alpha * np.sqrt(np.dot(x.T, np.dot(A_inv, x)))

        return p

    def reward_update(self, reward, x_array):
        # Reshape covariates input into (d x 1) shape vector
        x = x_array.reshape([-1, 1])

        # Update A which is (d * d) matrix.
        self.A += np.dot(x, x.T)

        # Update b which is (d x 1) vector
        # reward is scalar
        self.b += reward * x


class linucb_policy():

    def __init__(self, K_arms, d, alpha):
        self.K_arms = K_arms
        self.linucb_arms = [linucb_disjoint_arm(arm_index=i, d=d, alpha=alpha) for i in range(K_arms)]

    def select_arm(self, x_array):
        # Initiate ucb to be 0
        highest_ucb = -1

        # Track index of arms to be selected on if they have the max UCB.
        candidate_arms = []

        for arm_index in range(self.K_arms):
            # Calculate ucb based on each arm using current covariates at time t
            arm_ucb = self.linucb_arms[arm_index].calc_UCB(x_array)

            # If current arm is highest than current highest_ucb
            if arm_ucb > highest_ucb:
                # Set new max ucb
                highest_ucb = arm_ucb

                # Reset candidate_arms list with new entry based on current arm
                candidate_arms = [arm_index]

            # If there is a tie, append to candidate_arms
            if arm_ucb == highest_ucb:
                candidate_arms.append(arm_index)

        # Choose based on candidate_arms randomly (tie breaker)
        chosen_arm = np.random.choice(candidate_arms)

        return chosen_arm


class ContextSimulator:
    def __init__(self, simulator: Simulator):
        self.simulator = simulator

    def guess(self, array):
        return self.linucb_policy_object.select_arm(np.array(array))

    def learnx(self, K_arms: int, context_size: int, alpha: float):
        # Initiate policy
        self.linucb_policy_object = linucb_policy(K_arms=K_arms, d=context_size, alpha=alpha)

        # Instantiate trackers
        aligned_time_steps = 0
        cumulative_rewards = 0
        aligned_ctr = []
        unaligned_ctr = []  # for unaligned time steps

        for i in range(10):

            worst_node = self.worst_node_with_container()
            worst_container = None
            if worst_node and len(worst_node.containers) > 0:
                worst_container = random.choice(worst_node.containers)

            context = self.simulator.make_context(0)
            print(context)

            data_x_array = np.array(context)
            arm_index = self.linucb_policy_object.select_arm(data_x_array)
            print("arm:", arm_index)
            if worst_container:
                self.simulator.migrate(worst_container.name, self.simulator.nodes[arm_index].name)
                print("migration")

            reward = self.simulator.compute_reward()
            print("reward:", reward)
            self.linucb_policy_object.linucb_arms[arm_index].reward_update(reward, data_x_array)
            aligned_time_steps += 1
            cumulative_rewards += reward
            aligned_ctr += [cumulative_rewards / aligned_time_steps]

            self.simulator.inc_time()
            """
            
            if arm_index == data_arm:
                # Use reward information for the chosen arm to update
                self.linucb_policy_object.linucb_arms[arm_index].reward_update(data_reward, data_x_array)

                # For CTR calculation
                aligned_time_steps += 1
                cumulative_rewards += data_reward
                aligned_ctr += [cumulative_rewards / aligned_time_steps]
            """
        return (aligned_time_steps, cumulative_rewards, aligned_ctr, self.linucb_policy_object)



    def learn(self, K_arms: int, context_size: int, alpha: float, data_path: str):
        # Initiate policy
        self.linucb_policy_object = linucb_policy(K_arms=K_arms, d=context_size, alpha=alpha)

        # Instantiate trackers
        aligned_time_steps = 0
        cumulative_rewards = 0
        aligned_ctr = []
        unaligned_ctr = []  # for unaligned time steps
        cnt = 0
        # Open data
        with open(data_path, "r") as f:

            for line_data in f:
                if cnt % 1000 == 0:
                    print(f"{cnt}")
                cnt += 1
                # 1st column: Logged data arm.
                # Integer data type
                splitted = line_data.strip().split()
                data_arm = int(splitted[0])

                # 2nd column: Logged data reward for logged chosen arm
                # Float data type
                data_reward = float(splitted[1])

                # 3rd columns onwards: 100 covariates. Keep in array of dimensions (100,) with float data type
                covariate_string_list = splitted[2:]
                data_x_array = np.array([float(covariate_elem) for covariate_elem in covariate_string_list])

                # Find policy's chosen arm based on input covariates at current time step
                arm_index = self.linucb_policy_object.select_arm(data_x_array)

                # Check if arm_index is the same as data_arm (ie same actions were chosen)
                # Note that data_arms index range from 1 to 10 while policy arms index range from 0 to 9.
                if arm_index == data_arm:

                    # Use reward information for the chosen arm to update
                    self.linucb_policy_object.linucb_arms[arm_index].reward_update(data_reward, data_x_array)

                    # For CTR calculation
                    aligned_time_steps += 1
                    cumulative_rewards += data_reward
                    aligned_ctr += [cumulative_rewards / aligned_time_steps]

        return (aligned_time_steps, cumulative_rewards, aligned_ctr, self.linucb_policy_object)

    def worst_node_with_container(self) -> Node:
        result_node = None
        minEnergy = None
        shuffled = []

        for node in self.simulator.nodes:
            if len(node.containers) > 0:
                shuffled += [node]

        random.shuffle(shuffled)

        for node in shuffled:
            energy = node.green_at(self.simulator.now())
            if result_node == None or energy < minEnergy:
                result_node = node
                minEnergy = energy

        return result_node



if __name__ == '__main__':

    #simulator = PolicySimulator()
    #aligned_time_steps, cum_rewards, aligned_ctr, policy = simulator.learn(K_arms=5, context_size=5, alpha=alpha_input, data_path=data_path)
    """
    for test_case in [([0, 1, 1, 1, 1], 0),
                      ([1, 0, 1, 1, 1], 1),
                      ([1, 1, 0, 1, 1], 2),
                      ([1, 1, 1, 0, 1], 3),
                      ([1, 1, 1, 1, 0], 4)]:
        print(test_case[0], test_case[1], simulator.guess(test_case[0]))
    
    """



    #plt.plot(aligned_ctr)
    #plt.title("alpha = "+str(alpha_input))
    #plt.show()
