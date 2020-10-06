import array

def func():
    pass



def yrange(n):
    i = 0
    while i < n:
        yield i
        i += 1

def get_objects():
    
    types = [{'key':'value'}, 'str', 1.0, None,
        1+1j, True, [], 1, b'str',
            (1,2,3), range(1), bytearray(b'str'),
            {1,2,3,4}, frozenset({1,2,3,4}), memoryview(b'abcefg'),
            object(), type(object()), func, array, ValueError(), Exception(),
            len, iter([1,2,3]), iter({'key':'value'}), yrange(5), str.center]
    
    return sorted(types, key=lambda x: type(x).__name__)