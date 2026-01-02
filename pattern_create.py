import sys
def create_pattern(length):
	character_1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	character_2="abcdefghijklmnopqrstuvwxyz"
	character_3="0123456789"
	out=""

	for a in character_1:
		for b in character_2:
			for c in character_3:
				out+=a+b+c
				if len(out)>=length:
					return out
	return out[:length]
if(len(sys.argv)!=2):
	print("USAGE <script.py> <size>")
size=int(sys.argv[1])
print(create_pattern(3000))




