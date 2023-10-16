import mido
from pythonosc.udp_client import SimpleUDPClient

# This is the port used for OSC. I think changing it will make the whole program useless.
PORT = 9000

client = SimpleUDPClient("127.0.0.1", PORT)

# Displays all connected and active MIDI inputs and asks which one should be opened.
print(mido.get_input_names())
inport = mido.open_input(input("> Which MIDI input should be opened? "))

for msg in inport:
    # print(msg) # Used for debugging. Remove the first hashtag to add it to the code (make sure it's spaced properly).
    if msg.type == "note_on":
        client.send_message(f"/avatar/parameters/Key{msg.note}", True)
    elif msg.type == "note_off":
        client.send_message(f"/avatar/parameters/Key{msg.note}", False)