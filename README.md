# NiceGUI-primer
 NiceGUI documentation to be used as a primer for AI usage.

cd NiceGUI-primer
conda create -n NiceGUI-primer python=3.10
conda activate NiceGUI-primer

## Steps to scrape NiceGUI documentation

1. run nicegui website at localhost:8080 to avoid bothering their server:
	- git clone nicegui
	- pip install itsdangerous prometheus_client isort docutils pandas plotly pyecharts matplotlib requests dnspython
	  ... maybe all of that is not needed, but it works
	- python -B main.py

2. collect all of the scrapable urls 
	- python -B 1_get_all_urls.py