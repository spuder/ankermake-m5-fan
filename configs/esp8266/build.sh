# esphome clean d1mini.yaml && \
esphome compile d1mini.yaml && \
esphome upload --device /dev/cu.usbserial-21140 d1mini.yaml && \
esphome logs d1mini.yaml --device /dev/cu.usbserial-21140 && \
esphome dashboard . --open-ui --address 127.0.0.1 --port 6053