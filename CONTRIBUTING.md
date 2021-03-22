# Contributing guide

The guide is made using the open-source documentation tooling [Sphinx](https://www.sphinx-doc.org/) and the [reStructuredText](https://www.sphinx-doc.org/es/master/usage/restructuredtext/index.html) text format. Markdown is reserved for repository information and writter-oriented documentation, like this file. Markdown files don't render the same way as rST ones do on Sphinx, and telling Sphinx to detect `.md` files as documentation will make some files that don't belong to the guide itself (like this one) to be included with it when it shouldn't.

If you have an idea, please create a new GitHub issue, assign it a proper label and add as much information as possible about it in order to engage discussion.

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

### Code editor

A code editor with reStructuredText support is recommended:

| Name                                                                                               | Additional extensions                                                                             | Notes                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Micsosoft Visual Studio Code](http://code.visualstudio.com/) // [VSCodium](https://vscodium.com/) | [reStructuredText](https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext) | If asked, don't install the Snooty language server extension. IntelliSense support through Snooty on the reStructuredText extension is still experimental and often drops errors on each key pressing and marks certain Sphinx-specific directives such as `table` as bad written lines because it was made for docutils, not for Sphinx. |

### Web server

In order to actually see how the guide will behave when seen by the final reader, you will need a local web server software that will read the HTML build folder (`./_build/html`), map it to a local network port on your PC and allow you to read the guide on a web browser.

- [**Servez:**](https://greggman.github.io/servez/) A simple and easy-to-use open-source local web server. Just map the HTML output folder on the UI as the root path of the server ("Folder to Serve"), start the server and access `localhost:8080` to read the guide.

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
