#!/bin/bash
args=${@}

hello2()
{
        echo "this is func2 ${2}, ${args}"
}

echo "${1}"
echo "${args}"

if [ ${1} -eq 1 ]
then
        hello2
elif [ ${1} -eq 2 ]
then
        hello2
else
        echo "param is error! ${args}"
fi

for loop in ${@}
do
        echo "this loop is ${loop}"
done

#for((i=1;i<=5;i++))
#do
#       echo "this is ${i}"
#done

i=5

while [ ${i} -lt 10 ]
do
        i=$((${i} + 1))
        echo "this is while ${i}"
done

x=5
until [ ! ${x} -lt 15 ]
do
        #[i++]
        x=$((${x} + 1))
        echo "this is until ${x}"
done

case ${1} in
        1)
                echo "match is 1 -> ${1}"
                ;;
        *)
                echo "not match anything! ${1}"
                ;;
esac