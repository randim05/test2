children = {'Emily': 'artist', 'Adam': 'astronaut', 'Nancy': 'programmer'}
children['Emily'] = dict(profession=children['Emily'])
children['Emily']['age'] = 5
children['Adam'] = dict(profession=children['Adam'])
children['Adam']['age'] = 9
children['Nancy'] = dict(profession=children['Nancy'])
children['Nancy']['age'] = 14
print(children)

children = {'Emily': {'profession': 'artist', 'age': 5},
            'Adam': {'profession': 'astronaut', 'age': 9},
            'Nancy': {'profession': 'programmer', 'age': 14}}
