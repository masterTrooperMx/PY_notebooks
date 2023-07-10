# creamos objeto midi
import sys
import json
import mido

class midiClass:
    # setup class
    def __init__(self, mfile='./data/Test.mid') -> None:
        self.midi_file = mido.MidiFile(mfile)
    # create a dict
    def midifile2dict(self, mid):
        self.tracks = []
        for track in mid.tracks:
            self.tracks.append([vars(msg).copy() for msg in track])

        return {
            'ticks_per_beat': mid.ticks_per_beat,
            'tracks': self.tracks,
        }
    # convert midi file into json
    def midi2json(self):
        print(json.dumps(self.midifile2dict(self.midi_file), indent=2))
    # convert to full python object from json
    def json2dict(self, jsonFile):
        # Opening JSON file
        with open(jsonFile) as json_file:
            data = json.load(json_file)
 
        # Print the type of data variable
        print("Type:", type(data))
    # print track
    def print_track(self, numTrack):
        track = self.tracks[numTrack]
        for t in track:
            print(f"t={t['time']}")

#mid = mido.MidiFile(sys.argv[1])
#mid = mido.MidiFile('./data/Yesterday.mid')

#print(json.dumps(midifile_to_dict(mid), indent=2))