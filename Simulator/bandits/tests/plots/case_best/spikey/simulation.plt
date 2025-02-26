set terminal pngcairo enhanced font 'Times New Roman,12.0' size 800,1000
set output 'output.png
set key left top
set multiplot layout 5, 1 title "Best Reschedule - spikey" font ",20"
set yrange [0:1]
set xrange [0:86400]
set format x " " 
set offsets graph 0, 0, 0.05, 0.05
set title 'Green Energy, Performance node1'
plot 'node1.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node1_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance node2'
plot 'node2.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node2_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance node3'
plot 'node3.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node3_resources.pts' using 1:5  with points pointtype 0 linecolor rgb "black" notitle
set ylabel ' '
set yrange[0:*]
set title 'Reward'
plot 'reward.pts'  with points pointtype 0 title "reward"
set title 'Cumulative reward'
set yrange [0:*]
plot 'reward_cummulative.pts' with lines linestyle 1 title "cumulative reward"
unset multiplot
