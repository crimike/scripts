#copy each file from $1 to $2 directory
for f in $(ls $1)
do
    echo $f
    cp ${1}/$f ${2}/$f
done
