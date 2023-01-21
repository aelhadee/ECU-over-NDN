#! /bin/bash 
while true; do cat /proc/net/wireless | grep wlp0s20f3; sleep 1; done > pc_wifi_perf.log

