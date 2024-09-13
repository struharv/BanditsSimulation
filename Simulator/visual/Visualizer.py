from engine.Node import Node
from engine.Simulator import Simulator
from PIL import Image, ImageDraw

class Visualizer:
    NODE_WIDTH = 500
    NODE_HEIGHT = 200

    def __init__(self, simulator: Simulator, prefix = ""):
        self.simulator = simulator
        self.prefix = prefix

    def draw_node(self, node: Node):
        with open(f"../plots/{self.prefix}{node.name}.pts", "w") as f:

            if len(node.green_points) > 0 and node.green_points[0][0] != 0:
                f.write("0 0\n")

            for green_point in node.green_points:
                f.write(f"{green_point[0]} {green_point[1]}\n")


            if len(node.green_points) > 0 and node.green_points[len(node.green_points)-1][0] != self.simulator.TIME_MAX:
                f.write(f"{self.simulator.TIME_MAX} 0\n")


    def draw(self, title="Bandit experiment" ):

        for node in self.simulator.nodes:
            self.draw_node(node)

        with open(f"../plots/{self.prefix}reward.pts", "w") as f:
            for reward in self.simulator.reward_history:
                f.write(f"{reward[0]} {reward[1]}\n")

        with open(f"../plots/{self.prefix}reward_cummulative.pts", "w") as f:
            cummulative_reward = 0
            for reward in self.simulator.reward_history:
                cummulative_reward += reward[1]
                f.write(f"{reward[0]} {cummulative_reward}\n")

        with open(f"../plots/{self.prefix}simulation.plt", "w") as f:
            f.write("set margins 10,10,0,0\n")
            f.write("set key left top\n")
            f.write(f"set multiplot layout {len(self.simulator.nodes)+2},1 title \"{title}\" font \",20\"\n")

            f.write("set yrange [0:1]\n")
            f.write(f"set xrange [0:{Simulator.TIME_MAX}]\n")

            for node in self.simulator.nodes:
                f.write(f"plot '{self.prefix}{node.name}.pts' with linespoints linestyle 1 linecolor rgb \"green\" notitle\n")

            f.write("set yrange[0:*]\n")
            f.write(f"plot '{self.prefix}reward.pts' with points pointtype 0 title \"reward\"\n")
            f.write(f"plot '{self.prefix}reward_cummulative.pts' with lines linestyle 1 title \"cummulative reward\"\n")
            f.write("unset multiplot\n")


