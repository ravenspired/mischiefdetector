#!/bin/bash

kernel=$1
stride=$2
reps=$3
x=$4
y=$5


convolve () {
    length=$1
    for i in `seq 1 $reps`; do
        echo "Convolution #$i"
        echo "Length: $length"
        if [ $kernel -le $length ]; then
            # OK, convolution kernel fits.
            total=0
            lengthRemaining=$length
            done=""
            until [ $done ]; do
                if [ $kernel -le $lengthRemaining ]; then
                    lengthRemaining=$((lengthRemaining-stride))
                    total=$((total+1))
                else
                    done=true
                fi
            done
            length=$total
        else
            # Yikes, kernel doesn't fit.
            echo 'Too Small, Aborting!'
            break
        fi
    done
}

echo Convolving x
convolve $x

echo
echo Convolving y
convolve $y