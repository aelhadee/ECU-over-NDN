#! /bin/bash
modprobe vcan
ip link add dev vcan0 type vcan
ip link set vcan0 mtu 72
ip link set dev vcan0 up
