set terminal pdfcairo size 5,8
set output 'Bandit experiment.pdf'
set key left top
set multiplot layout 7, 1 title "Bandit experiment" font ",20"
set yrange [0:1]
set xrange [0:345600]
set format x " " 
set offsets graph 0, 0, 0.05, 0.05
set title 'Green Energy, Performance nodeES'
plot 'nodeES.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'nodeES_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance nodePT'
plot 'nodePT.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'nodePT_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance nodeUS'
plot 'nodeUS.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'nodeUS_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance nodeFR'
plot 'nodeFR.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'nodeFR_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance nodeHU'
plot 'nodeHU.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'nodeHU_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set ylabel ' '
set yrange[0:*]
set title 'Reward'
plot 'reward.pts'  with points pointtype 0 title "reward"
set title 'Cumulative reward'
set yrange [0:*]
set xlabel 'time'
plot 'reward_cummulative.pts' with lines linestyle 1 title "cumulative reward"
unset multiplot
