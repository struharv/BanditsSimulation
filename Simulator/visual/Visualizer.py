import os

from bandits.Simulator import Simulator
from engine.Node import Node


class Visualizer:
    NODE_WIDTH = 500
    NODE_HEIGHT = 200
    SHOW_PERFORMANCE = False
    FIGURE_WIDHT = 5
    FIGURE_HEIGHT = 8
    #OUT_TYPE = 'pngcairo'
    #OUT_FILENAME = "output.png"

    #OUT_TYPE = 'epscairo'
    #OUT_FILENAME = "output.eps"

    OUT_TYPE = 'pdfcairo'
    OUT_EXTENSION = "pdf"

    def __init__(self, simulator: Simulator, prefix: str):

        self.simulator = simulator
        self.prefix = prefix
        self.test_dir = prefix
        if not os.path.isdir(self.test_dir):
            os.mkdir(self.test_dir)

    def draw_node(self, node: Node):
        with open(f"{self.test_dir}/{node.name}.pts", "w") as f:

            if len(node.green_points) > 0 and node.green_points[0][0] != 0:
                f.write("0 0\n")

            for green_point in node.green_points:
                f.write(f"{green_point[0]} {green_point[1]}\n")

            if len(node.green_points) > 0 and node.green_points[len(node.green_points) - 1][0] != self.simulator.simulation_time_sec:
                f.write(f"{self.simulator.simulation_time_sec} 0\n")

    def draw(self, title="Bandit experiment"):

        for node in self.simulator.nodes:
            self.draw_node(node)

        self.dump_reward_history()
        self.dump_reward_cummulative()
        self.dump_events()
        self.dump_resources()

        self.make_plot(title)

    def dump_resources(self):
        for node in self.simulator.nodes:
            with open(f"{self.test_dir}/{node.name}_resources.pts", "w") as f:
                for time in range(self.simulator.simulation_time_sec):
                    f.write(
                        f"{time} {node.cpu_history[time]} {node.memory_mb_history[time]} {node.storage_mb_history[time]} {node.cpu_history[time] / node.cpu} {node.memory_mb_history[time] / node.memory_mb} {node.storage_mb_history[time] / node.storage_mb} {node.performance_history[time]}\n")

    @staticmethod
    def escape(text: str) -> str:
        return text.replace("_", "\\\\\\_")

    def make_plot(self, title, filename=None, show_rewards=True):
        if not filename:
            filename = f"{title}.{Visualizer.OUT_EXTENSION}"

        with open(f"{self.test_dir}/simulation.plt", "w") as f:
            f.write(f"set terminal {self.OUT_TYPE} size {self.FIGURE_WIDHT},{self.FIGURE_HEIGHT}\n")
            f.write(f"set output '{filename}'\n")

            f.write("set key left top\n")
            f.write(f"set multiplot layout {len(self.simulator.nodes) + (2 if show_rewards else 0) }, 1 title \"{Visualizer.escape(title)}\" font \",20\"\n")

            f.write("set yrange [0:1]\n")
            f.write(f"set xrange [0:{self.simulator.simulation_time_sec}]\n")
            f.write("set format x \" \" \n")
            f.write("set offsets graph 0, 0, 0.05, 0.05\n")

            # for each node:
            for node in self.simulator.nodes:
                f.write(f"set title 'Green Energy, Performance {node.name}'\n")

                performance = ""
                if self.SHOW_PERFORMANCE:
                    performance = f", '{node.name}_resources.pts' using 1:8 with lines linestyle 1 linecolor rgb 'gray' notitle"

                f.write(
                    f"plot '{node.name}.pts' with linespoints linestyle 1 linecolor rgb \"green\" notitle{performance}, '{node.name}_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb \"black\" notitle\n")

                #f.write(f"set title 'Resources {node.name}'\n")
                #f.write("set ylabel 'CPU %'\n")
                #f.write(f"plot '{node.name}_resources.pts' using 1:5  with points pointtype 0 linecolor rgb \"black\" title 'CPU'\n")
                #f"     '{node.name}_resources.pts' using 1:6  with points pointtype 0 linecolor rgb \"brown\" title 'memory', "
                #f"     '{node.name}_resources.pts' using 1:7  with points pointtype 0 linecolor rgb \"magenta\" title 'storage' \n")

            if show_rewards:
                f.write("set ylabel ' '\n")
                f.write("set yrange[0:*]\n")
                f.write(f"set title 'Reward'\n")
                f.write(f"plot 'reward.pts'  with points pointtype 0 title \"reward\"\n")
                f.write(f"set title 'Cumulative reward'\n")
                f.write("set yrange [0:*]\n")
                f.write("set xlabel 'time'\n")
                f.write(f"plot 'reward_cummulative.pts' with lines linestyle 1 title \"cumulative reward\"\n")

            f.write("unset multiplot\n")


    def dump_reward_cummulative(self):
        with open(f"{self.test_dir}/reward_cummulative.pts", "w") as f:
            cummulative_reward = 0
            for reward in self.simulator.reward_history:
                cummulative_reward += reward[1]
                f.write(f"{reward[0]} {cummulative_reward}\n")

    def dump_reward_history(self):
        with open(f"{self.test_dir}/reward.pts", "w") as f:
            for reward in self.simulator.reward_history:
                f.write(f"{reward[0]} {reward[1]}\n")

    def dump_events(self):
        with open(f"{self.test_dir}/events.pts", "w") as f:
            for event in self.simulator.orchestration_events:
                f.write(f"{event[0]} {event[1]} {event[2]} \n")
