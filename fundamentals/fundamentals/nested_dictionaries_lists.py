x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15 #Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
print(x)

students[0]['last_name'] = 'Bryant' #Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres' #In the sports_directory, change 'Messi' to 'Andres'
print(sports_directory)

z[0]['y'] = 30 #Change the value 20 in z to 30
print(z)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

for iterateDictionary in students:
    print(iterateDictionary)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDict(list,name):
    for val in range(len(list)):
        print(list[val][name])

iterateDict(students,'first_name')
iterateDict(students,'last_name')


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dictionary):  
    for key,val in dictionary.items(): 
        print(len(val),key.upper())
        for i in range(len(val)):
            print(val[i])

printInfo(dojo)
