Written by Jacob Holm

#Clothing Website Webscraping Project

##Overview

This Python project uses web scraping techniques to gather product data from three different clothing websites. The scraped data is then organized, sorted by price from lowest to highest, and exported to Excel files for further analysis. This README provides an overview of the project, its purpose, and instructions on how to use and set it up.


##Prerequisites

Before running this project, ensure you have the following prerequisites:

- Python 3.x installed on your machine.
- Required Python libraries (BeautifulSoup, Pandas, Requests, Openpyxl) installed. You can install them using `pip` or `conda`.


## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/clothing-website-scraper.git


2. Navigate to the project directory

    cd clothing-website-scraper


3. Install the required Python libraries

    pip install -r requirements.txt




##Usage

1. Open one of the website folders
2. Select which type of clothing file you would like to scrape
3. Run the script (python (filename).py)
4. The data will be saved in Excel files, one for each website



##Project Structure

The project directory is structured as follows:

- BYLT: folder containing the python scripts that scrape the BYLT website
    - bylt_joggers.py: python script that scrapes the data for joggers
    - bylt_shirts.py: python script that scrapes the data for shirts
    - bylt_shorts.py: python script that scrapes the data for shorts
- Gymshark: folder containing the python scripts that scrape the Gymshark website
    - gymshark_pants.py: python script that scrapes the data for pants
    - gymshark_tops.py: python script that scrapes the data for shirts
    - gymshark_shorts.py: python script that scrapes the data for shorts
- YoungLa: folder containing the python scripts that scrape the YoungLa website
    - youngla_joggers.py: python script that scrapes the data for joggers
    - youngla_shirts.py: python script that scrapes the data for shirts
    - youngla_shorts.py: python script that scrapes the data for shorts
- bylt_data.xlsx: excel file that contains the scraped data from the BYLT website
- gymshark_data.xlsx: excel file that contains the scraped data from the Gymshark website
- youngla_data.xlsx: excel file that contains the scraped data from the YoungLa website
- requirements.txt: a list of Python dependencies rtequired for the project