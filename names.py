students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_students(arr):
    for student in arr:
        name = ''
        for names in student.values():
             name += names + ' '
        print name


def print_users(users):
    for key, value in users.items():
        print key
        for indx in range(len(value)):
            name = value[indx]['first_name'] + ' ' + value[indx]['last_name']
            name = str(indx+1) + ' - ' + name + ' - ' + str(len(name)-1)
            print name
