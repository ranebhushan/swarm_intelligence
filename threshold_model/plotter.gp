set term qt size 900, 300 persist raise

set xlabel "time step"
set nokey

set multiplot layout 1,3

set ylabel "task"
plot for [i=0:19] 'data.dat' every 20::i using 1:3


set ylabel "threshold 0"
plot for [i=0:19] 'data.dat' every 20::i using 1:4 with lines 


set ylabel "threshold 1"
plot for [i=0:19] 'data.dat' every 20::i using 1:5 with lines

unset multiplot