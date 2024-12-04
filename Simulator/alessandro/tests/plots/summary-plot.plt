set term png size 1500,600
set output "summary-plot.png"

set title "Benchmarks - External sources"
C = "#99ffff"; Cpp = "#4671d5"; Java = "#ff0000"; Python = "#f36e00"
set auto x

#set yrange [0:730]

set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
set xtic scale 0
set ylabel "Build Time [s]"
# 2, 3, 4, 5 are the indexes of the columns; 'fc' stands for 'fillcolor'

plot 'summary.dat' using 2:xtic(1) ti col fc rgb C, '' u 3 ti col fc rgb Cpp, '' u 4 ti col fc rgb Java