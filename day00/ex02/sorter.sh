#/bin/sh

if [ -z "$1" ]
    then
        FILE="../ex01/hh.csv"
    else
        FILE="$1"
fi

cat $FILE | head -n 1 > hh_sorted.csv &&
cat $FILE | tail -n +2 | sort  >> hh_sorted.csv