# Codeforces Contest Ratings Scraper

This project is a web scraping tool designed to collect and save contest ratings details from the Codeforces website for a specified contest round. The data is saved in a CSV file for easy access and analysis.

## Project Overview

This project uses Python's `requests` library to fetch web pages and `BeautifulSoup` to parse the HTML content. It extracts information about contest ratings, such as rank, name, points, rating, and rating change, and stores the data in a CSV file.

## Features

- Fetches contest ratings data for a specified contest round from Codeforces.
- Parses HTML content to extract contest rating details.
- Saves the extracted data into a CSV file.
- Supports user input for contest round and file name.
