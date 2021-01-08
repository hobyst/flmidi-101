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

MIDI monitoring
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
DAW send to each other or look on the internet to find if there's any public information about it or some piece of code made by other people for other DAWs. Continue 
reading to know more about these methods.

Getting the MIDI specification of your device
---------------------------------------------

If you are having issues figuring out how to work with your device because some stuff isn't working or you are trying to use a feature that requires sending messages 
to the device, then you should look for the MIDI specification of your device: documentation that DAW developers would normally get in order to bring compatibility with 
a device for their DAW and specifies how the device should be contacted and used.

Unfortunately, this information isn't usually available for the public but a Google search might help. If you don't see anything, you can try looking on forums or 
contacting the manufacturer of your device (although it is likely they won't give it to you).

Man in the middle
-----------------

A man in the middle approach means you will be hearing the messages being sent to and received from your device when an officially supported DAW is running on your PC by 
putting yourself in the middle of both to know what are they saying to each other. There are multiple options depending on your OS, since the methods available to you 
depend on how the MIDI protocol is handled internally in your OS.

macOS
=====

Between macOS and Windows, macOS it's the one with the easiest man-in-the-middle method. `MIDI Monitor <https://www.snoize.com/MIDIMonitor>`_ has a feature called 
"Spy on output to destinations", that allows the software to monitor any kind of MIDI message, even if you haven't routed the device to send messages to the MIDI monitor. 
This way, if you connect your MIDI device and both an officially supported DAW and MIDI Monitor are running, you will be able to see and record all the messages the DAW 
sends to the device as well as any message your device sends back.

Then you can re-send all of the messages the DAW sent to the device to see how the device reacts to them and start to break down the MIDI specification.

.. note:: Since MIDI Monitor only works with MIDI messages, this monitoring method won't work with devices that use other protocols such as OSC. For any other protocol
          you will either need to use a dedicated monitor utility for it or analyze the raw USB data using something like `Wireshark <https://www.wireshark.org/>`_.

Windows
=======

On Windows, due to how MIDI is implemented, device assignations are exclusive. This means two software cannot connect to the same MIDI device at the same time. 
Trying to do this will result in an error on the 2nd software you are trying to connect saying other software is already using the device so the connection cannot 
be done. Because of this, doing man-in-the-middle MIDI sniffing on Windows isn't possible. At least in theory...

While the MIDI stack on Windows doesn't allow you to do so, you can go lower: the USB stack. You can monitor the USB messages being sent and received to/from your 
device using `Wireshark <https://www.wireshark.org/>`_ and `USBPcap <https://desowin.org/usbpcap/>`_. To know about this method, read 
:doc:`../tutorials/midi/midi_sniffing_win`.

Looking at already written code
-------------------------------

If nothing of the above worked for you, the only thing left to try is looking at other people's code that have successfully adapted your MIDI controller to work 
with other DAWs. You'll be on your own doing this and you'll need to know several programming languages in order to do this. Some of the best pieces of code to look 
at are:

* `DrivenByMoss <https://github.com/git-moss/DrivenByMoss>`_ by Jürgen Moßgraber: Written in Java for Bitwig Studio, it features almost any MIDI controller you can 
  imagine.

* Ableton `Live 9 <https://github.com/gluon/AbletonLive9_RemoteScripts>`_ , `Live 10 <https://github.com/gluon/AbletonLive10.1_MIDIRemoteScripts>`_ and 
  `Live 11 (beta) <https://github.com/gluon/AbletonLive11_MIDIRemoteScripts>`_ MIDI Remote Scripts by Julien Bayle: Written in Python for Ableton Live. These 
  repositories contain the same Python scripts that bring compatibility with MIDI devices to Ableton Live. Pretty much every controller compatible with Ableton Live 
  has its sources included on these repositories. As stated by Julien on his website, Robert Henke, one of the co-founders of Ableton and co-developer of Ableton Live 
  already knows about the ability of users to decompile the scripts (as Python bytecode compilation can be reversed).

.. tip::  In order to look through the code of these vast repositories properly, either a code editor or an IDE is recommended, as well as Git to be able to clone 
          the repositories in your PC rather than reading them directly on GitHub.
