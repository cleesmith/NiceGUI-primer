# NiceGUI-primer
The plain text primer version of NiceGUI's documentation for usage with AI or as a portable offline file.

Further information here:
- https://nicegui.io/
- https://nicegui.io/documentation
- https://github.com/zauberzeug/nicegui/
- https://github.com/zauberzeug/nicegui/blob/main/CONTRIBUTING.md#documentation

---

## Steps to install NiceGUI's documentation website for later scraping

To avoid bugging the nicegui.io online server, I run the nicegui documenation website at http://localhost:8080/ by doing the following:

> By the way, this was a very thoughtful option for the NiceGUI project to offer, so why not use it.

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

Perhaps not all of these lib's are not needed, but it works:

```sh 
pip install itsdangerous prometheus_client isort docutils pandas plotly pyecharts matplotlib requests dnspython
```

After cloning and pip installs for the NiceGUI repository

Now launch `main.py` in the root directory:

```sh 
python -B main.py
```

---

## Steps to install NiceGUI-primer

Clone the repo or download zip file:
```sh
git clone https://github.com/cleesmith/NiceGUI-primer.git
```

```sh
cd NiceGUI-primer
```
Setup a virtual environment using conda or something:
```sh
conda create -n NiceGUI-primer python=3.10
```
> Also, other python versions may work, but I used 3.10.14.
```sh
conda activate NiceGUI-primer
```

---

## Steps to scrape NiceGUI documentation


---

2. Collect a list of the scrapable urls using Playwright with Chromium option

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

3. Scrape using the list of scrapable urls into a text file
	> also uses Playwright with Chromium option

	```sh
	cd NiceGUI-primer
	```

	```sh
	python -B 2_????.py
	```

---

