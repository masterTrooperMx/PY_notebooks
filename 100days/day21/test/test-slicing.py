piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
piano_tuple = ('do', 're', 'mi', 'fa', 'sol', 'la', 'si')
# mutable iterable
print(piano_keys)
print(piano_keys[1:]) # skip position 0
print(piano_keys[:5]) # from first to position 4
print(piano_keys[2:5]) # position 2 to 4
print(piano_keys[1::2]) # position 1 to the end, every two places
print(piano_keys[::2]) # from begining to end every two places
print(piano_keys[::-1]) # backwards
# non mutable iterable
print(piano_tuple)
print(piano_tuple[1:]) # skip position 0
print(piano_tuple[:5]) # from first to position 4
print(piano_tuple[2:5]) # position 2 to 4
print(piano_tuple[1::2]) # position 1 to the end, every two places
print(piano_tuple[::2]) # from begining to end every two places
print(piano_tuple[::-1]) # backwards