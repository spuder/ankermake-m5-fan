esphome clean config.yaml && \
esphome compile config.yaml && \
esphome upload --device /dev/cu.usbmodem211301 config.yaml && \
esphome logs config.yaml --device /dev/cu.usbmodem211301 && \
esphome dashboard . --open-ui --address 127.0.0.1 --port 6053