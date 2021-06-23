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
    # message to be hidden inside wav file
    string_in = input("\nEnter the string you want to hide: ")
    print(string_in)

    print("\nOpening wav...")

    # open and get wav audio object
    audio = wave.open(wav_in, mode="rb")
    time.sleep(0.2)

    print("\nEncoding...")
    # get number of frames from WAV audio
    num_of_audio_frames = audio.getnframes()

    # get bytes object
    bytes_object = audio.readframes(num_of_audio_frames)

    # convert bytes object to list
    bytes_list = list(bytes_object)

    # get array of bytes from audio frames
    bytes_array_encode = bytearray(bytes_list)

    # modify original message
    string_mod = string_in + int((len(bytes_array_encode) - (len(string_in) * 64)) / 8) * '#'

    # turn modified string into a list of bits
    bits_list = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string_mod])))

    # encode and turn the list of bits into a new array of bytes
    for i, bit in enumerate(bits_list):
        bytes_array_encode[i] = (bytes_array_encode[i] & 254) | bit
    bytes_array_encode_mod_object = bytes(bytes_array_encode)
    time.sleep(0.2)

    # writing the new encoded array of bytes into output WAV audio
    print("\nWriting to output WAV...")
    new_audio = wave.open(wav_out, 'wb')
    new_audio.setparams(audio.getparams())
    new_audio.writeframes(bytes_array_encode_mod_object)
    time.sleep(0.2)

    new_audio.close()
    audio.close()
    print("Successfully encoded!")


def decode(wav_out):
    print("\nOpening encoded wav...")

    # get encoded WAV audio object
    audio = wave.open(wav_out, mode='rb')
    time.sleep(0.2)

    print('Decoding...')
    # get array of bytes from encoded WAV audio
    bytes_array_decode = bytearray(list(audio.readframes(audio.getnframes())))

    # extract a list of bits from encoded array of bytes
    bits_list_extracted = [bytes_array_decode[i] & 1 for i in range(len(bytes_array_decode))]

    # produce a string from the extracted list of bits
    string_extracted = "".join(chr(int("".join(map(str, bits_list_extracted[i:i + 8])), 2)) for i in range(0, len(bits_list_extracted), 8))

    # decode produced string
    decoded = string_extracted.split("###")[0]
    time.sleep(0.2)

    # output original message
    print("Successfully decoded: " + decoded)
    audio.close()


while True:
    print("\nEnter your choice:\n1 = Encode\n2 = Decode\n3 = Exit")
    my_choice = input("\nYour choice: ")
    start_steganography(my_choice)
