#! /bin/bash

service nfd restart
unset nfdc strategy
nfdc strategy unset /ndn/broadcast
nfdc strategy unset /localhost/nfd
nfdc strategy unset /localhost
nfdc strategy set /trailerECU/can/data /localhost/nfd/strategy/best-route	
nfdc face create udp://192.168.10.33
nfdc route add /trailerECU/can/data udp://192.168.10.33
