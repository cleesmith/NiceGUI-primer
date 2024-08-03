# NiceGUI-primer
The plain text primer version of NiceGUI's documentation for usage with AI or as a portable offline file.

Clone the repo or download zip:
```sh
git clone https://github.com/cleesmith/NiceGUI-primer.git
```

```sh
cd NiceGUI-primer
```
Setup a virtual environment using conda or other:
```sh
conda create -n NiceGUI-primer python=3.10
```
> Also, other python version may work, but I used 3.10.14.
```sh
conda activate NiceGUI-primer
```

## Steps to scrape NiceGUI documentation

1. Run nicegui website at localhost:8080 to avoid bugging the nicegui.io server:
	```sh 
	git clone nicegui
	```
	```sh
	cd nicegui
	```
	Setup a virtual environment using conda or:
	```sh
	conda create -n nicegui python=3.10
	```
	```sh
	conda activate NiceGUI-primer
	```
	Perhaps not all of these lib's are not needed, but it works:
	```sh 
	pip install itsdangerous prometheus_client isort docutils pandas plotly pyecharts matplotlib requests dnspython
	```
	After cloning and pip'ing the NiceGUI repository, now launch `main.py` in the root directory:
	```sh 
	python -B main.py
	```

2. Collect all of the scrapable urls using Playwright via Chromium
	```sh
	pip install playwright
	```

	```sh
	python -B 1_get_all_urls.py
	```

3. Scrape the text from all urls into a text file

4. Scrape the text from all urls into a PDF file

