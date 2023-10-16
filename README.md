## MIDI to OSC
This simple Python script converts MIDI input to OSC, specifically intended to work with VRChat and my VRChat piano visualiser, which will be published in the **near future**.

[Mido](https://pypi.org/project/mido/) and [python-osc](https://pypi.org/project/python-osc/) (and Python) are required. You can install them easily by running the two commands below in your terminal (if you have pip installed).
`pip install mido`
`pip install python-osc`

If you do not have my VRChat piano visualiser, and want to include a piano in your avatar, contact me for more information on how to do so.

## How to Use

Using this program is quite straightforward:
* Run *midi_to_osc.py*,
* Look at the list of MIDI inputs (which looks like `['USB-MIDI 0']` in my case) and input exactly as shown the name of the one you wish to listen to, **including the number at the end** (in my case `USB-MIDI 0`).

That's it!

## How does it work?

This script basically listens to the MIDI input you give it and when it detects a message, either `"note_on"` or `"note_off"`, it sends a signal, either `True` or `False` to a specific URI for the note it just detected. Yes, this means every note has a different URI. The only reason I adopted this method was to achieve complete independence of every key on my VRChat piano visualiser. Currently the URI is structured like this: `/avatar/parameters/KeyXXX`, where `XXX` represents a two- or three-digit number (without any leading zeros) which corresponds to the MIDI note number. This signal is then handled further by the avatar.
