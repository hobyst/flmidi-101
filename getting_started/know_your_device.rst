================
Know your device
================

Now that you know how the MIDI protocol works, before telling FL Studio about your MIDI device you'll need to know what you have to tell. Your device has it's own way of communicating with DAW software and you need to know how it interacts with them in order to script for FL Studio. How you do it? Through reverse engineering.

What you need is as much information as possible on how your device works under the hood and which MIDI messages have to be sent to it in order to use its features. An example of this information would be the `Ableton Push 2 MIDI and Display Interface Manual <https://github.com/Ableton/push-interface/blob/master/doc/AbletonPush2MIDIDisplayInterface.asc>`_ by Ableton.

This article will guide you through the different techniques you can use to guess how to talk with your MIDI device. However, some exceptions may apply, that if possible, will be documented at the end of this article.

.. warning:: **DO NOT EVER TRY TO DECOMPILE THE PROPRIETARY DRIVER(S) OR SOFTWARE PROVIDED BY THE MANUFACTURER TO KNOW THE MIDI SPECIFICATION OF THE DEVICE.** There's a high chance you'll either be doing something that is either illegal (like breaking IP or patent rights) or against some sort of EULA contract from the manufacturer.

Organize yourself
-----------------

When trying to reverse engineer a specification, the best practice is to write down everything you find so when the moment to code arrives, you won't have to do everything again: just looking at the documentation you wrote should be enough for you to be able to code. Create tables with the different messages you get, write down your thoughts about what you have seen so far... Even the slightest thing might help you to guess everything out.

- Create tables with the different messages you get and what button you pressed to get it

- Write down your thoughts about what you have seen so far

- With that information, try to find the logic behind those messages based on the features of the device.

MIDI Monitoring
---------------

The easiest aspect to reverse engineer are the messages your device sends when you press a button. Using a MIDI monitoring tool like 
`Pocket MIDI <https://www.morson.jp/pocketmidi-webpage>`_, `MIDI Monitor <https://www.snoize.com/MIDIMonitor>`_ (macOS only) or 
`MIDI-OX <http://www.midiox.com/http://www.midiox.com>`_ (Windows only) you will be able to see the different messages your device sends to your DAW.

* **Buttons:** Pressing a button should send a MIDI message to your PC with some sort of differentiating factor between one button and another (normally as different ``DATA1`` values). You might also get two messages: one for the button press and another one for the button release.

* **Knobs:** Using a knob depends on the kind of knob your MIDI device has:
    
  * **Absolute knobs:** These ones go from 0 to 127, giving their value depending on their physical position on the controller and forcing synchronization 
    with the value they control to their physical position. They usually have a spin limit so you can't spin them indefinitely as the knob will prevent you from doing so, reaching either their maximum or the minimum value.
  
  * **Relative knobs:** These act like some sort of button, sending a unique message depending on the direction the user is spinning the knob 
    (clockwise or counter-clockwise). This allows the knob to modify the value of the parameter it controls using increments rather than force-syncing its value to 
    match its physical position like absolute knobs do.

* **Faders:** Normally act as absolute knobs.

**Your controller doesn't send any MIDI message at all when you use certain buttons?** Some MIDI controllers have features and buttons locked only to be used with 
proprietary software from the manufacturer or the DAWs the controller is officially supported on. Depending on the way these are unlocked, you might be able to trick 
your device to think a supported software has been launched so that it unlocks those features. The usual "key" for this is a MIDI or SysEx message the DAW sends to 
the device as soon as it gets detected to wake up the device. And in order to get this message, you will need to either spy on the messages your device and a supported 
DAW send to each other or look on the internet to find if there's any public information about it or some piece of code made by other people for other DAWs.