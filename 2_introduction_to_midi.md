# Introduction to MIDI

> NOTE: All inline references to hexadecimal numbers will be formatted as `XX`. Otherwise, they will be decimal values or binary values (these last ones being easy tp recognize).

The [MIDI (Musical Instrument Digital Interface) protocol](https://en.wikipedia.org/wiki/MIDI) is the communication standard pretty much every music hardware uses to intercommunicate with other music hardware.

It carries information back and forth between devices using messages made out of hexadecimal bytes (like `B1`, `01` or `F2`; they are basically numeric values encoded in hexadecimal going from 0 // `00` to 255 // `FF`) that can be transmited using one or multiple of 16 information channels, so multiple messages can be transmitted and recieved by the same device at the same time.

It uses two kind of messages, but have a different structure and are for different purposes.

## Standard MIDI messages

These are used almost by any MIDI device and usually carry button/key pressing information.

A regular MIDI message consists of a chain of three hexadecimal bytes, plus two more that are used as a starting (`F0`) and ending (`F7`) bytes but these are normally omitted on regular 3-byte MIDI messages:

| Byte 1: `STATUS`                                                              | Byte 2: `DATA1`                                                                                                                                      | Byte 3: `DATA2`                                                                                                                                                                                 |
|:-----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Specifies the kind of message that is being sent (note on/off, aftertouch...) | Field for additional data (depends on the `STATUS` byte). For example, on note pressing events it is used to specify the note that is being pressed. | Field for additional data (depends on the `STATUS` byte). For example, on note pressing events it is used to specify the velocity of the key pressing (in a range of 0 // `00` to 127 // `7F`). |

The different possible values for the `STATUS` byte, as well as the ones for `DATA1` and `DATA2` can be found here:

- [Expanded MIDI 1.0 Messages List (Status Bytes)](https://www.midi.org/specifications-old/item/table-2-expanded-messages-list-status-bytes)

- [MIDI note numbers and center frequencies](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies)

- [Control Change Messages (Data Bytes)](https://www.midi.org/specifications-old/item/table-3-control-change-messages-data-bytes-2)

Many of the MIDI messages (also called "events") related to to buttons for DAW control will probably consist of a `STATUS` byte corresponding to one of the note on events (from 144 to 159) with a `DATA1` number unique to that button and a generic `DATA2` value like 0, 1 or 127. In case of some devices two messages might be sent from the device: one for the button press and another for the button release.

Example of a message to notify a note pressing:

|             | `STATUS`                     | `DATA1`                    | `DATA2`                 |
| ----------- |:----------------------------:|:--------------------------:|:-----------------------:|
| Message     | `90`                         | `81`                       | `127`                   |
| Description | Note On message on channel 1 | Note A5 ("La5" on solfège) | 100% (maximum) velocity |

Buttons on devices with DAW control capabilities usually use this same principle but with dumb `DATA2` value (since they only need to report the pressing of a specific button) and maybe a different `STATUS` byte so that they don't get misunderstood as key pressings.
