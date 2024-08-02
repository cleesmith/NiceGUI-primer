# NiceGUI-primer
 NiceGUI documentation to be used as a primer for AI usage.

cd NiceGUI-primer
conda create -n NiceGUI-primer python=3.10
conda activate NiceGUI-primer

## Steps to scrape NiceGUI documentation

1. run nicegui website at localhost:8080 to avoid bothering their server:
	```sh 
		git clone nicegui
	```
	```sh 
	  	pip install itsdangerous prometheus_client isort docutils pandas plotly pyecharts matplotlib requests dnspython
	```
	  ... maybe all of that is not needed, but it works
	```sh 
		python -B main.py
	```

2. collect all of the scrapable urls 
	```sh
	pip install playwright
	```

	```sh
	python -B 1_get_all_urls.py
	```

3. scrape the text from all urls into a text file

4. scrape the text from all urls into a PDF file