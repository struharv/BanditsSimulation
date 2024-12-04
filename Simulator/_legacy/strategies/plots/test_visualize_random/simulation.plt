set margins 10,10,0,0
set key left top
set multiplot layout 5, 2 title "Bandit experiment" font ",20"
set yrange [0:1]
set xrange [0:86400]
plot 'node1.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
plot 'node1_resources.pts' using 1:4  with points pointtype 0 linecolor rgb "black" notitle,      'node1_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle, 
plot 'node2.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
plot 'node2_resources.pts' using 1:4  with points pointtype 0 linecolor rgb "black" notitle,      'node2_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle, 
plot 'node3.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
plot 'node3_resources.pts' using 1:4  with points pointtype 0 linecolor rgb "black" notitle,      'node3_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle, 
set yrange[0:*]
plot 'reward.pts' with points pointtype 0 title "reward"
plot 'reward_cummulative.pts' with lines linestyle 1 title "cummulative reward"
unset multiplot
