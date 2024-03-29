====================
Introduction to MIDI
====================

.. note:: All inline references to hexadecimal numbers will be formatted as ``XX``. Otherwise, they will be decimal values or binary values (these last ones being easy to recognize).

The `MIDI (Musical Instrument Digital Interface) protocol <https://en.wikipedia.org/wiki/MIDI>`__ is the communication standard pretty much every music hardware uses to intercommunicate with other music hardware.

It carries information back and forth between devices using messages made out of hexadecimal bytes (like ``B1``, ``01`` or ``F2``; they are basically numeric values encoded in hexadecimal going from 0 // ``00`` to 255 // ``FF``) that can be transmitted using one or multiple of 16 information channels, so multiple messages can be transmitted and received by the same device at the same time.

It uses two kind of messages with different structures and used for different purposes.

Standard MIDI messages
======================

These are used almost by any MIDI device and usually carry button/key pressing information.

A regular MIDI message consists of a chain of three hexadecimal bytes:

+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Byte 1: ``STATUS``                                                            | Byte 2: ``DATA1``                                                                                                                                         | Byte 3: ``DATA2``                                                                                                                                                                                     |
+===============================================================================+===========================================================================================================================================================+=======================================================================================================================================================================================================+
| Specifies the kind of message that is being sent (note on/off, aftertouch...) | Field for additional data (depends on the ``STATUS`` byte). For example, on note pressing events it is used to specify the note that is being pressed.    | Field for additional data (depends on the ``STATUS`` byte). For example, on note pressing events it is used to specify the velocity of the key pressing (in a range of 0 // ``00`` to 127 // ``7F``). |
+-------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The different possible values for the ``STATUS`` byte, as well as the ones for ``DATA1`` and ``DATA2`` can be found here:

- `Expanded MIDI 1.0 Messages List (Status Bytes) <https://www.midi.org/specifications-old/item/table-2-expanded-messages-list-status-bytes>`__

- `MIDI note numbers and center frequencies <https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies>`__

- `Control Change Messages (Data Bytes) <https://www.midi.org/specifications-old/item/table-3-control-change-messages-data-bytes-2>`__

Many of the MIDI messages (also called "events") related to buttons for DAW control will probably consist of a ``STATUS`` byte corresponding to one of the note on events (from 144 to 159) or the control change events (from 176 to 191) with a ``DATA1`` number unique to that button and a generic ``DATA2`` value like 0, 1 or 127. In case of some devices two messages might be sent from the device: one for the button press and another for the button release.

Example of a message to notify a note pressing:

+------------------------+--------------------------------------+-------------------------------+-----------------------------------+
|                        | ``STATUS``                           |``DATA1``                      |``DATA2``                          |
+========================+======================================+===============================+===================================+
| **Message**            |   ``90``                             |  ``81``                       |  ``127``                          |
+------------------------+--------------------------------------+-------------------------------+-----------------------------------+
| **Description**        | Note On message on channel 1         | Note A5 ("La5" on solfège)    |  100% (maximum) velocity          |
+------------------------+--------------------------------------+-------------------------------+-----------------------------------+

Buttons on devices with DAW control capabilities usually use this same principle but with a dumb ``DATA2`` value (since they only need to report the pressing of a specific button) and maybe a different ``STATUS`` byte so that they don't get misunderstood as key pressings. You have to keep in mind that even when using standard MIDI messages, the device you are trying to script for might not follow what is written in this guide, and it's up to you to guess which messages relate to which features of your MIDI controller.

System Exclusive (SysEx) messages
=================================

SysEx messages are the most interesting yet more complex and harder to reverse-engineer but the ones behind most of the features we love from MIDI controllers.

They are made out of several "header" bytes, a data chunk of unlimited length and an ending byte:

.. table::
    :widths: 15 85

    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Byte name             | Description                                                                                                                                                                                                                                                             |
    +=======================+=========================================================================================================================================================================================================================================================================+
    | **Start byte**        | It is used to open every SysEx message. Its value is always ``F0``, which is the ``STATUS`` byte value for SysEx messages.                                                                                                                                              |
    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Manufacturer ID**   | Can take either 1 byte (``00``) or 3 bytes (``00 00 00``) on the message. Every single MIDI manufacturer is registered with the MIDI Association and has a unique ID. You can find them `here <https://www.midi.org/specifications-old/item/manufacturer-id-numbers>`__.|
    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Device ID**         | This one is usually used for chain-connected MIDI devices, so that a SysEx message only targets one device of the chain rather than all of them. On MIDI over USB isn't normally used and it's default value is ``01``.                                                 |
    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Model ID**          | Should be unique for each device model the manufacturer makes. (assigned by the manufacturer)                                                                                                                                                                           |
    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Command ID**        | It is usually used to specify what kind of information you are going to send/request to/from the device. (assigned by the manufacturer)                                                                                                                                 |
    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Arguments**         | The actual body of the message you are sending. It has an unlimited length. (assigned by the manufacturer)                                                                                                                                                              |
    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **End byte**          | It is used to close every SysEx message. Its value is always ``F7``.                                                                                                                                                                                                    |
    +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Here's an example with ``F0 00 20 29 02 18 0B 51 3F 29 00 F7``, which sets the color of the RGB light of a pad to orange (HTML/HEX: ``FFA500``, RGB: R255 G165 B000) on the Novation Launchpad MK2:

.. table::
    :widths: 15 15 80

    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Byte name             | Value             | Description                                                                                                                                                                                                                                                             |
    +=======================+===================+=========================================================================================================================================================================================================================================================================+
    | **Start byte**        | ``F0``            |                                                                                                                                                                                                                                                                         |
    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Manufacturer ID**   | ``00 20 29``      | Focusrite/Novation                                                                                                                                                                                                                                                      |
    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Device ID**         | ``02``            | Launchpad                                                                                                                                                                                                                                                               |
    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Model ID**          | ``18``            | Launchpad MK2                                                                                                                                                                                                                                                           |
    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Command ID**        | ``0B``            | Change LED color (RGB mode)                                                                                                                                                                                                                                             |
    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **Arguments**         | ``51 3F 29 00``   | The ``DATA1`` number of the 1st pad on the Session mode (``51``), and the RGB data of the color in hex bytes scaled down from 0-255 to 0-63 (``3F 29 00``).                                                                                                             |
    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | **End byte**          | ``F7``            |                                                                                                                                                                                                                                                                         |
    +-----------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

As many manufacturers approach MIDI messages in different ways depending on what they want to do, you will have to see how your device reacts with each thing you do on it based on the context (what button you pushed, the features of your device, the different ways you can use it...).

If you need more information about the MIDI protocol, you can go to the `MIDI Association <https://www.midi.org/>`__ webpage, create a (free) account and get access to their `forums <https://www.midi.org/forum>`__ as well as the `full specifications <https://www.midi.org/specifications>`__ of both MIDI 1.0 (the well-known MIDI and the one described here) and MIDI 2.0 (the new and more advanced MIDI standard).

In summary
==========

* MIDI messages are made of numbers (normally encoded in hexadecimal), whose meaning depends on the context and the place they take on the message.

* To differentiate between standard MIDI messages, ask yourself the following questions each time you see one:

  * **Is the message 3 bytes** ``XX XX XX`` **long?:** If the answer is yes, then you are reading a standard MIDI message.
  * **Is the message more than 3 bytes long** ``XX XX XX XX ...`` **, starts with** ``F0`` **and ends with** ``F7`` **?:** If the answer is yes, then you are reading a 
    SysEx message.

* The best place to find information about how to understand the MIDI protocol is the `MIDI Association <https://www.midi.org/>`__ website. There are so many different aspects about 
  the protocol and so many different ways to implement it that it would take an eternity to document everything. 

  However, since such a technical and low-level oriented specification might be hard to understand even for experienced programmers, don't feel afraid to ask for 
  clarifications if there's anything you don't understand to other people on the Internet, but before doing it try to inform yourself as much as possible about 
  the topic in question. The answer you are looking for might have already been answered somewhere else.