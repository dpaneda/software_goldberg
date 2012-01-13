#!/bin/bash

COMMANDS="
read_tweet.py \
goodbye \
tunnel
"

function start_machine {
  echo -n "Building rube goldberg machine, please wait"
  for program in $COMMANDS
  do
    echo -n .
    ./$program &
    sleep 0.1
  done
  echo "OK"
}

function stop_machine {
  echo -n "Destroying rube goldberg machine, please wait"
  for program in $COMMANDS
  do
    echo -n .
    pkill -f $program
  done
  echo "OK"
}

case "$1" in
  start)
    stop_machine
    start_machine
    ;;
  stop)
    stop_machine
    ;;
  go)
    start_machine
    ./send_tweet.py &
    ;;
  *)
    echo "What ?"
    echo "Usage: $0 start / stop"
esac
