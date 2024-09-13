set margins 10,10,0,0
set key left top
set multiplot layout 5,1 title "Bandit experiment" font ",20"
set yrange [0:1]
set xrange [0:1440]
plot 'MultiArmBandit-uniform_node1.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
plot 'MultiArmBandit-uniform_node2.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
plot 'MultiArmBandit-uniform_node3.pts' with linespoints linestyle 1 linecolor rgb "green" notitle
set yrange[0:*]
plot 'MultiArmBandit-uniform_reward.pts' with points pointtype 0 title "reward"
plot 'MultiArmBandit-uniform_reward_cummulative.pts' with lines linestyle 1 title "cummulative reward"
unset multiplot
