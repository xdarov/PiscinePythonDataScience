#! /bin/bash
# @ Pies,Bars
# 2007    73.32   70.52
# 2008    81.23  93
# 2009    181.43   135.10
# 2010    110.21   95
# 2011    93.97  90.45

pip3 install termgraph > /dev/null 2> /dev/null
termgraph temp.dat --color {blue,magenta} --width 90

