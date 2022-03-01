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
        