#! /bin/bash
service nfd restart
#CAN - RPI 12
nfdc strategy set /trailer/can /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.33:6363
nfdc route add /trailer/can tcp4://192.168.10.33:6363
