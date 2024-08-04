# NiceGUI-primer

This project provides the plain text primer version of NiceGUI's documentation for usage with AI or as a portable offline file. 

Why? 

- NiceGUI is new compared to cut-off training dates of many AI LLM's
- while impressive being a dynamically created website for documentation, 
a text file is smaller, faster, easier to ingest by AI's

The [primer for NiceGUI](https://chatgpt.com/g/g-n2O45ylVT-nicegui-primer) is 
available for use as a GPT on OpenAI's GPT store. While it's offered as free 
to use by me; you may have to have a ChatGPT account ($'s).
> It turns out that there are several existing GPT's being offered.

Further information here:
- https://nicegui.io/
- https://nicegui.io/documentation
- https://github.com/zauberzeug/nicegui/
- https://github.com/zauberzeug/nicegui/blob/main/CONTRIBUTING.md#documentation

---


## 1. Install NiceGUI's documentation website for scraping

To avoid disturbing the nicegui.io online server, let's run the nicegui documenation website at: \
http://localhost:8080/ by doing the following:

> By the way, this was a very thoughtful option for the NiceGUI project to offer, so why not use it.

Clone the github repo or download the zip file:
```sh 
git clone nicegui
```

```sh
cd nicegui
```

Setup a virtual environment using conda or something:

```sh
conda create -n nicegui python=3.10
```

```sh
conda activate nicegui
```

Perhaps not all of the following are actually required, but this works:

```bash
python3 -m pip install -e .
```

```sh 
pip install itsdangerous prometheus_client isort docutils pandas plotly pyecharts matplotlib requests dnspython
```

Now launch `main.py` in the root directory:

```sh 
python -B main.py
```

---
  

## 2. Install NiceGUI-primer

Clone the github repo or download the zip file:
```sh
git clone https://github.com/cleesmith/NiceGUI-primer.git
```

```sh
cd NiceGUI-primer
```

Setup a virtual environment using conda or something:
> Also, other python versions may work, but I used 3.10.14:

```sh
conda create -n NiceGUI-primer python=3.10
```

```sh
conda activate NiceGUI-primer
```

---


## 3. Scrape NiceGUI documentation

Collect a list of the scrapable urls using Playwright with the Chromium option

```sh
cd NiceGUI-primer
```

```sh
pip install playwright
```

```sh
python -B 1_get_all_urls.py
```

---


## 4. Scrape using the list of urls into a text file
> This process also uses Playwright with the Chromium option

```sh
cd NiceGUI-primer
```

```sh
python -B 2_scrape_all_urls.py
```

---


# Thoughts

The online [NiceGUI documentation](https://nicegui.io/documentation) is great for 
humans, but not so great for AI. 

And the scraping process is affected by:
1. repeated links due to navigation which is helpful to humans; 
see #1 and #2 in the screenshot below
2. so many anchor links, such as: 
https://nicegui.io/documentation/section_text_elements#label 
i.e. it's the #label thing, and there are a lot of them in the doc's; 
see #3 in the screenshot below
3. the example display/output shown by executing the example code; 
see #4 in the screenshot below
> This example code, regardless of how it's executed, impacts page load time.

```sh
cd nicegui
```

After digging around in the source code, there are ways to turn off #1 and 
#2 (the nav bars) but there was no easy way found to stop #3 (anchor links) 
and #4 (code example display/output). Perhaps this is not possible, or 
just too much to ask, but a *command line arg* such as: *--honhuman* would 
certainly help with the scraping of the doc's to be feed to AI's.

```sh
python -B main.py --nonhuman
```

![NiceGUI Screenshot](nicegui_screenshot.png)

---

