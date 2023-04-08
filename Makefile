# generate make file with `clean`, build, upload and logs steps
# Usage: make [clean|build|upload|logs]
.PHONY: all clean build upload dashboard logs

all: build upload dashboard logs

#clean step
clean:
	esphome clean config-esp32-c3.yaml
build:
	esphome config config-esp32-c3.yaml
	esphome compile config-esp32-c3.yaml
upload:
	esphome upload --device /dev/cu.wchusbserial21140 config-esp32-c3.yaml
logs:
	esphome logs config-esp32-c3.yaml --device /dev/cu.wchusbserial21140
dashboard:
	esphome dashboard . --open-ui --address 127.0.0.1 --port 6053



# rp2040
# /dev/cu.usbmodem211401



# esp32
# esphome upload --device /dev/cu.usbmodem487F300F7AC31 config-esp32.yaml