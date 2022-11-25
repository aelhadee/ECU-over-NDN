#! /bin/bash 
service nfd restart
# PC
nfdc strategy set /trailer/lidar /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.11
nfdc route add /trailer/lidar tcp4://192.168.10.11

nfdc strategy set /trailer/can /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.12 
nfdc route add /trailer/can tcp4://192.168.10.12

nfdc strategy set /trailer/cam /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.13 
nfdc route add /trailer/cam tcp4://192.168.10.13
