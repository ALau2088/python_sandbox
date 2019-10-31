# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members. Similar to object literal in JavaScript and hash in Ruby.

# Create dict
person = {
  'first_name': 'John',
  'last_name': 'Doe',
  'age': 30
}

# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')
# print(person, type(person2)) # {'first_name': 'John', 'last_name': 'Doe', 'age': 30} <class 'dict'> 

# Get value
print(person['first_name']) # John
print(person.get('last_name')) # Doe

# Add key/value
person['phone'] = '555-555-555'

# Get dict keys
print(person.keys()) # dict_keys(['first_name', 'last_name', 'age', 'phone'])

# Get dict items
print(person.items()) # dict_items([('first_name', 'John'), ('last_name', 'Doe'), ('age', 30), ('phone', '555-555-555')])

# Copy dict similar to spread operator in JS
person2 = person.copy()
person2['city'] = 'Boston'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
  {'name': 'Martha', 'age': 30},
  {'name': 'Kevin', 'age': 25 }
]

print(people[1]['name']) # Kevin