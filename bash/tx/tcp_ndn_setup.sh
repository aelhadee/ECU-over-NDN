#! /bin/bash 
service nfd restart
# PC
nfdc strategy set /lidar /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.11
nfdc route add /lidar tcp4://192.168.10.11

nfdc strategy set /cam /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.12 
nfdc route add /cam tcp4://192.168.10.12

nfdc strategy set /can /localhost/nfd/strategy/best-route
nfdc face create tcp4://192.168.10.13 
nfdc route add /can tcp4://192.168.10.13
