import sys
def create_pattern(length):
    charset1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    charset2 = "abcdefghijklmnopqrstuvwxyz"
    charset3 = "0123456789"
    out = ""

    for a in charset1:
        for b in charset2:
            for c in charset3:
                if len(out) >= length:
                    return out
                out += a + b + c
    return out[:length]
if(sys.argv!=2):
	print("USAGE:<script.py> <eip>/<rip>")
eip=sys.argv[1]
pattern = create_pattern(3000)

eip = eip.lower()

# little endian fix
eip_bytes = bytes.fromhex(eip)
eip_str = eip_bytes[::-1].decode(errors="ignore")

print("Offset:", pattern.find(eip_str))
