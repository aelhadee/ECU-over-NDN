#! /bin/bash 
while true; do ps aux | grep -e examples/ -e nfd; sleep 1; done > pc_tx_ndn_cpu.log
