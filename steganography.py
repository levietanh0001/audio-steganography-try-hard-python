import wave
import time


def start_steganography(a):
    wav_in = "input/sample.wav"
    wav_out = "output/sample_out.wav"
    if a == "1":
        encode(wav_in, wav_out)
    elif a == "2":
        decode(wav_out)
    elif a == "3":
        quit()
    else:
        print("\nEnter valid Choice!")


def encode(wav_in, wav_out):
    string_in = input("\nEnter the string you want to hide: ")
    print(string_in)

    print("\nOpening wav...")
    audio = wave.open(wav_in, mode="rb")
    time.sleep(0.2)

    print("\nEncoding...")
    bytes_array_encode = bytearray(list(audio.readframes(audio.getnframes())))
    string_mod = string_in + int((len(bytes_array_encode) - (len(string_in) * 64)) / 8) * '#'
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string_mod])))
    for i, bit in enumerate(bits):
        bytes_array_encode[i] = (bytes_array_encode[i] & 254) | bit
    bytes_array_encode_mod_object = bytes(bytes_array_encode)
    time.sleep(0.2)

    # for i in range(0, 10):
    #     print(bytes_array_encode[i])
    print("\nWriting to sample_out.wav...")
    new_audio = wave.open(wav_out, 'wb')
    new_audio.setparams(audio.getparams())
    new_audio.writeframes(bytes_array_encode_mod_object)
    time.sleep(0.2)

    new_audio.close()
    audio.close()
    print("Successfully encoded!")


def decode(wav_out):
    print("\nDecoding...")
    audio = wave.open(wav_out, mode='rb')
    # get array of bytes from wav
    bytes_array_decode = bytearray(list(audio.readframes(audio.getnframes())))

    extracted_list = [bytes_array_decode[i] & 1 for i in range(len(bytes_array_decode))]
    string_extracted = "".join(chr(int("".join(map(str, extracted_list[i:i + 8])), 2)) for i in range(0, len(extracted_list), 8))
    decoded = string_extracted.split("###")[0]
    time.sleep(0.2)
    print("Successfully decoded: " + decoded)
    audio.close()


while True:
    print("\nEnter your choice:\n1 = Encode\n2 = Decode\n3 = Exit")
    my_choice = input("\nYour choice: ")
    start_steganography(my_choice)
