import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = 'https://www.hubertiming.com/results/2018MLK'
html = urlopen(url)

soup = BeautifulSoup(html, features="html.parser")