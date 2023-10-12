import csv

with open("./queries_test.csv", "w", newline="") as outcsv:
    writer = csv.writer(outcsv)
    writer.writerow(["index","sample_id","possible_answers","query_type","query","answer","image_name"])
    writer.writerow([0,0,["purple", "red", "green", "yellow"], None,"What color is the flower?","purple","flower.jpeg"])
    writer.writerow([0,0,["star","heart","square"], None ,"What shape does the flower resemble?","star","flower.jpeg"])