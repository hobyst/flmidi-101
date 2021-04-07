====================
Handling MIDI Inputs
====================

Overview
========

Each time a MIDI message gets received by FL Studio from a MIDI device with a Python script assigned to it, several script events get called as a part of a
filtering process with several levels that allows, among others, to process MIDI messages of the same kind the same way without having to repeat code for
each specific message.

.. SVG graph showing the MIDI filtering stack should go here

Level 0: Reception and ``OnMidiIn()``
=====================================

When your device sends a MIDI message to FL Studio, it creates an `event object <https://www.image-line.com/fl-studio-learning/fl-studio-online-manual
/html/midi_scripting.htm#eventType>`__ that will represent the message for your script to use it.

.. class:: event

    Represents and holds the data of a MIDI message in order for a MIDI script to be able to react and use it.
    
    .. attribute:: handled
        :type: bool
        :value: False

        Controls wether the message will make it into the next MIDI filtering stage or not. (read/write access)

        Each time the execution of a ``OnMidi*()`` script event ends, FL Studio will check the value of ``handled`` to decide whether the event has to
        get promoted to the next filtering level or the script doesn't need any further processing of the event.

    .. attribute:: timestamp
        :type: time

        Timestamp of the event. (read access)

    .. attribute:: status
        :type: int

        Value of the STATUS byte of the MIDI message. (read/write access)

    .. attribute:: data1
        :type: int

        Value of the DATA1 byte of the MIDI message. (read/write access)

        If the message is a SysEx message, it will be set to ``0``.

    .. attribute:: data2 
        :type: int

        Value of the DATA2 byte of the MIDI message. (read/write access)

        If the message is a SysEx message, it will be set to ``0``.

    .. attribute:: port
        :type: int

        Value of the MIDI port the MIDI device is assigned to. (read access)
    
    .. attribute:: note
        :type: int

        MIDI note number. (read/write access)
    
    .. attribute:: velocity
        :type: int
        
        MIDI velocity. (read/write access)

    .. attribute:: pressure
        :type: int

        MIDI pressure. (read/write access)

    .. attribute:: progNum
        :type: int

        MIDI program number. (read access)

    .. attribute:: controlNum
        :type: int

        MIDI control number. (read access)

    .. attribute:: controlVal
        :type: int

        MIDI control value. (read access)
    
    .. attribute:: pitchBend
        :type: int

        MIDI pitch bend value. (read access)
    
    .. attribute:: sysex
        :type: bytes

        If the message is a SysEx message, the full byte chain will be available here. (read/write access)

        If the message is regular MIDI message, it will be set to ``None``.
    
    .. attribute:: isIncrement
        :type: bool

        MIDI is increment state. (read/write access)

    .. attribute:: res
        :type: double

        Unknown. (read/write access)

    .. attribute:: inEv
        :type: int

        Unknown. (read/write access)
    
    .. attribute:: outEv
        :type: int

        Unknown. (read/write access)
    
    .. attribute:: midiId
        :type: int

        Unknown. (read/write access)
    
    .. attribute:: midiChan
        :type: int

        MIDI channel used to transmit the message (with index on ``0``). (read/write access)
    
    .. attribute:: midiChanEx
        :type: int

        Unknown. (read/write access)
    
    .. attribute:: pmeflags
        :type: int

        Tags the event with a number to add more information about it. (read access)

        See `table <https://www.image-line.com/fl-studio-learning/fl-studio-online-manual/html
        /midi_scripting.htm#pmeFlags>`__