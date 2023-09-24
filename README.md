# Play Store Game Scraper API

Play Store Game Scraper API! This effective program simplifies the procedure for obtaining thorough game statistics from the Google Play Store. This API allows you to quickly get information on games, including their names, developer addresses, versions, and a lot more. It was developed using the Google Play Scraper library. However, this helpful tool goes beyond games; in addition to streamlining procedures and assisting in the creation of fresh datasets, it also gives you the option to extract apps and other information from a number of different categories.

## Table of Contents

- [Directory Structure](#directory-structure)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Installing Dependencies](#installing-dependencies)
- [Usage](#usage)
  - [Running the Scraper](#running-the-scraper)
  - [Starting the API](#starting-the-api)
- [Feedback](#feedback)

## Directory Structure

Before we get started, let's have a quick look at the project's directory structure:

```
project-root/
│
├── json_data/ # Store scraped JSON data here
│
├── scraper_library.py # Python script for scraping and saving data
│
├── extra.py # Python script for continuous scraping
│
├── app.py # Flask web application for serving the API
│
├── README.md # You're reading it!
```

## Installation

Let's set up the environment to get you up and running.

### Prerequisites

Before you can use this project, you need to have the following software installed on your computer:

1. **MongoDB**: Ensure that you have MongoDB installed and running on your system. If you haven't installed it yet, follow the official [MongoDB installation guide](https://docs.mongodb.com/manual/installation/).

2. **Python**: Make sure you have Python 3.x installed. If not, download it from the [official Python website](https://www.python.org/downloads/).

### Installing Dependencies

Now, let's install the necessary Python packages. Open your terminal, navigate to the project directory, and execute the following command:

```
pip install -r requirements.txt
```

This will automatically install all the required packages for the scraper and API.
Usage

Great! We're all set up. Let's start using the Play Store Game Scraper API.
Running the Scraper

Open your terminal and navigate to the project directory.

To start the scraper, run the following command:

```

python scraper_library.py
```



This script will commence scraping game data from the Google Play Store and store it in your MongoDB database.

If you want to keep the scraper running continuously to collect new data, leave it running. To stop it, press Ctrl+C in the terminal.

Starting the API


> Ensure that your MongoDB instance is up and running.

>Open a new terminal window and navigate to the project directory.


Start the Flask API using this command:

```
python app.py
```


API is now live and accessible locally.

  To access a list of all the scraped games, open your web browser and visit 

     http://localhost:5000/api/apps
 
  You can also access individual game data by appending the game's title to the URL, e.g., http://localhost:5000/api/apps/Game-Title.

Feedback


I'm always open to questions, feedback, and suggestions. If you have any, feel free to reach out. Enjoy exploring the vast world of game data with this tool!


> Disclaimer: Please note that web scraping may be subject to terms of service and legal restrictions imposed by websites. Always ensure that your use of this library complies with Google Play's terms of service and any applicable laws and regulations.
