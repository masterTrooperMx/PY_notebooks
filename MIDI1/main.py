# carga un midi y los vuelve json
# luego analizamos cuantos tracks
# luego dibujamos los tracks

from utils import midiClass

myMidi = midiClass('./data/Yesterday.mid')
myMidi.midi2json()
#print(myMidi.tracks)
myMidi.print_track(1)