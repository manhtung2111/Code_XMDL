from pymodbus.client.sync import ModbusSerialClient

client = ModbusSerialClient(method = "rtu", port="COM13",stopbits = 1, bytesize = 8, parity = 'N', baudrate= 9600)
client.connect()
print(client.connect())
