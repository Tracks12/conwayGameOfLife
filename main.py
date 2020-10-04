#!/bin/python3
# -*- coding: utf-8 -*-

from random import getrandbits, randint
from platform import system
from time import sleep
import json, os

class c:
	r = "\033[31m"
	b = "\033[34m"
	g = "\033[32m"
	e = "\033[0m"

def initMap(x, y):
	map = []
	for i in range(0, x):
		map.append([])
		for j in range(0, y):
			map[i].append(0)

	return map

def displayMap(map):
	for item in map:
		row = ""
		for value in item:
			if(value): row += "{}{}{}".format(c.g, u'\u2588', c.e)
			else: row += "{}{}{}".format(c.r, u'\u2588', c.e)

		print(row)

	return True

def update(map):
	if(system() == "Linux"): os.system('clear')
	else: os.system('cls')

	xmap = initMap(len(map), len(map[0]))

	for x in range(0, len(map)-1):
		for y in range(0, len(map[x])-1):
			xmap[x][y] = map[x][y]
			active = 0
			active += map[x-1][y-1]
			active += map[x-1][y]
			active += map[x-1][y+1]
			active += map[x][y-1]
			active += map[x][y+1]
			active += map[x+1][y-1]
			active += map[x+1][y]
			active += map[x+1][y+1]

			if((active == 3) or (map[x][y] and (active == 2))): xmap[x][y] = 1
			else: xmap[x][y] = 0

	with open("data.json", 'w') as outFile:
		json.dump(map, outFile)

	return xmap

def main():
	if(system() == "Linux"): os.system('clear')
	else: os.system('cls')

	try:
		with open("data.json") as inFile:
			map = json.load(inFile)

	except Exception:
		size = {
			"x": int(input("Hauteur de la map: ")),
			"y": int(input("Largeur de la map: "))
		}

		map = initMap(size["x"], size["y"])

	while(True):
		map = update(map)
		displayMap(map)
		sleep(.5)

if __name__ == "__main__":
	main()
