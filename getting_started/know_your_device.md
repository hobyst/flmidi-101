# Know your device

Now that you know how the MIDI protocol works, before telling FL Studio about your MIDI device you'll need to know what you have to tell. Your device has it's own way of communicating with DAW software and you need to know how it interacts with them in order to script for FL Studio. How you do it? Through reverse engineering.

What you need is as much information as possible on how your device works under the hood and which MIDI messages have to be sent to it in order to use its features. An example of this information would be the [Ableton Push 2 MIDI and Display Interface Manual](https://github.com/Ableton/push-interface/blob/master/doc/AbletonPush2MIDIDisplayInterface.asc) by Ableton.

This article will guide you through the different techniques you can use to guess how to talk with your MIDI device. However, some exceptions may apply, that if possible, will be documented at the end of this article.

**Note:** DO NOT EVER TRY TO DECOMPILE THE PROPIETARY DRIVER(S) OR SOFTWARE PROVIDED BY THE MANUFACTURER TO KNOW THE MIDI SPECIFICATION OF THE DEVICE. There's a high chance you'll either be doing something that is either illegal (like breaking IP or patent rights) or against some sort of EULA contract from the manufacturer.

## Organize yourself

When trying to reverse engineer a specification, the best practice is to write down everything you find so when the moment to code arrives, you won't have to do everything again: just looking at the documentation you wrote should be enough for you to be able to code. Create tables with the different messages you get, write down your thoughts about what you have seen so far... Even the slightest thing might help you to guess everything out.

- Create tables with the different messages you get and what button you pressed to get it

- Write down your thoughts about what you have seen so far

- With that information, try to find the logic behind those messages based on the features of the device.

## MIDI Monitoring

The easiest aspect to reverse engineer are the messages your device sends when you press a button. Using a MIDI monitoring tool like [Pocket MIDI](https://www.morson.jp/pocketmidi-webpage/), [MIDI Monitor](https://www.snoize.com/MIDIMonitor/) (macOS only) or [MIDI-OX](http://www.midiox.com/http://www.midiox.com/) (Windows only) you will be able to see the different messages your device sends to your DAW.


