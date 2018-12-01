
curr=0
while read line; do
  curr=$((curr + line))
done <input.txt
echo $curr
