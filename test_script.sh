#!/bin/bash
x=10
while [ $x -gt 0 ]; do
  sleep 1s
  echo "$x seconds until blast off"
  x=$(($x - 1))
done
echo "Blast off!!"
