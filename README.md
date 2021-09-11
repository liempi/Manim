# Manim
Hello! Here you would find some animations that I made in **Manim**.

Hola! Aquí iré dejando algunas animaciones que he hecho en **Manim**.

I'm currently using **MacOs** but before I worked with **Windows** and **Linux**, so I would help you if you couldn't install them.

# Installation
## MacOS
### Pre-requirements
* **Python 3.x**

If you don't have **Python** already you should consider install from the official web-site.

https://www.python.org/downloads/macos/

Here just click the appropiated version of your **MacOs**. If you are not sure, don't worry, go to the terminal and type:

<pre><code> uman -m
</code></pre>

You will see the **arch** of your system like this:

<pre><code> x86_64
</code></pre>

If you wanna see information about your **processor**:

<pre><code> sysctl -a | grep machdep.cpu.brand_string
</code></pre>

In my case, this returned:

<pre><code> Intel(R) Core(TM) i5-6267U CPU @ 2.90GHz
</code></pre>

Now, you are able to download the correct version of **Python** for your system!

When it's already downloaded, double-click python.mpkg and follow the instructions, after the installation is completed, you see an Install Succeeded dialog box.

* **Homebrew**

I recommend to install the  **Homebrew** package because this is a easy way to install the dependecies used in Manim. Just copy & paste the next line in your terminal and follow the instructions.

<pre><code> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
</code?</pre>
