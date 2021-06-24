# audio-steganography-try-hard-python
## Assignments
1. Each group can has at most 5 students.
2. Each group has to prepare: python code that works, one 8-page report, one presentation in 7 minutes.
3. The presentation date is Thursday, June 24 (Detail information will be sent later).

## Members
<table>
  <tr>
    <th style="color:red; font-weight:bold"> Name </th>
  	<th style="color:yellow; font-weight:bold"> Role </th>
  </tr>

  <tr>
  	<td> Le Viet Anh </td>
  	<td> Coding </td>
  </tr>
  
  <tr>
  	<td> Do Thanh Dat </td>
  	<td> Presentation </td>
  </tr>  

  <tr>
  	<td> Vu Tuan Phuong Nam </td>
  	<td> Co-coder </td>
  </tr>

  <tr>
  	<td> Tran Bao Huy </td>
  	<td> Report </td>
  </tr>
  
  <tr>
  	<td> Nguyen Tu Tung </td>
  	<td> Report </td>
  </tr>  
</table>

## Contributions
1. Le Viet Anh: 
2. Do Thanh Dat:
3. Vu Tuan Phuong Nam:
4. Tran Bao Huy:
5. Nguyen Tu Tung:

## Requirements
1. OS: Windows 10
2. Python 3.7 installed (https://www.howtogeek.com/197947/how-to-install-python-on-windows/)
3. Input audio: in WAV format (by default it's sample.wav)
4. Non-unicode message

## Project Explained

### Console appearance

![image](https://user-images.githubusercontent.com/47298653/123188431-37d12a80-d4c6-11eb-91d4-ebc15dcbcfb9.png)

### Project Structures
---input---sample.wav <br>
| <br>
---output---sample_out.wav <br>
| <br>
---audio_steganography.bat, audio_steganography.py, install-packages.bat, uninstall-packages.bat <br>

### Setup
<p>To run this project, first double click on install-packages.bat to install required modules for the program. Then we run audio_steganography.bat to start the code.</p>
<p>Another way is to run the audio-steganography.exe inside audio_steganography_executable folder</p>
<p>The input wav file is located inside input folder, while the output wav file with encoded text could be found in output directory.</p>
<p>Inside audio_steganography.py we have 3 methods: encode, decode and start_steganography. We can adjust the path to input and output in start_steganography as shown below:</p>

![image](https://user-images.githubusercontent.com/47298653/123109070-20ae2080-d465-11eb-9a81-76c950a60098.png)

<p>The main menu will look like this:</p>

![image](https://user-images.githubusercontent.com/47298653/123109327-57843680-d465-11eb-9111-81d3ebe2b2f0.png)

### Encode
<p>Enter 1 for encoding, then enter whatever message you want to hide inside sample.wav, for example 'Hello World' as followed:</p>

![image](https://user-images.githubusercontent.com/47298653/123109637-99ad7800-d465-11eb-8c32-841101cf8732.png)

![image](https://user-images.githubusercontent.com/47298653/123109926-d7120580-d465-11eb-801e-f49f165bba32.png)

### Decode
<p>To decode, simply enter 2 as below:</p>

![image](https://user-images.githubusercontent.com/47298653/123111159-e34a9280-d466-11eb-8282-78dde6b0e4b6.png)

![image](https://user-images.githubusercontent.com/47298653/123111209-ee052780-d466-11eb-89db-7146ef47faaa.png)

### Exit

![image](https://user-images.githubusercontent.com/47298653/123111351-0a08c900-d467-11eb-8092-dc5b966695a5.png)

### Algorithm
**About WAV**
<p>WAV audio is a sequence of frames, each frame contains amplitude (loudness) information (represented in bytes) at that particular point in time. To produce sound, thousands of these frames are played in sequence to produce frequencies.</p>

**What is LSB**
<p>Least Significant bit also called RightMost Bit is a lowest bit of a binary number. For example in binary number 10010010, "0" is the least significant bit.</p>

**What is LSB-Steganography**
<p>LSB-Steganography is a steganography technique in which we hide messages inside an image by replacing Least significant bit of image with the bits of message to be hidden. By modifying only the first most right bit of an image we can insert our secret message and it also make the picture unnoticeable, but if our message is too large it will start modifying the second right most bit and so on and an attacker can notice the changes in picture.</p>






## References
1. https://github.com/sniperline047/Audio-Steganography 
2. https://stackoverflow.com/questions/3957025/what-does-a-audio-frame-contain  
3. https://www.cybrary.it/blog/0p3n/hide-secret-message-inside-image-using-lsb-steganography/


