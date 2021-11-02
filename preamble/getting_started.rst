========================
Before we get started...
========================

You have to keep in mind how familiar you are with Python (and programming, in general) before you get into reading the rest of this guide.

If you are already familiar with Python programming, you can straight up skip this and start reading the next section, but if you are new to either Python or programming, then this might help you to get a better understanding of it.

What is Python?
===============

Python is an open-source, high-level, object-oriented, interpreted and multiplatform programming language.

**Excuse me, what?**

A programming language is what you use to tell a computer what you want it to do. Pretty much like humans have English, French, Spanish, Chinese and so on, computers have their own ones, and that is what you use to make any piece of software. In the early days of computing, you had to directly tell orders that were more hardware-oriented, but nowadays you have way more better options than writing in `assembly <https://en.wikipedia.org/wiki/Assembly_language>`__. The "level" of the programming language you use is determined by how much it abstracts you from hardware control.

The more higher, the less hardware focused and more easier to use, but more likely to have worse performance since you don't have control over what's happening behind the scenes. The more lower, more hardware-focused and technical they get, so you have more precise control over how your software behaves, but they are more tedious to program on. It's a sacrifice between hardware control and ease of use.

In programming, there are multiple ways the instructions of your code can be executed depending on the programming language you use. The main two ways are procedurally and object-oriented.

In procedural programming languages like the well-known `C <https://en.wikipedia.org/wiki/C_(programming_language)>`__ your code is executed as some sort of "step-by-step instruction", going line to line right from the first one down to the last one (unless there's an error on your program and the execution breaks). This is okay for simple programs, but as a software gets more complicated, it can become a nightmare. And that's when **object**-oriented programming comes in: instead of your code being a literal instruction, it becomes a definition of multiple parts/modules where you tell what an object is capable of and what **attributes** it will have. On runtime, you generate (**instantiate**) objects out of those definitions (**classes**) that will have their own job on your software and communicate with each other to get your software working. However, you can also write procedural code on an object-oriented language.

When you have written a piece of code and you want to test it, you need to pass that code to a compiler since the your code is just plain text and your computer doesn't know what to do with it. The compiler (on languages that generate native code like C or C++, notice there are some exceptions like `Java <https://en.wikipedia.org/wiki/Java_compiler>`__) is a piece of software that translates those human-readable instructions you write using a "regular" programming language down to the lowest language possible: `machine code <https://en.wikipedia.org/wiki/Machine_code>`__. Do you remember Assembly? Well, this one is way more complicated, being the closest-to-hardware existing language and contains raw CPU instructions. This way, you can use the advantages of a human-readable language while performing as faster as possible when you use your software.

Python, in contrast to natively compiled languages where you run `binary executable files <https://en.wikipedia.org/wiki/Executable>`__, you directly run the source code file(s) (`.py` format) using the Python `interpreter <https://techterms.com/definition/interpreter>`__. When you write in Python you don't target the system, but the interpreter. And then the interpreter is the one that actually transposes the code you wrote to native instructions if needed, but native code is never generated. In fact, there's a Python compiler that optimizes the code to be initialized faster, but doesn't either improve performance or bypass the need of having the Python interpreter installed to run Python code.

And lastly, due to the fact that Python code is made to target the interpreter rather than a system, any platform compatible with Python's interpreter will be able to run your code. This is the reason Python is a multiplatform language.

Getting prepared for Python development and FL Studio MIDI scripting
====================================================================

The first thing you will need to properly code in Python is the Python interpreter. Even though Image-Line's documentation says it isn't necessary for making scripts for FL Studio (and they are right on that one), it is recommended to have it installed so you can get language integration features when using a code editor.

Since source code files are usually just text files that get interpreted by a compiler (and in case of Python, a interpreter that hot-reads the instructions), you can write code in any text editor like Windows' Notepad or Notepad++. But since these are done for general purpose and basic text editing, using them you will miss a lot of the optimizations a dedicated code editor can bring to you. Code completion, debugging features, syntax checking and extensions are just a few things that nowadays development tools bring to the equation.

To take it further, there `IDEs <https://en.wikipedia.org/wiki/Integrated_development_environment>`__ also exist, putting together a code editor and the rest of the tools you might be using (compilers, debuggers and so on) under the same umbrella. However, they are more complicated to setup and a bit overpowered for what we are going to do. So sticking with a code editor is the best option.

The editor this guide will reference is the open-source code editor `Visual Studio Code <https://code.visualstudio.com/>`__ by Microsoft. It's one of the most popular code editors among a wide range of developers due to how lightweight and versatile it is. If you don't like it for being a Microsoft software or you are weary about telemetry (even though you can disable it), you can also use `VSCodium <https://vscodium.com/>`__. Inside Visual Studio Code, you will also need to install the `Python language extension for Visual Studio Code <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`__.

Now that you are all set up, you can start learning Python programming. There are a lot of tutorials out there, but one of the best is the `W3schools' Python guide <https://www.w3schools.com/python/default.asp>`__. You can start reading it from the `Syntax <https://www.w3schools.com/python/python_syntax.asp>`__ page and it is advised that you read it at least until the `Math <https://www.w3schools.com/python/python_math.asp>`__ module page. Simply create a `.py` file using Visual Studio Code and start practicing by writing code. VS Code should detect your Python interpreter and running your code should be as simple as right-clicking your source code file on the *Browser* and then selecting *Run Python file on the terminal*.
