import wave

def case(a):
	if a == '1':
		encode()
	elif a == '2':
		decode()
	elif a == '3':
		quit()
	else:
		print("\nEnter valid choice!")

def encode():
	string_in = input("\nEnter the string you want to hide: ")
	print("\nEncoding in progress...")
	audio = wave.open("input/sample.wav", mode="rb")
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	
	# string_in = "Spiderman is Peter Parker"
	print(string_in)
	# create a new string from the original string
	string_in = string_in + int((len(frame_bytes)-(len(string_in)*64))/8) * '#'
	
	bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string_in])))
	for i, bit in enumerate(bits):
		frame_bytes[i] = (frame_bytes[i] & 254) | bit
	frame_modified = bytes(frame_bytes)
	for i in range(0, 10):
		print(frame_bytes[i])
	new_audio = wave.open('output/sample_out.wav', 'wb')
	new_audio.setparams(audio.getparams())
	new_audio.writeframes(frame_modified)

	new_audio.close()
	audio.close()
	print("Successfully encoded into sample_out.wav")


def decode():
	print("\nDecoding Starts...")
	audio = wave.open("output/sample_out.wav", mode='rb')
	frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
	extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
	string_out = "".join(chr(int("".join(map(str, extracted[i:i+8])), 2)) for i in range(0, len(extracted), 8))
	decoded = string_out.split("###")[0]
	print("Successfully decoded: " + decoded)
	audio.close()	


while(True):
	print("\nEnter your choice:\n1 = Encode\n2 = Decode\n3 = Exit")
	val = input("\nYour choice: ")
	case(val)
