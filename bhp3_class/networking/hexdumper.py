# https://code.activestate.com/recipes/142812-hex-dumper/

HEX_FILTER = ''.join(
    [(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

def hexdump(src, show=False, length=8):
    if isinstance(src, bytes):
        src = src.decode()
    
    results = list()
    for i in range(0, len(src), length):
        word = src[i:i+length]
        printable = word.translate(HEX_FILTER)
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        results.append(f'{i:04x}  {hexa:<{hexwidth}}  {printable}')
    if show:
        for line in results:
            print(line)
    else:
        return results

if __name__ == '__main__':
    s = b'''This little function is just a sample of python's power
         for string manipulations."
         The code is \x07even\x08 quite readable!'''
    for line in hexdump(s):
        print(line)
