# web-scraping-challenge

This exercise builds a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

### The following outlines were performed:

1. Scraping: NASA Mars News, JPL Mars Space Images - Featured Image, Mars Facts, Mars Hemispheres
2. MongoDB and Flask Application: Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above

### How to run the codes:
1. Open Jupyter notebook "mission_to_mars" and run the codes for data scraping
2. Run app.py in Git Bash and open http://127.0.0.1:5000/ in the browser, click Scrape New Data. First time opening this web there is a blank page with only headlines, clicking Scrape bottom will pop the content.
3. **Note:** Sometimes first time launching the site and click "scrape" the page shows "can't be reached" while reloading, however the content shows up automatically once the code completes running. Please wait for a minute until the code finishes or click "Reload". If the code breaks in middle of running, just close the browser and reopen -> click scrape again. Once scrape succeed for one time it runs smoothly for all following scraps.
