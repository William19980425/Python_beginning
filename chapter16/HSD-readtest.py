import numpy as np
import struct

def read_h8(fn):
    # Read data header
    f = open(fn, 'rb')
    hlen = 0

    # 1 Basic information block
    f.read(282)
    hlen += 282

    # 2 Data information block
    f.read(5)
    
    ncol, nrow = struct.unpack('<hh', f.read(4))
    print(ncol, nrow)
    f.read(41)
    hlen += 50

    # 3 Data block
    data = np.fromfile(f, np.float32, ncol * nrow * nband)
    data = data.reshape((nrow, ncol, nband))

    return data

if __name__ == '__main__':
    data = read_h8('HS_H09_20230711_0800_B01_JP02_R10_S0101.DAT')
    print(data)