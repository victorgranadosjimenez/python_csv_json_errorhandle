import csv

moviesfile = open("imdbtitles.csv", "r")

movies_list = moviesfile.readlines()
moviesfile.close()

print(movies_list[1])

