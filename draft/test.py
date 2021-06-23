import wave
import time


string_in = "Testing testing!"
print(string_in)
# print("\nEncoding in progress...")

audio = wave.open("input/sample.wav", mode="rb")

num_of_audio_frames = audio.getnframes()
bytes_object = audio.readframes(num_of_audio_frames)
# print(audio.readframes(num_of_audio_frames))
bytes_list = list(bytes_object)
# print(list(bytes_object))
bytes_array = bytearray(bytes_list)
# print(bytes_array)

# append hashtags to original string to create string_mod
string_mod = string_in + int((len(bytes_array) - (len(string_in) * 64)) / 8) * '#'

# for i in string_mod:
#     print(i)
# print(string_mod[0:20])
# for i in string_mod:
#     int_equivalent = ord(i)
#     binary_str_0b_stripped_len_8_zero_filled_head = bin(int_equivalent).lstrip('0b').rjust(8, '0')
#     print(int(''.join(binary_str_0b_stripped_len_8_zero_filled_head)))
#     print("Binary obj: " + bin(ord(i)) for i in string_mod)

map_object = map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string_mod]))
# print([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in string_mod])
# print(''.join([bin(ord(i)).lstrip('0b').rjust(8, '0') for i in "str"]))
bits = list(map_object)
# print(bits)

for i, bit in enumerate(bits):
    # Bitwise '|' (or) operator: Returns 1 if either of the bit is 1 else 0.
    bytes_array[i] = (bytes_array[i] & 254) | bit
bytes_array_mod_object = bytes(bytes_array)

# print(bytes_array_mod_object)
# show samples of bytes_array
# for i in range(0, 20):
    # print(bytes_array[i])
    # print(type(bytes_array))
    # print(bytes_array_mod_object)

new_audio = wave.open('output/sample_out.wav', 'wb')
new_audio.setparams(audio.getparams())
new_audio.writeframes(bytes_array_mod_object)


new_audio.close()
audio.close()
# print("Successfully encoded into sample_out.wav")

# print("\nDecoding...")
audio = wave.open("output/sample_out.wav", mode='rb')
bytes_array = bytearray(list(audio.readframes(audio.getnframes())))
extracted_list = [bytes_array[i] & 1 for i in range(len(bytes_array))]
# print(extracted_list)
string_extracted = "".join(chr(int("".join(map(str, extracted_list[i:i + 8])), 2)) for i in range(0, len(extracted_list), 8))
# print('string_extracted: ' + string_extracted)
decoded = string_extracted.split("###")[0]
time.sleep(0.2)
# print("Successfully decoded: " + decoded)
audio.close()