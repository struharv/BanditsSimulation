set terminal pdfcairo size 5,8
set output 'UCB Multi Armed Bandit - bigspikey_30_container_low.pdf'
set key left top
set multiplot layout 7, 1 title "Contextual Multi-Armed Bandit - Dynamic Green Energy" font ",20"
set yrange [0:1]
set xrange [0:86400]
set format x " " 
set offsets graph 0, 0, 0.05, 0.05
set title 'Node 1 - Green Energy, CPU utilization'
plot 'node1.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node1_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Node 2 - Green Energy, CPU utilization'
plot 'node2.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node2_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Node 3 - Green Energy, CPU utilization'
plot 'node3.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node3_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Node 4 - Green Energy, CPU utilization'
plot 'node4.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node4_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Node 5 - Green Energy, CPU utilization'
plot 'node5.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node5_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set ylabel ' '
set yrange[0:*]
set title 'Reward'
plot 'reward.pts'  with points pointtype 0 title "reward"
set title 'Cumulative reward'
set yrange [0:*]
set xlabel 'time'
plot 'reward_cummulative.pts' with lines linestyle 1 title "cumulative reward"
unset multiplot
