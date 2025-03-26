set terminal pdfcairo size 5,8
set output 'Bandit experiment.pdf'
set key left top
set multiplot layout 3, 1 title "Bandit experiment" font ",20"
set yrange [0:1]
set xrange [0:86400]
set format x " " 
set offsets graph 0, 0, 0.05, 0.05
set title 'Green Energy, Performance node1'
plot 'node1.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node1_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance node2'
plot 'node2.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node2_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
set title 'Green Energy, Performance node3'
plot 'node3.pts' with linespoints linestyle 1 linecolor rgb "green" notitle, 'node3_resources.pts' using 1:($5 == 0 ? NaN:$5)   with points pointtype 0 linecolor rgb "black" notitle
unset multiplot
