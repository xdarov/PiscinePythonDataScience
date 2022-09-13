#/bin/sh

if [ -z "$1" ]
    then
        FILE="../ex00/hh.json"
    else
        FILE="$1"
fi

cat $FILE | jq -r -f filter.jq > hh.csv