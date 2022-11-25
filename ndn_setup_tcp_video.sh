#! /bin/bash 
service nfd restart
#LIDAR - RPI 13
nfdc strategy set /trailer/cam /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.33:6363
nfdc route add /trailer/cam tcp4://192.168.10.33:6363
