# Contributing guide

The guide is made using the open-source documentation tooling [Sphinx](https://www.sphinx-doc.org/) and the [reStructuredText](https://www.sphinx-doc.org/es/master/usage/restructuredtext/index.html) text format. Markdown is reserved for repository information and writter-oriented documentation, like this file. Markdown files don't render the same way as rST ones do on Sphinx, and telling Sphinx to detect `.md` files as documentation will make some files that don't belong to the guide itself (like this one) to be included with it when it shouldn't.

If you have an idea, please create a new GitHub issue, assign it a proper label and add as much information as possible about it in order to engage discussion.

## Guide structure

As of today, the guide is divided in three main sections:

- **Preamble:** Introductory section for people who aren't familiar with Python either directly working with MIDI devices.

- **MIDI scripting in FL Studio:** The actual section that will contain most of the theory and knowledge the guide will provide.

- **Tutorials:** More how-to oriented articles that should be organized in topics. As the number of tutorials rises, new categories may also get created for those new that don't fit in the already existing ones.
  
  - **MIDI:** Pure MIDI related tutorials for stuff like device diagnosis, MIDI messages, sniffing and so on.
  
  - **Exercises:** Articles to practice stuff learned in the guide. Articles on this section might get referenced at the end of each theory article.

Throughout the guide, hardware-specifics should be skipped when possible. Rather than stating which device is going to be used to explain a topic and then just write the entire article around that specific device, the guide should focus on the actual knowledge so people can then apply it indifferently of which device they have by giving hardware-agnostic instructions and arbitrary MIDI values will be used instead to make the explanation more easier to be applied for other MIDI devices

Example of a bad practice:

> In this article, we are going to talk about how to set colors on pads! On the Novation Launchpad MK3 you do it like this, like this and I also did this so I can also turn off the lights.

Example of a good practice:

> In this article, we are going to talk about how to handle the coloring of pads. Pads are hittable cushions usually used for clip triggering and live playing drums or percussive instruments that some devices like the Novation Launchpad or the Native Instruments Maschine controllers have.
> 
> These pads are usually arranged on a grid and have unique MIDI identifiers, being one of the most common methods used by manufacturers is assigning a unique DATA1 value to each pad so a single pad will always use the same DATA1 byte to send pressings to the host. However, exceptions may apply, such as devices with user-mappable pads, multiple pad "pages", modes or profiles.
> 
> From one device to another, the way to specify the colors changes and you will need to get to look out for that information. But what most devices have in common is that pad colors are usually set by sending a MIDI message with the same DATA1 byte as the one reported by the device on the pad press/release events, a DATA2 value that refers to a color from a predefined palette and a STATUS byte that is either a constant for setting colors and sending DAW integration messages, or multiple STATUS byte values can be used depending on the intensity of the light or the animation effect (blinking, fading in and out...).
> 
> In this article, a Novation Launchpad MK3 will be used to demonstrate how to set lights on pads, which has a 2x8 pad grid with two different pad modes and unique DATA1 values for each pad and mode. Just like with any other device with a pad layout, an array of values should be used to make accessing the MIDI value for each pad easier:
> 
> (Python code block with 2x8 arrays filled with arbitrary MIDI values)
> 
> Which in my device would be assigned like this:
> 
> (either a high quality PNG file or an SVG of a 2x8 grid with the same arbitrary values shown on the arrays exemplified above)

## Dependencies

- Python 3.7+

- Sphinx
  **Note:** Please install it from PyPI using:
  
  ```bash
  pip install -U Sphinx
  ```

- sphinx-typlog-theme
  
  ```bash
  pip install sphinx-typlog-theme
  ```

## Additional tooling

Although you can use any tools you want, some might work best than others for this project. Here are some software recommendations that are known to work well with this guide.

### Code editor

A code editor with reStructuredText support is recommended:

| Name                                                                                               | Additional extensions                                                                             | Notes                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Micsosoft Visual Studio Code](http://code.visualstudio.com/) // [VSCodium](https://vscodium.com/) | [reStructuredText](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext) | If asked, don't install the Snooty language server extension. IntelliSense support through Snooty on the reStructuredText extension is still experimental and often drops errors on each key pressing and marks certain Sphinx-specific directives such as `table` as bad written lines because it was made for docutils, not for Sphinx. |

### Web server

In order to actually see how the guide will behave when seen by the final reader, you will need a local web server software that will read the HTML build folder (`./_build/html`), map it to a local network port on your PC and allow you to read the guide on a web browser.

- [**Servez:**](https://greggman.github.io/servez/) A simple and easy-to-use open-source local web server. Just map the HTML output folder on the UI as the root path of the server ("Folder to Serve"), start the server and access `localhost:8080` to read the guide.

### Diagrams and wireframes

In order to complement some explanations, diagrams and wireframes may be used.

| Name                                                | Notes                                                                                                                                                                                                                                                             |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [draw.io](https://github.com/jgraph/drawio-desktop) | Export diagrams as SVG files at diagram size, including images (if you did insert any) and a copy of your diagram (which will embed the draw.io project into the SVG file for further editing) and don't activate the transparent background and shadows options. |

### Images and videos

| Name                             | Notes                                                                                                                                                                                                                                                                                                                 |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ShareX](https://getsharex.com/) | Open-source tool for screenshots. Being way more advanced that the snipping tool, allows to add text and other elements without the need to open a dedicated image editor, record actions on screen and render them as animated GIF images and create screenshots out of scrolling screen elements. Only for Windows. |

### MIDI

| Name                                                     | Notes                                                                                                                                                                                                                                          |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Pocket MIDI](https://www.morson.jp/pocketmidi-webpage/) | Simple MIDI monitoring tool for macOS and Windows that displays the raw MIDI messages being sent/received by/from a device. Also has the ability to write and batch send multiple MIDI messages to a device using its System Exclusive window. |

## Formatting guidelines

### Titling

When choosing the name for a new `.rst` keep it concise and (if possible) unique. On the file itself, title formatting should be done this way:

```rst
===============
Main file title
===============

Level 1 header
==============

Level 2 header
--------------

Level 3 header
..............
```

If you have the need to create a new titling level, try to use a symbol that would be easily to detect by other people and make the level difference obvious.

### Whitespacing

Sphinx is very sensitive in terms of spacing and tabulation and lot of syntax elements and directive blocks in Sphinx use whitespaces to differ themselves from plain text, so it's important to get it properly done. While on Sphinx's official documentation they just use spaces ` `, you can actually use any whitespace you want. Because of this, whitespacing on the guide should be done using tabulation `    ` which is much easier to manage, navigate through and detect than just plain spacing characters.

- When declaring quote blocks or admonition directives such as `note`, you need to align the first characters of each line:
  
  ```rst
  .. note::   These two text lines
              will get rendered as a continuation of each other.
  
              These text lines will get
              rendered as a separate paragraph from the first two ones.
  ```

- When declaring quotes, use tabulation instead of regular spacing:
  
  ```rst
  Normal text
  
     Quoted text
  ```
  
  You might also need to separate a quote block from another directive block that got declared just before the quote. To do that, you can use a separator (`|`) to indicate Sphinx the separation between the two text blocks.
  
  ```rst
  .. note::   These two text lines
              will get rendered as a continuation of each other.
  
              These text lines will get
              rendered as a separate paragraph from the first two ones.
  
  |
  
      This is a
      quote block.
  
      With two
      paragraphs.
  ```

### Tables

Instead of declaring tables using the "standard" way by directly creating the table, the [`table`](https://docutils.sourceforge.io/docs/ref/rst/directives.html#table) directive should be used. This way table block declaration will be much clear and will allow to table properties such as `title` or `widths` to be used.

- Standard way of declaring tables:
  
  ```rst
  +------------------------+------------+----------+----------+
  | Header row, column 1   | Header 2   | Header 3 | Header 4 |
  | (header rows optional) |            |          |          |
  +========================+============+==========+==========+
  | body row 1, column 1   | column 2   | column 3 | column 4 |
  +------------------------+------------+----------+----------+
  | body row 2             | ...        | ...      |          |
  +------------------------+------------+----------+----------+
  ```

- Table declaration using the `table` directive, also declaring the `align` property:
  
  ```rst
  .. table:: <optional table name>
      :align: auto
  
      +------------------------+------------+----------+----------+
      | Header row, column 1   | Header 2   | Header 3 | Header 4 |
      | (header rows optional) |            |          |          |
      +========================+============+==========+==========+
      | body row 1, column 1   | column 2   | column 3 | column 4 |
      +------------------------+------------+----------+----------+
      | body row 2             | ...        | ...      |          |
      +------------------------+------------+----------+----------+
  ```

### Code blocks

rST has a dedicated block directive `code-block` for code chunks. You need to align the name of the directive with the first character of each line of code.

```rst
.. code-block:: python

   # Prints text to the console
   print("Hello World!")
```

### Links

reStructuredText uses two kinds of [hyperlinks](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#hyperlink-references): named and anonymous links. Avoid using named links as much as possible, as their text representation must be unique (you can't use the same text to represent two different links on a manual). Because of this, anonymous link declaration should be used as the default way to declare links.

```rst
.. Named reference link

`Title <http://link>`_

.. Anonymous reference link

`Title <http://link>`__
```

### Inserting files

For inserting additional files such as images or videos to be displayed on the guide, each folder with `.rst` files will also have an additional resources (`_resources`) folder. Inside this folder, there will be subfolders with the same name as the `.rst` files where the additional resources for each file will be located.

```
- _resources/
|--- doc1/
|  |--- image1.png
|  |--- diagram1.svg
|--- doc3/
   |--- image1.png
- doc1.rst
- doc2.rst
- doc3.rst
```

- **Images:**
  
  - The better the quality, the best.
  
  - If you are going to upload a simple self-made image you made with primitive geometrical shapes, then consider making a SVG image instead.

- **Videos:**
  
  - 4K resolution max. We don't want to get the guide to be heavy because of videos.
  
  - Videos will get tracked using Git LFS instead of Git (this is done automatically by detecting file extensions)
