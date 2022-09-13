#/bin/sh

if [ -z "$1" ]
  then
    OUTPUT_FILE="./hh_positions.csv"
  else
    OUTPUT_FILE="$1"
fi

FILE_LIST=($(ls splitted/created_at_*.csv))

cat ${FILE_LIST[0]} | head -n 1 > $OUTPUT_FILE

for file in ${FILE_LIST[@]}
do
  cat $file \
    | tail -n +2 \
    >> $OUTPUT_FILE
done
