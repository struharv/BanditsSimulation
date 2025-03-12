#set term png size 1500,600
#set output 'summary.png'
set terminal pdfcairo size 5,3
set output 'output.pdf'

set title 'Deployment Comparison'
COLOR0='#99ffff'
COLOR1='#4671d5'
COLOR2='#ff0000'
COLOR3='#f36e00'
COLOR4='#f36e00'
COLOR5='#f36e00'
COLOR6='#f36e00'


set auto x
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set xtic scale 0
set ylabel 'Average Cumulative reward '
set xlabel 'Scenario'

plot 'summary.dat' using 2:xtic(1) ti col fc rgb COLOR0, 'summary.dat' using 3:xtic(1) ti col fc rgb COLOR1, 'summary.dat' using 4:xtic(1) ti col fc rgb COLOR2, 'summary.dat' using 5:xtic(1) ti col fc rgb COLOR3
