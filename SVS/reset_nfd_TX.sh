#! /bin/bash
service nfd restart
nfdc strategy set /trailer/rear/camera /localhost/nfd/strategy/best-route
nfdc face create udp://192.168.10.11
nfdc route add /trailer/rear/camera udp://192.168.10.11

nfdc strategy set /trailer/rear/lidar /localhost/nfd/strategy/best-route
nfdc face create udp://192.168.10.13
nfdc route add /trailer/rear/lidar udp://192.168.10.13

nfdc strategy set /trailer/serial/buses /localhost/nfd/strategy/best-route
nfdc face create udp://192.168.10.12
nfdc route add /trailer/serial/buses udp://192.168.10.12
nfdc strategy unset /ndn/broadcast
nfdc strategy unset /localhost/nfd
nfdc strategy unset /localhost

