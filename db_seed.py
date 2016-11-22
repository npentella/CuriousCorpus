import gutenberg
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from app import Text
from app import db
from metainfo import *
import math
import csv
import random

md = readmetadata()

def load_text(gutenberg_id):
  text = strip_headers(load_etext(gutenberg_id)).strip()
  return text.encode('ascii', 'ignore')

def roundown_year(year):
  return int(math.floor(year/100.0)) * 100

def data_set_selector(counter):
  case = {
    1: "validation",
    3: "test",
  }
  return case.get(counter%5, 'train')

def initialize_book(book, counter):
  exists = db.session.query(Text.gutenberg_id).filter_by(gutenberg_id=book).scalar() is not None
  title = db.session.query(Text.title).filter_by(title=md[book]['title']).scalar() is not None
  if (not exists and not title):
    book_content = None
    while True:
      try:
        book_content = load_text(book)
        break
      except ValueError:
        print("Could not load ", book)
        break
    if (book_content != None):
      meta = md[book]
      new_text = Text(meta['title'], meta['author'], meta['authoryearofbirth'], roundown_year(meta['authoryearofbirth']), book_content, book, 0, data_set_selector(counter))
      db.session.add(new_text)
      db.session.commit()

with open('gutenberg_id_texts.csv', 'rb') as csvfile:
  counter = 0
  id_collection = csv.reader(csvfile)
  for row in id_collection:
    book = int(row[0])
    if (counter % 50 == 0):
      print ("Book processing:", book, counter)
    initialize_book(book, counter)
    counter += 1




