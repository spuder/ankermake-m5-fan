# esphome clean config.yaml && \
esphome compile config.yaml && \
esphome upload --device /dev/cu.usbmodem01 config.yaml && \
esphome logs config.yaml --device /dev/cu.usbmodem01 && \
esphome dashboard . --open-ui --address 127.0.0.1 --port 6053


# esptool.py --before default_reset --after hard_reset --baud 115200 --port /dev/cu.usbmodem01 --chip esp32s2 write_flash -z --flash_size detect 0x10000 /Users/spencer.owen/Code/github/spuder/ankermake-m5-fan/configs/esp32s2/.esphome/build/foobar3/.pioenvs/foobar3/firmware.bin 0x1000 /Users/spencer.owen/Code/github/spuder/ankermake-m5-fan/configs/esp32s2/.esphome/build/foobar3/.pioenvs/foobar3/bootloader.bin 0x8000 /Users/spencer.owen/Code/github/spuder/ankermake-m5-fan/configs/esp32s2/.esphome/build/foobar3/.pioenvs/foobar3/partitions.bin 0xe000 /Users/spencer.owen/.platformio/packages/framework-arduinoespressif32/tools/partitions/boot_app0.bin