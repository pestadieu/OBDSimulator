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

3. Clone this repository

```
git clone https://github.com/pestadieu/OBDSimulator.git
```

4. Run OBDSimulator

```
python3 src/main.py
```

## Supported OBD PIDS

Currently the simulator only supports these PIDS:

0D - Vehicle Speed

0C - Engine RPM


## Run the tests

1. In a terminal start the server:

```
python3 src/main.py
```

2. In another terminal run the tests:

```
python3 test/main.py
```

## Ressources

* [CAN-Bus (Wikipedia Arcticle)](https://en.wikipedia.org/wiki/CAN_bus)

* [List of OBD-II PIDs and the OBD Query/Response system](https://en.wikipedia.org/wiki/OBD-II_PIDs)

 
