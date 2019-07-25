# multi-device-record-script
python script used for recording multiple devices in one time on Mac

# How to use:
## 1. add devices in Audio MIDI Setup
<img width="145" alt="Screen Shot 2019-07-24 at 7 48 57 PM" src="https://user-images.githubusercontent.com/20760190/61842199-2dc2cf00-ae4c-11e9-8206-d8f2b1b90056.png">


![Screen Shot 2019-07-24 at 7 49 59 PM](https://user-images.githubusercontent.com/20760190/61842246-5fd43100-ae4c-11e9-8602-486bdac93a7a.png)

## 2. Modify correct variable in script
modify the correct aggregate device name in variable ```input_device``` of record_script.py, in my example, it should have ```input_device="AggregateDevice"```.Variable ```channel_device``` is a list of device name, it could be any string

## 3. run script in terminal: 
python3 record_script.py. By default, it will save audio file (with multiple channels) every 3 seconds, you can change the time for saving by modify variable ```onefilelen```

