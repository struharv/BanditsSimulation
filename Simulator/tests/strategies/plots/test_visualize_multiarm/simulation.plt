set terminal pngcairo enhanced font 'Times New Roman,12.0' size 1024,768
set output 'output.png
set key left top
set multiplot layout 4, 2 title "Bandit experiment" font ",20"
set yrange [0:1]
set xrange [0:86400]
set format x " " 
set ylabel 'xlabel'
set title 'Green Energy node1'
plot 'node1.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
set title 'Resources node1'
plot 'node1_resources.pts' using 1:4  with points pointtype 0 linecolor rgb "black" notitle,      'node1_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle, 
set ylabel 'xlabel'
set title 'Green Energy node2'
plot 'node2.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
set title 'Resources node2'
plot 'node2_resources.pts' using 1:4  with points pointtype 0 linecolor rgb "black" notitle,      'node2_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle, 
set ylabel 'xlabel'
set title 'Green Energy node3'
plot 'node3.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
set title 'Resources node3'
plot 'node3_resources.pts' using 1:4  with points pointtype 0 linecolor rgb "black" notitle,      'node3_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle, 
set yrange[0:*]
set title 'Reward'
plot 'reward.pts' with points pointtype 0 title "reward"
set title 'Cumulative reward'
plot 'reward_cummulative.pts' with lines linestyle 1 title "cumulative reward"
unset multiplot
