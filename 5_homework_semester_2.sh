a="$(cat $1)"
for i in $(seq 0 60 ${#a})
do
echo ${a:${i}:60}
done
b=$(echo $a | rev)
for i in $(seq 0 60 ${#b})
do
echo ${b:${i}:60}
done
