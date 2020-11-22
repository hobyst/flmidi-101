# flmidi-101: A comprehensive guide for FL Studio MIDI Scripting

## 0. Before we get started...

You have to keep in mind how familiar you are with Python (and programming, in general) before you get into reading the rest of this guide.

If you are already familiar with Python programming, you can straight up skip this and start reading the next section, but if you are new to either Python or programming, then this might be of your interest.

### 0.1. Firstly, what is this Python thing?

Python is an open-source, high-level, object-oriented, intepreted and multiplatform programming language.

**Excuse me, what?**

A programming language is what you use to tell a computer what you want it to do. Pretty much like humans have English, French, Spanish, Chinese and so on, computers have their own ones, and that is what you use to make any piece of software. In the early days of computing, you had to directly tell orders that were more hardware-oriented, but nowdays you have way more better options than writting in [assembly](https://en.wikipedia.org/wiki/Assembly_language). The "level" of the programming language you use is determined by how much it abstracts you from hardware control.

The more higher, the less hardware focused and more easier to use, but more likely to have worse performance since you don't have control over what's happening behind the scenes. The more lower, more hardware-focused and technical they get, so you have more precise control over how your software behaves, but they are more tedious to program on. It's a sacrifice between hardware control and ease of use.

In programming, there are multiple ways the instructions of your code can be executed depending on the programming language you use. The main two ways are: procedurally and object-oriented.

In procedural programming languages (like the well-known [C](https://en.wikipedia.org/wiki/C_(programming_language))) your code is executed as some sort of "step-by-step instruction", going line to line right from the first one down to the last one (unless there's an error on your program and the execution breaks). This is okay for simple programs, but as a software gets more complicated, it can become a nightmare. And that's when **object**-oriented programming comes in: instead of your code being a literal instruction, it becomes a definition of multiple parts/modules where you tell what an object is capable of and what **atributtes** it will have. On runtime, you generate (**instantiate**) objects out of those definitions (**classes**) that will have their own job on your software and communicate with each other to get your software working. However, you can also write procedural code on an object-oriented language.

When you have written a piece of code and you want to test it, you need to pass that code to a compiler since the your code is just plain text and your computer doesn't know what to do with it. The compiler (on languages that generate native code like C or C++, notice there are some exceptions like [Java](https://en.wikipedia.org/wiki/Java_compiler)) is a piece of software that translates those human-readable instructions you write using a "regular" programming language down to the lowest language possible: [machine code](https://en.wikipedia.org/wiki/Machine_code). Do you remember Assembly? Well, this one is way more complicated, being the closest-to-hardware existing language and contains raw CPU instructions. This way, you can use the advantages of a human-readable language while performing as faster as possible when you use your software.

Python, in contrast to natively compiled languages where you run [binary executable files](https://en.wikipedia.org/wiki/Executable), you directly run the source code file(s) (`.py` format) using the Python [interpreter](https://techterms.com/definition/interpreter). When you write in Python you don't target the system, but the interpreter. And then the interpreter is the one that actually transposes the code you wrote to native instructions if needed, but native code is never generated. In fact, there's a Python compiler that optimizes the code to be initialized faster, but doesn't either improve performance or bypass the need of having the Python interpreter installed to run Python code.

And lastly, due to the fact that Python code is made to target the interpreter rather than a system, any platform compatible with Python's interpreter will be able to run your code. This is the reason Python is a multiplatform language.

### 0.2. Getting prepared for Python development and FL Studio MIDI scripting

The first thing you will need to properly code in Python is the Python interpreter. Even tho Image-Line's documentation says it isn't necessary for making scripts for FL Studio (and they are right on that one), it is recomended to have it installed so you can get language integration features when using a code editor. For MIDI scripting, FL Studio uses a custom Python interpreter based on Python 3.6.x that you can download from the [official page](https://www.python.org/downloads/) (download a version from that specific branch, the 3.6.x one, not the latest Python release).

Since source code files are usually just text files that get interpreted by a compiler (and in case of Python, a interpreter that hot-reads the instructions), you can write code in any text editor like Windows' Notepad or Notepad++. But since these are done for general purpose and basic text editing, using them you will miss a lot of the optimizations a dedicated code editor can bring to you. Code completion, debugging features, syntax checking and extensions are just a few things that nowdays development tools bring to the equation.

To take it further, there [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment) also exist, putting together a code editor and the rest of the tools you might be using (compilers, debuggers and so on) under the same umbrella. However, they are more complicated to setup and a bit overpowered for what we are going to do. So sticking with a code editor is the best option.

The editor this guide will reference is the open-source code editor [Visual Studio Code](https://code.visualstudio.com/) by Microsoft. It's one of the most popular code editors among a wide range of developers due to how lightweight and versatile it is. If you don't like it for being a Microsoft software or you are weary about telemetry (even tho you can disable it), you can also use [VSCodium](https://vscodium.com/). Inside Visual Studio Code, you will also need to install the [Python language extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

Now that you are all set up, you can start learning Python programming. There are a lot of tutorials out there, but one of the best's is [W3schools' Python guide](https://www.w3schools.com/python/default.asp). You can start reading it from the [Syntax](https://www.w3schools.com/python/python_syntax.asp) page and it is advised that you read it at least until the [Functions](https://www.w3schools.com/python/python_functions.asp) section to get a basic understanding of the language, as well as the [Modules](https://www.w3schools.com/python/python_modules.asp) section and the [Math](https://www.w3schools.com/python/python_math.asp) module page. Simply create a `.py` file using Visual Studio Code and start practicing by writting code. VS Code should detect your Python interpreter and running your code should be as simple as right-clicking your source code file on the *Browser* and then selecting *Run Python file on the terminal*.

## 1. Introduction to MIDI

> NOTE: All inline references to hexadecimal numbers will be formatted as `XX`. Otherwise, they will be decimal values or binary values (these last ones being easy tp recognize).

The [MIDI (Musical Instrument Digital Interface) protocol](https://en.wikipedia.org/wiki/MIDI) is the communication standard pretty much every music hardware uses to intercommunicate with other music hardware.

It carries information back and forth between devices using messages made out of hexadecimal bytes (like `B1`, `01` or `F2`; they are basically numeric values encoded in hexadecimal going from 0 // `00` to 255 // `FF`) that can be transmited using one or multiple of 16 information channels, so multiple messages can be transmitted and recieved by the same device at the same time.

It uses two kind of messages with different structures and used for different purposes.

### 1.1 Standard MIDI messages

These are used almost by any MIDI device and usually carry button/key pressing information.

A regular MIDI message consists of a chain of three hexadecimal bytes:

| Byte 1: `STATUS`                                                              | Byte 2: `DATA1`                                                                                                                                      | Byte 3: `DATA2`                                                                                                                                                                                 |
|:-----------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Specifies the kind of message that is being sent (note on/off, aftertouch...) | Field for additional data (depends on the `STATUS` byte). For example, on note pressing events it is used to specify the note that is being pressed. | Field for additional data (depends on the `STATUS` byte). For example, on note pressing events it is used to specify the velocity of the key pressing (in a range of 0 // `00` to 127 // `7F`). |

The different possible values for the `STATUS` byte, as well as the ones for `DATA1` and `DATA2` can be found here:

- [Expanded MIDI 1.0 Messages List (Status Bytes)](https://www.midi.org/specifications-old/item/table-2-expanded-messages-list-status-bytes)

- [MIDI note numbers and center frequencies](https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies)

- [Control Change Messages (Data Bytes)](https://www.midi.org/specifications-old/item/table-3-control-change-messages-data-bytes-2)

Many of the MIDI messages (also called "events") related to buttons for DAW control will probably consist of a `STATUS` byte corresponding to one of the note on events (from 144 to 159) with a `DATA1` number unique to that button and a generic `DATA2` value like 0, 1 or 127. In case of some devices two messages might be sent from the device: one for the button press and another for the button release.

Example of a message to notify a note pressing:

|             | `STATUS`                     | `DATA1`                    | `DATA2`                 |
| ----------- |:----------------------------:|:--------------------------:|:-----------------------:|
| Message     | `90`                         | `81`                       | `127`                   |
| Description | Note On message on channel 1 | Note A5 ("La5" on solfège) | 100% (maximum) velocity |

Buttons on devices with DAW control capabilities usually use this same principle but with dumb `DATA2` value (since they only need to report the pressing of a specific button) and maybe a different `STATUS` byte so that they don't get misunderstood as key pressings. You have to keep in mind that even when using standard MIDI messages, the device you are trying to script for might not follow what is written in this guide, and it's up to you to guess which messages relate to which features of your MIDI controller.

### 1.2. System Exclusive (SysEx) messages

SysEx messages are the most interesting yet more complex and harder to reverse-engineer but the ones behind most of the features we love from MIDI controllers.

They are made out of several "header" bytes, a data chunk of unlimited lenght and an ending byte:

| Byte name       | Description                                                                                                                                                                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Init byte       | It is used to open every SysEx message. Its value is always `F0`.                                                                                                                                                                                                 |
| Manufacturer ID | Can take either 1 byte (`00`) or 3 bytes (`00 00 00`) on the message. Every single MIDI manufacturer is registered with the MIDI Association and has a unique ID. You can find them [here](https://www.midi.org/specifications-old/item/manufacturer-id-numbers). |
| Device ID       | This one is usually used for chain-connected MIDI devices, so that a SysEx message only targets one device of the chain rather than all of them. On MIDI over USB isn't normally used and it's default value is `01`.                                             |
| Model ID        | Should be unique for each device model the manufacturer makes. (assigned by the manufacturer)                                                                                                                                                                     |
| Command ID      | It is usually used to specify what kind of information you are going to send/request to/from the device. (assigned by the manufacturer)                                                                                                                           |
| Arguments       | The actual body of the message you are sending. It has an unlimited lenght. (assigned by the manufacturer)                                                                                                                                                        |
| Ending byte     | It is used to close every SysEx message. Its value is always `F7`.                                                                                                                                                                                                |

Here's an example with `F0 00 20 29 02 18 0B 51 3F 29 00 F7`, which sets the colour of the RGB light of a pad to orange on the Novation Launchpad MK2 (HTML/HEX: `FFA500`, RGB: R255 G165 B000)

| Init byte | Manufacturer ID    | Device ID | Model ID      | Command ID                   | Arguments                                                                                                                                              | Ending byte |
|:---------:|:------------------:|:---------:|:-------------:|:----------------------------:|:------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------:|
| `F0`      | `00 20 09`         | `02`      | `18`          | `0B`                         | `51 3F 29 00`                                                                                                                                          | `F7`        |
|           | Focusrite/Novation | Launchpad | Launchpad MK2 | Change LED colour (RGB mode) | The `DATA1` number of the 1st pad on the Session mode (`51`), and the RGB data of the colour in hex bytes scaled down from 0-255 to 0-63 (`3F 29 00`). |             |
