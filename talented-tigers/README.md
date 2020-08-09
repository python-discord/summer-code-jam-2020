# SpydirWeb

<p align="center">
  <img src="readme/coollogo.gif">
</p>

<p align="center">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/thaniel-c/summer-code-jam-2020">
    <img alt="GitHub" src="https://img.shields.io/github/license/thaniel-c/summer-code-jam-2020?color=%23009dff%20">
    <a href="https://discord.gg/python">
        <img src="https://img.shields.io/static/v1?label=Python%20Discord&logo=discord&message=%3E80k%20members&color=%237289DA&logoColor=white">
    </a>
</p>

Blast off to the past and surf the web 90s style! With SpydirWeb, you can browse a realistic version of the early internet! Get lost in hundreds of webpages, all generated with AI text generation, webscraping, and more! 

# Table of Contents
  * [Overview](#overview)
  * [Installation](#installation)
  * [License](#license)
  * [Authors](#Authors)

# Overview

**SpydirWeb** has three different types of pages: information pages, blog pages, and business pages. The blog and business pages use [openai's gpt-2](https://github.com/openai/gpt-2) AI to generate the content, while the info pages use the [wikipedia](https://pypi.org/project/wikipedia/) package. Images are gotten using the [Pixabay API](https://pixabay.com/api/docs/).

Click one of the three links listed on the home page to get started browsing Spydirweb.

![](readme/home.png)

Click any underlined link to continue browsing.

![](readme/info.png)

The text in the blog and business pages may take a while to load, as they are generated with an AI.

![](readme/blog.png)

And thats it. Have fun browsing!

![](readme/blogdone.png)
 
# License
MIT License

Copyright (c) 2020 Python Discord

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# Installation

For the judges, please check the `#talented-tigers` channel on the discord server.
Copy and paste the text block we sent into a file called `.env` in the `talented-tigers` directory.

For non-judges you'll need your own API key for Pixabay, which SpydirWeb use for collecting images. Go to [their website](https://pixabay.com/api/docs/) to get a key and then make a new file called `.env` with only 
```
API_KEY=your_key_here
```
written inside of it.

# Authors
<p align="center">
<a href="#" >
    <img src="readme/banner.png" alt="LogoMakr_5RDTOc" width=100%>
</a>
</p>

<sub>
<p align="center">
(Talented Tigers logo made by neon#9865, a helper on the <a href="https://pythondiscord.com/">Python Discord</a> </a> using <a href="https://logomakrcom">logomakr</a>)
</p></sub>
