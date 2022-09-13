#/bin/sh

if [ -z "$1" ]
  then
    FILE="../ex03/hh_positions.csv"
  else
    FILE="$1"
fi

echo '"name","count"' > hh_uniq_positions.csv

cat $FILE | awk 'BEGIN{FS=OFS=",";} NR>1 {print $3;}' | sort | uniq -c | awk 'BEGIN{OFS=","} {print $2, $1;}' >> hh_uniq_positions.csv