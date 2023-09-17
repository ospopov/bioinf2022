for i in $1/*
do
for j in $1/${i}/*
do
do cat ${i} >> out.txt
done
done
