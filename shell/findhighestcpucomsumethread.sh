#!/bin/bash
LOG_FILE='/letv/logs/monitor/jvmdump.log'
JSTACK_PATH='/letv/logs/monitor/'
TIDDS=$(top -n5 -H | grep -m5 java | perl -pe 's/\e\[?.*?[\@-~] ?//g' | cut -f1 -d' ')
tidd_arr=($TIDDS)
echo 'highest cpu consume threads info:'$(date) >> $LOG_FILE
PID=0
for TIDD in "${tidd_arr[@]}"
do
	echo 'TIDD' $TIDD >> $LOG_FILE
	TIDH=$(printf "%x" $TIDD)
	echo 'TIDH' $TIDH >> $LOG_FILE
    PID=$(ps -aefL | grep java | grep -m1 ${TIDD} | awk '{print $3}')
	echo 'PID' $PID >> $LOG_FILE
	jstack $PID | grep -A500 $TIDH | grep -m1 "^$" -B 500 >> $LOG_FILE
done
jstack $PID >> ${JSTACK_PATH}${PID}.log

