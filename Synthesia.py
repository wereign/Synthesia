from PIL import Image
from numpy import asarray
import sounddevice as sd
import soundfile as sf


class Synthesia:
    def __init__(self, image_path):

        self.sampling_frequency = 44100
        self.image = Image.open(image_path)
        self.image_array = asarray(self.image)

        # Operating on the image array to convert it to a 2D array
        # Transposing the array to make it playable

        self.audio_array = self.image_array.transpose(2, 0, 1).reshape(3, -1).T
        self.match_types = []
        for i in self.audio_array:
            for j in i:
                self.match_types.append(float(j))

    def play_audio(self):

        sd.play(self.audio_array, blocking=True)

    def save_file(self, file_name):

        sf.write(file_name+'.wav', self.match_types, self.sampling_frequency)


synth = Synthesia('syntheisia_block_1.png')
synth.play_audio()
synth.save_file('synth_audio1')
