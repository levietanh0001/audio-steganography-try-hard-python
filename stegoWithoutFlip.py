import wave


def case(a):
    if a == "1":
        encode()
    elif a == "2":
        decode()
    elif a == "3":
        quit()
    else:
        print("\nEnter valid Choice!")


def encode():
    string_in = input("\nEnter the string you want to hide: ")
    print(string_in)
    print("\nEncoding Starts..")
    audio = wave.open("input/sample.wav", mode="rb")
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    string_in = string_in + int(((2 * len(frame_bytes)) - (len(string_in) * 8 * 8)) / 8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string_in])))
    j = 0
    for i in range(0, len(frame_bytes), 2):
        frame_bytes[j] = frame_bytes[j] & 243
        if bits[i] == 0 and bits[i + 1] == 1:
            frame_bytes[j] = frame_bytes[j] + 4
        elif bits[i] == 1 and bits[i + 1] == 0:
            frame_bytes[j] = frame_bytes[j] + 8
        elif bits[i] == 1 and bits[i + 1] == 1:
            frame_bytes[j] = frame_bytes[j] + 12
        j = j + 1
    frame_modified = bytes(frame_bytes)
    new_audio = wave.open('output/sampleStegoWithoutFlip.wav', 'wb')
    new_audio.setparams(audio.getparams())
    new_audio.writeframes(frame_modified)

    new_audio.close()
    audio.close()
    print("Successfully encoded inside sampleStegoFlip.wav!")


def decode():
    print("\nDecoding Starts..")
    audio = wave.open("output/sampleStegoWithoutFlip.wav", mode='rb')
    frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
    extracted = []
    for i in range(len(frame_bytes)):
        frame_bytes[i] = frame_bytes[i] & 12
        if frame_bytes[i] == 0:
            extracted.append(0)
            extracted.append(0)
        elif frame_bytes[i] == 4:
            extracted.append(0)
            extracted.append(1)
        elif frame_bytes[i] == 8:
            extracted.append(1)
            extracted.append(0)
        elif frame_bytes[i] == 12:
            extracted.append(1)
            extracted.append(1)
    string_out = "".join(chr(int("".join(map(str, extracted[i:i + 8])), 2)) for i in range(0, len(extracted), 8))
    decoded = string_out.split("###")[0]
    print("Successfully decoded: " + decoded)
    audio.close()


while True:
    print("\nEnter your choice: \n1 = Encode\n2 = Decode\n3 = Exit")
    val = input("\nYour choice:")
    case(val)
