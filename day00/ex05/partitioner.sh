#/bin/sh

if [ -z "$1" ]
  then
    FILE="../ex03/hh_positions.csv"
  else
    FILE="$1"
fi
OUTPUT_FILE_EXTENTION=".csv"

UNIQUE_DATES=$(cat $FILE \
                | tail -n +2 \
                | awk 'BEGIN{FS=",\""} {split($2, result, "T"); print result[1];}' \
                | sort \
                | uniq \
              )

mkdir -p splitted
for date in $UNIQUE_DATES
do
  CURRENT_FILE="splitted/created_at_$date.csv"
  touch $CURRENT_FILE
  
  cat $FILE \
    | head -n 1 \
    > $CURRENT_FILE

  cat $FILE \
    | tail -n +2 \
    | awk -v date=$date \
      'BEGIN{FS=OFS=","}
      {
        i = index($2, date);
        if (i > 0)
        {
          print $0;
        }
      }' \
    >> $CURRENT_FILE
done