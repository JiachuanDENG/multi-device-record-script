# play and record audio dataset using multi-microphones
# need to install following pakadges first
# bella 12/05/18
# update 03/28/19
# update 04/07/19
# modified by Jiachuan Deng 07/24/2019

import sounddevice as sd
import wave
import pyaudio
import os
import datetime
from tqdm import tqdm


FORMAT = pyaudio.paInt16
BUFFER_SIZE = 1024
SAMPLE_RATE = 16000
onefilelen = 50 # 50 map to about 3 seconds

out_dir = "/Users/JiachuanDengAdmin/Desktop/record_out/"
input_device="AggregateDevice"
channel_device = ["MBP"]


# print device list
device_list = sd.query_devices()
print(device_list)

in_ind = -1

for i in range(len(device_list)):

    if (input_device in device_list[i]["name"]):
        print('Mic: '+device_list[i]["name"])
        channel_num=device_list[i]["max_input_channels"]
        print('Channels: '+str(channel_num))
        in_ind = i



if (in_ind == -1):
    raise NameError("Didn't find wanted mic!")


t1 = datetime.datetime.now()

p = pyaudio.PyAudio()

# record



fidx= 0
while True:
    input_stream = p.open(
        format=FORMAT,
        channels=channel_num,
        rate=SAMPLE_RATE,
        input=True,
        output=False,
        frames_per_buffer=BUFFER_SIZE,
        input_device_index=in_ind
        )

    input_stream.start_stream()
    frames=[]
    for i in tqdm(range(onefilelen)):

        frames.append(input_stream.read(BUFFER_SIZE))
    input_stream.stop_stream()

    outpath = os.path.join(out_dir,str(fidx)+'.wav')
    fidx += 1
    outwf = wave.open(outpath,'wb')
    outwf.setnchannels(channel_num)
    outwf.setsampwidth(p.get_sample_size(FORMAT))
    outwf.setframerate(SAMPLE_RATE)
    outwf.writeframes(b''.join(frames))
    outwf.close()
    print("file saved "+outpath)

    input_stream.close()


p.terminate()

t2=datetime.datetime.now()


deltat=t2-t1
print(deltat)


print('Finished processing.')
