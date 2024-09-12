from engine.Node import Node
from engine.Simulator import Simulator
from PIL import Image, ImageDraw

class Visualizer:
    NODE_WIDTH = 500
    NODE_HEIGHT = 200

    def __init__(self, simulator: Simulator):
        self.simulator = simulator

    def draw_node(self, node: Node):
        with open(f"../plots/{node.name}.pts", "w") as f:

            if len(node.green_points) > 0 and node.green_points[0][0] != 0:
                f.write("0 0\n")

            for green_point in node.green_points:
                f.write(f"{green_point[0]} {green_point[1]}\n")


            if len(node.green_points) > 0 and node.green_points[len(node.green_points)-1][0] != self.simulator.TIME_MAX:
                f.write(f"{self.simulator.TIME_MAX} 0\n")





    def draw(self):

        for node in self.simulator.nodes:
            self.draw_node(node)

        with open(f"../plots/simulationX.plt", "w") as f:
            f.write("set margins 10,10,0,0\n")
            f.write("# unset xtics\n")
            f.write("set multiplot layout 4,1 title \"Overall title\" font \",50\" offset 0,-1 right\n")
            f.write("set yrange [0:1]\n")
            f.write("plot 'node1.pts' with linespoints linestyle 1\n")
            f.write("plot x**2\n")
            f.write("plot x**2\n")
            f.write("plot x**3\n")
            f.write("unset multiplot\n")
