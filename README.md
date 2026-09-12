# Book Price Tracker

A Python script that checks the price of a book on books.toscrape.com
and tells you if it has changed since the last time you ran it.

## Setup

Install dependencies:
   pip3 install requests beautifulsoup4

## Usage

Run the script:
   python3 tracker.py

- On the first run, it saves the current price to `number.txt`.
- On every run after that, it compares the current price to the saved
  one and prints whether it changed.

## Notes

Currently tracks one specific book (hardcoded URL in the script). To
track a different book, change the `url` variable to that book's page
on books.toscrape.com.

This project is a demo built against a practice scraping site
(books.toscrape.com), made for learning web scraping. It doesn't
include automatic scheduling — you run it manually each time you want
to check.
