set margins 10,10,0,0
# unset xtics

set multiplot layout 4,1 title "Overall title" font ",50" offset 0,-1 right
  set yrange [0:1]
  plot 'node1.pts' with linespoints linestyle 1
  plot x**2
  plot x**2
  plot x**3
unset multiplot