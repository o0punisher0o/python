import requests, psycopg2
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
conn = psycopg2.connect("dbname=pyhon user=postgres password=LKsd25sf35df221")
cur = conn.cursor()


from sweater import models, routes