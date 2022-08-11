import requests
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def scrap_title(website):
    driver = webdriver.Firefox()
    driver.get(website)
    title = driver.title
    driver.quit()
    print(title)


parser = argparse.ArgumentParser(description='Json Explorer')
parser.add_argument('-n', '--name', nargs=1)
parser.add_argument('-t', '--type', nargs=1)
parser.add_argument('-l', '--language', nargs='*')
parser.add_argument('-o', '--owner', nargs=1)
parser.add_argument('-c', '--country', nargs=1)
parser.add_argument('-w', '--website', nargs=1)
args = parser.parse_args() 

url = "https://z3n42.github.io"

c_line = sys.argv

if len(c_line) == 1:
    print("input error")
    exit()

resp = requests.get(url=url)

data = resp.json()
lista = data.values()

if args.type != None:
    for x in lista:
        if x['Type'] in args.type:
            print(x['Name'])

if args.name != None:
    for x in lista:
        if x['Name'] in args.name:
            print(x)

if args.language != None:
    for x in lista:
        for i in x['Language']:
            if i in args.language:
                print(x['Name'])

if args.owner != None:
    for x in lista:
        if x['Owner'] in args.owner:
            print(x['Name'])

if args.country != None:
    for x in lista:
        if x['Country'] in args.country:
            print(x['Name'])

if args.website != None:
    for x in lista:
        if x['Website'] in args.website:
            print(x['Name'])
            scrap_title(x['Website'])

print("\n")





