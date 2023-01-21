#! /bin/bash 
# UDP
service nfd restart
# PC
nfdc strategy set /lidar /localhost/nfd/strategy/best-route
nfdc face create udp4://192.168.10.11
nfdc route add /lidar udp4://192.168.10.11

nfdc strategy set /cam /localhost/nfd/strategy/best-route
nfdc face create udp4://192.168.10.12 
nfdc route add /cam udp4://192.168.10.12

nfdc strategy set /can /localhost/nfd/strategy/best-route
nfdc face create udp4://192.168.10.13 
nfdc route add /can udp4://192.168.10.13
