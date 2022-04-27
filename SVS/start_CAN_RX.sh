#! /bin/bash

service nfd restart
unset nfdc strategy
nfdc strategy unset /ndn/broadcast
nfdc strategy unset /localhost/nfd
nfdc strategy unset /localhost
nfdc strategy set /trailer/serial/buses /localhost/nfd/strategy/best-route	
nfdc face create udp://192.168.10.33
nfdc route add /trailer/serial/buses udp://192.168.10.33
