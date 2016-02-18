#!/bin/bash
#Description:print jstack info of the top/custom cpu consume java thead id
#Arguments:$1 --java thead id
#Usage:
# 1.su linux user to the java process owner
# 2.
#   case1:execute this script with no arguments --show jstack info of the top cpu consume java thead id
#   case2:execute this script whih argument of java thead id u want to check,this will show jstack info of this java thead id above

#find the top cpu consume thead id
#using perl to escspe ANSI color code
if [ -z "$1" ]; then
	TID=$(top -n1 -H |grep -m1 java |perl -pe 's/\e\[?.*?[\@-~] ?//g' |cut -f1 -d' ')
	echo 'highest cpu consume threads info:'$(date)
else
	TID=$1
fi
echo 'thead id:'${TID}
TIDHEX=$(printf "%x" ${TID})
echo 'thead id in hex:' ${TIDHEX}
PID=$(ps -aefL | grep java | grep ${TID} | awk '{print $2}')
echo 'associate pid:' ${PID}
source /etc/profile
jstack ${PID} | grep -A500 ${TIDHEX} | grep -m1 "^$" -B 500

