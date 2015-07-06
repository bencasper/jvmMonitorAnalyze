#!//bin/sh
LOG_FILE='/letv/logs/monitor/jvmdump.log'
TIDDS=$(top -a -n5 -H | grep -m5 java | perl -pe 's/\e\[?.*?[\@-~] ?//g' | cut -f1 -d' ')
tidd_arr=($TIDDS)
echo 'highest ram consume threads info:' $(date) >> $LOG_FILE
for TIDD in "${tidd_arr[@]}"
do
        echo 'TIDD' $TIDD >> $LOG_FILE
        TIDH=$(printf "%x" $TIDD)
        echo 'TIDH' $TIDH >> $LOG_FILE
        PID=$(ps -aefL | grep java | grep -m1 ${TIDD} | awk '{print $3}')
        echo 'PID' $PID >> $LOG_FILE
        jstack $PID | grep -A500 $TIDH | grep -m1 "^$" -B 500 >> $LOG_FILE
done
