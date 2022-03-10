
"""
tool = {
    'python' : {
        '2015' : 9, 
        '2016' : 22, 
        '2017' : 27, 
        '2018' : 32,
        '2019' : 35
    }, 
    'javascript' : {
        '2015' : 8, 
        '2016' : 18, 
        '2017' : 12, 
        '2018' : 6,
        '2019' : 15
    }, 
    'twitter' : {
        '2015' : 10, 
        '2016' : 18, 
        '2017' : 26, 
        '2018' : 16,
        '2019' : 12
    },
    
}

#print(tool)
#print(tool['python']['2015'])
#print(tool['python']['2015'] + tool['python']['2016']
# + tool['python']['2017'] + tool['python']['2018'] + tool['python']['2019'])
toolname = 'twitter'
for key, value in tool.items() : 
    if key == toolname:
        print(key)
        print('tool name', key)
        print('tool value in 2015', value['2015'])
        print('tool value in 2019', value['2019'])
        print('total popularity count', value['2015'] + value['2016'] + value['2017']
        + value['2018'] + value['2019'])
    else: 
        print('not twitter')     
""""

jane = "The Project Gutenberg EBook of Pride and Prejudice, by Jane Austen This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever.  You may copy it, give it away or re-use it under the terms of the Project Gutenberg License included with this eBook or online at www.gutenberg.org Title: Pride and Prejudice Author: Jane Austen Posting Date: August 26, 2008 Release Date: June, 1998 Last Updated: March 10, 2018 Language: English Character set encoding: UTF-8 ***START OF THIS PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE*** Produced by Anonymous Volunteers PRIDE AND PREJUDICE By Jane Austen Chapter 1 It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."

x = jane.split("***")
jane_cleaned = x[2]
print(jane_cleaned)


#assignment 2 
#print content of csv file 
import csv
with open('tools_dh_proceedings.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


