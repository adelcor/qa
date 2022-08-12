import requests
import sys
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_values():
    url = "https://z3n42.github.io"
    resp = requests.get(url=url)
    data = resp.json()
    return (data.values())

def scrap_title(website):
    driver = webdriver.Firefox()
    driver.get(website)
    title = driver.title
    driver.quit()
    return title

def get_args():
    parser = argparse.ArgumentParser(description='Json Explorer')
    parser.add_argument('-n', '--name', nargs=1)
    parser.add_argument('-t', '--type', nargs=1)
    parser.add_argument('-l', '--language', nargs='*')
    parser.add_argument('-o', '--owner', nargs=1)
    parser.add_argument('-c', '--country', nargs=1)
    parser.add_argument('-w', '--website', nargs=1)
    return (parser.parse_args()) 

class Parser:
    def __init__(self, lista, args):
        self.lista = lista
        self.args = args

    def search(self):
            
            box = list()

            for x in self.lista:
                if self.args.type:
                    if x['Type'] in self.args.type:
                        box.append(x['Name'])
                if self.args.name:        
                    if x['Name'] in self.args.name:
                        box.append(x)
                if self.args.language:
                    for i in x['Language']:
                        if i in self.args.language:
                            box.append(x['Name'])
                if self.args.owner:
                    if x['Owner'] in self.args.owner:
                        box.append(x['Name'])
                if self.args.country:
                    if x['Country'] in self.args.country:
                        box.append(x['Name'])
                if self.args.website:
                    if x['Website'] in self.args.website:
                        box.append(x['Name'])
                        box.append(scrap_title(x['Website']))
            print(box)
            return(box)

if len(sys.argv) == 1:
    print("input error")
    exit()

args = get_args()
lista = get_values()

test = Parser(lista, args)
test.search()
