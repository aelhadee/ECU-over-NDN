#! /bin/bash 
while true; do ps aux | grep -e examples/ -e nfd | head -n 4; sleep 1; done > pc_ndn_cpu.log
