# OBDSimulator

A simple OBD-II simulator software

## Install

OBDSimulator only works with versions of python >= 3.3

1. Load the driver for the virtual CAN interface

```
[sudo] modprobe vcan
```

2. Create a new virtual CAN interface and activate it

```
[sudo] ip link add dev vcan0 type vcan
[sudo] ip link set up vcan0
```
You can verify that the interface has been created by running the ```ip link show``` command

3. Install OBDSimulator

## How to use

