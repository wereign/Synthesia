from PIL import Image
from numpy import asarray
import sounddevice as sd
import soundfile as sf

file_no = 0
class Synthesia:
    def __init__(self, image_path):

        self.sampling_frequency = 44100
        self.image = Image.open(image_path)
        self.image_array = asarray(self.image)

        # Operating on the image array to convert it to a 2D array
        # Transposing the array to make it playable

        self.audio_array = self.image_array.flatten()
        self.match_types = []
        for i in self.audio_array:
                self.match_types.append(float(i))

    def play_audio(self):

        sd.play(self.audio_array, blocking=True)

    def save_file(self, file_name):
        global file_no
        sf.write(f'output/{file_no}'+file_name+'.wav', self.match_types, self.sampling_frequency)
        path = f'output/{file_no}'+file_name+'.wav'
        print(path)

        file_no +=1
        return path

# synth = Synthesia('static/images/logo.png')
# synth.save_file('test')

