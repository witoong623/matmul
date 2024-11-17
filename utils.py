import struct


def load_float32_array(filepath):
    ''' Load array data from binary file in Python list.\n
        Caller must interpret the data as intended by caller
    '''
    arr = []
    with open(filepath, 'rb') as f:
        A_data = f.read()
        for i in range(0, len(A_data), 4):
            element_data = A_data[i:i+4]
            assert len(element_data) == 4
            arr.append(struct.unpack('f', element_data)[0])
    return arr
