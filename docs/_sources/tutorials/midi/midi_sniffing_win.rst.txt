========================
MIDI sniffing on Windows
========================

On Windows, due to how MIDI is implemented, device assignations are exclusive. This means two software cannot connect to the same MIDI device at the same time. 
Trying to do this will result in an error on the 2nd software you are trying to connect saying other software is already using the device so the connection cannot 
be done. Because of this, doing man-in-the-middle MIDI sniffing on Windows isn't possible. At least in theory...

While the MIDI stack on Windows doesn't allow you to do so, you can go lower: the USB stack. You can monitor the USB messages being sent and received to/from your 
device using `Wireshark <https://www.wireshark.org/>`_ and `USBPcap <https://desowin.org/usbpcap/>`_. 

.. note:: Since this method directly captures raw USB data, it might not work if your manufacturer uses a proprietary driver that directly handles your device,
          as this article describes how to deal with MIDI messages that get directly sent and received from the device through USB and isn't intended to be 
          used with devices that require an intermediate piece of software between the controller and the DAW to handle their functionality. Trying to do so might 
          result in getting USB packets with a completely different set of data from the ones shown in this article.

Download the Wireshark installer, run it to install Wireshark and  when the installer asks you to install USBPcap, tell it to do so as well. 
After rebooting your PC, connect your MIDI device, run Wireshark as an administrator and you should be greeted with this:

.. image:: _resources/midi_sniffing_win/wireshark-1.png

|

What we will use is the *USBPcap1* capture interface. By default it will capture any USB data coming in and out of your PC, which is inconvenient for both inspection and 
privacy reasons (in case you want other people to look at the USB events you recorded.). To avoid this, we can tell Wireshark to only capture traffic related to specific 
device. On Wireshark's main page (the one shown above), click on the gear icon at the left of the USBPcap1 name on the list of capture interfaces to access its settings. 

1. Deselect *Capture from all devices connected*, *Capture from newly connected devices*, *Inject already connected devices descriptors into capture data* and everything 
   on the *Attached USB Devices* list as well.

2. The *Attached USB Devices* list contains all the physical USB devices connected to your PC (marked with ``[device_number]``), as well as any virtual device they generate.
   Look for your MIDI device by unfolding the different sub-lists based on this:

   * If you connected your device directly to your PC, then there's a high chance it will be one of the first few ones showing up on the root of the list.
    
     .. image:: _resources/midi_sniffing_win/wireshark-2.png

   * If you connected your device through something like a USB hub, then you will have to first unfold the sub-list of that USB hub before you get to see the actual MIDI device.
    
     .. image:: _resources/midi_sniffing_win/wireshark-3.png

3. Once you locate it, mark it and click on the *Start* button to start capturing USB traffic.
  
   .. image:: _resources/midi_sniffing_win/wireshark-4.png

|

Running a DAW the manufacturer of your device officially supports should start registering the MIDI messages happening between your device and the DAW. All the USB packets 
sent between your PC and your MIDI device will be monitored and shown in Wireshark.

.. image:: _resources/midi_sniffing_win/wireshark-5.png

|

.. table:: **USB packet properties relevant for MIDI sniffing**

   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | Name            | Example                  | Description                                                                                                                    |
   +=================+==========================+================================================================================================================================+
   | **Number**      | ``145``                  | The number of the packet.                                                                                                      |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | **Time**        | ``0.757612``             | Time of the message (measured in nanoseconds) since the 1st received message.                                                  |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | **Source**      | ``host``                 | The source of the message:                                                                                                     |
   |                 |                          |                                                                                                                                |
   |                 |                          | * ``host``: your PC                                                                                                            |
   |                 |                          |                                                                                                                                |
   |                 |                          | * ``1.device_number.port``: your USB MIDI device. ``port`` is the number of a virtual port from the USB device.                |
   |                 |                          |                                                                                                                                |
   |                 |                          |   * Port ``0`` is the USB descriptor. It has no use for us as it's something from the USB spec that is used just to describe   |
   |                 |                          |     the technical aspects of the device based on the USB protocol.                                                             |
   |                 |                          |                                                                                                                                |
   |                 |                          |   * Port ``1``, ``2``... are the different virtual devices your MIDI controller creates when it gets connected to a            |
   |                 |                          |     computer. Some of them might not be MIDI ports, so try not to use any proprietary software from the manufacturer           |
   |                 |                          |     to ensure only standard MIDI ports get contacted during the packet capture so you don't confuse USB packets containing     |
   |                 |                          |     actual MIDI events with other USB packets.                                                                                 |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | **Destination** | ``1.9.2``                | The device the message is being sent to. It follows the same scheme as the *Source* property.                                  |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | **Protocol**    | ``USB``                  | The protocol the packet is using.                                                                                              |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | **Length**      | ``31``                   | The length of the packet in bytes.                                                                                             |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | **Info**        | ``URB_INTERRUPT out``    | The USB transfer type.                                                                                                         |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
   | **Leftover**    | ``1bb02a6c``             | The actual information being sent on the message.                                                                              |
   | **Capture Data**|                          |                                                                                                                                |
   +-----------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+


All the USB packets (lines) with MIDI messages will have a *Leftover Capture Data* field on their details, which will contain the actual MIDI data. It will be structured with 
header and wrapper bytes each three MIDI bytes: ``HH mm mm mm HH mm mm mm HH mm mm mm HH mm ...``, where ``HH`` are the header/wrapper bytes and should be ignored when reading 
a USB packet's leftover data as a MIDI message. Following this, the MIDI message contained on the USB packet described on the table above isn't ``1B B0 2A 6C`` but ``B0 2A 6C``.

.. tip:: You can make *Leftover Capture Data* appear directly on the packets list, as well as any other packet properties, by right clicking on them on the details 
         view and selecting *Apply as Column*. This way, you won't have to click on a USB packet to see if it contains MIDI data or not.
