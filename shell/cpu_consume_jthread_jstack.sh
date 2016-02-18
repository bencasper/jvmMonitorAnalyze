#!/bin/bash
#find jstack info of the top/custom cpu consume java thead id
#$1 --java thead id 
#find the top cpu consume thead id
#using perl to escspe ANSI color code
if [ -z "$1" ]; then
	TID=$(top -n1 -H |grep -m1 java |perl -pe 's/\e\[?.*?[\@-~] ?//g' |cut -f1 -d' ')
else
	TID=$1
fi
echo 'highest cpu consume threads info:'$(date)
echo 'thead id:'$TID
TIDHEX=$(printf "%x" $TID)
echo 'thead id in hex:' $TIDHEX
PID=$(ps -aefL | grep java | grep $TID | awk '{print $2}')
echo 'associate pid:' $PID
source /etc/profile
jstack $PID | grep -A500 $TIDHEX | grep -m1 "^$" -B 500

