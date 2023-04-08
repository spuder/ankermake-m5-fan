# AnkerMake-M5 Fan


## Design Objective Document: AnkerMake M5 Fan Control

### Problem

The AnkerMake M5 Fan produces too much noise.

### Solution

The problem can be addressed either by software or hardware.
Anker has not yet provided a software fix. See [this github issue for details](https://github.com/ankermake/AnkerMake-Marlin/issues/3)

Until they provide a solution, we create a hardware solution to override the fan speed. 


### Objectives

The following objectives will be considered in designing the AnkerMake M5 Fan Control:

- **Reversibility:** The solution must be 100% reversible without any permanent modifications required.
- **Redundancy:** The solution should have no single points of failure and include redundant systems and sensors.
- **Updateability:** The solution should be updatable via wifi-usb and open source. It should not require any special programmers.
- **Feedback Loops:** The solution should include feedback loops that show the state of the system using LED or similar indicators.
- **Safety:** The solution must match or exceed all inputs to prevent any damage to fans.

### Preferences

The following preferences will be considered in designing the AnkerMake M5 Fan Control:

- **Aesthetics:** The solution should be beautiful and/or invisible.
- **API Accessibility:** The solution should be consumable through API.
- **Ease of Programming:** The solution should have a simple framework for programming.



## Development

Install esphome

```bash
brew install esphome
```

To test and build the firmware run these commands
```bash
make build && make upload
```

To upload the firmware and open a dashboard at 127.0.0.1:6053 and view logs run these commands
```bash
make clean
make all
```