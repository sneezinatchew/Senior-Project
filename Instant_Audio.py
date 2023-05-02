from pydub import AudioSegment
from pydub.playback import play
import time
import pyaudio
import threading

silent_eight = AudioSegment.silent(duration= 125, frame_rate=44100)
silent_quater = AudioSegment.silent(duration= 250, frame_rate=44100)
#disarm1 = AudioSegment.from_file("disarm1.wav")
#disarm2 = AudioSegment.from_file("disarm2.wav")
#disarm3 = AudioSegment.from_file("disarm3.wav")
#c = AudioSegment.from_file("C.wav")
#Em = AudioSegment.from_file("Em.wav")
#d = AudioSegment.from_file("D.wav")

def bpm(txt_file):
    with open(txt_file, "r") as f:
        lines = f.readlines()
        bpm = int(lines[0].strip('\n'))
        return bpm
        

       
def time_of_measure(txt_file):
    with open(txt_file, "r") as f:
        lines = f.readlines()
        bpm = int(lines[0].strip('\n'))
        top = int(lines[1].strip('\n'))
        #bottom = int(lines[2].strip('\n'))
        x = bpm / top
        seconds = 60 / x
        return seconds
    
def tempo(txt_file):
    with open(txt_file, "r") as f:
        lines = f.readlines()
        #bpm = int(lines[0].strip('\n'))
        top = int(lines[1].strip('\n'))
        bottom = int(lines[2].strip('\n'))
        return top, bottom


            

def starter_audio_disarm():
    duration_ms = 196000
    frame_rate = 44100
    blank_audio = AudioSegment.silent(duration=duration_ms, frame_rate=frame_rate)
    blank_audio.export("test_disarm.wav", format="wav")
    
def starter_audio_wish():
    duration_ms = 25000
    frame_rate = 44100
    blank_audio = AudioSegment.silent(duration=duration_ms, frame_rate=frame_rate)
    blank_audio.export("wish_demo.wav", format = "wav")

def starter_audio_delilah():
    duration_ms = 24000
    frame_rate = 44100
    blank_audio = AudioSegment.silent(duration=duration_ms, frame_rate=frame_rate)
    blank_audio.export("delilah_demo.wav", format = "wav")
    
def starter_audio_hallelujah():
    duration_ms = 27000
    frame_rate = 44100
    blank_audio = AudioSegment.silent(duration=duration_ms, frame_rate=frame_rate)
    blank_audio.export("hallelujah_demo.wav", format = "wav")
    
    
            

starter_audio = [starter_audio_disarm(), starter_audio_wish(), starter_audio_delilah(), starter_audio_hallelujah()]   

   
            
            
def play_audio(audio_file):
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(audio_file.sample_width),
                    channels=audio_file.channels,
                    rate=audio_file.frame_rate,
                    output=True)
    data = audio_file.raw_data
    stream.write(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    

def create_disarm():
#overlayed_audio = audio_file1.overlay(audio_file2, position=2000)
	with open("disarm.txt", "r") as f:
		first_time = True
		lines = f.readlines()
		bpm = int(lines[0].strip('\n'))
		top = int(lines[1].strip('\n'))
		bottom = int(lines[2].strip('\n'))
		one_measure = time_of_measure("disarm.txt")
		print(one_measure)
		start_time = 0.0
		loop = 0
		
		for i, line in enumerate(lines[3:]): # start from the fourth line
			notes = line.strip().split(",")
			start_time = one_measure*1000 * loop
			loop = loop + 1
			for note in notes:
				note, duration = note.split("/")
				duration = float(duration)
				print(note,duration)
				if first_time:
					first_time = False
					starter_audio_disarm()
					audio = AudioSegment.from_file("test_disarm.wav",format="wav")
				#if note == "0":
				#    	blank_note = AudioSegment.silent(duration = duration*1000)
				#    	audio = audio.overlay(blank_note, position=start_time)
				#else:
				filename = f"{note}.wav"
				sound = AudioSegment.from_file(filename)
				audio = audio.overlay(sound, position=duration)
				start_time = start_time + duration*1000
		audio.export("test_disarm.wav", format="wav")
    
def create_audio(file, newaudio, song_index):
        with open(file, "r") as f:
            first_time = True
            lines = f.readlines()
            bpm = int(lines[0].strip('\n'))
            top = int(lines[1].strip('\n'))
            bottom = int(lines[2].strip('\n'))
            one_measure = time_of_measure(file)
            # print(one_measure)
            start_time = 0.0
            loop = 0
            
            for i, line in enumerate(lines[3:]): # start from the fourth line
                notes = line.strip().split(",")
                start_time = one_measure*1000 * loop
                loop = loop + 1
                for note in notes:
                    note, duration = note.split("/")
                    duration = float(duration)
                    # print(note,duration)
                    if first_time:
                        first_time = False
                        starter_audio[song_index]
                        audio = AudioSegment.from_file(newaudio ,format="wav")
                    filename = "ABC_notes/" + note + ".wav"
                    sound = AudioSegment.from_file(filename)
                    audio = audio.overlay(sound, position=duration)
                    start_time = start_time + duration*1000
            audio.export(newaudio , format="wav")

# create_disarm()
create_audio("wish_you_were_here.txt", "wish_demo.wav",1)
create_audio("hey_there_delilah.txt", "delilah_demo.wav",2)
create_audio("hallelujah.txt", "hallelujah_demo.wav", 3)
print("\n")
print("Hallelujah by Jeff Buckley")
print(tempo("hallelujah.txt"))
print(bpm("hallelujah.txt"))
print(time_of_measure("hallelujah.txt"))
print('\n')

                

            


   