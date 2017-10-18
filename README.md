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
More informations on how to setup CAN interfaces can be found [here](https://elinux.org/Bringing_CAN_interface_up)

3. Install OBDSimulator

## How to use

## Ressources

* [CAN-Bus (Wikipedia Arcticle)](https://en.wikipedia.org/wiki/CAN_bus)

* [List of OBD-II PIDs and the OBD Query/Response system](https://en.wikipedia.org/wiki/OBD-II_PIDs)

 
