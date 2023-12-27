from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
import time
def readData(port,baud,type,address,id):
    try:
        client = ModbusClient(method='rtu', port=port, baudrate=baud, timeout=1, parity='N', strict=False, stopbits=1)
        client.connect()
        time.sleep(1)
        if type == "signed":
            response = client.read_holding_registers(int(address), 2, unit=int(id))
            a = response.registers
            k = round(a[0] / 100, 2)
            client.close()
            return k
        if type == "float":
            response = client.read_input_registers(int(address), 2, unit=int(id))
            value1 = response.registers[0]
            value2 = response.registers[1]
            value = [value1, value2]
            decoder = BinaryPayloadDecoder.fromRegisters(value, byteorder=Endian.Big)
            p = decoder.decode_32bit_float()
            m = round(p, 3)
            client.close()
            return m
    except:
        print("Lỗi đọc dữ liệu")
value_1 = readData('/dev/ttyUSB0',9600,float,1,1)
print(value_1)