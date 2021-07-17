print('hello')

from operator import itemgetter

data = [{'name': 'surya', 'dob':'12-05-1994','age':20},
        {'name': 'ram', 'dob':'12-06-1994','age':21}
        ]

##print(data)

data.sort(key=itemgetter('age'), reverse= True)
print(data)
