import pprint

message = 'There was something peculiar about his behaviour.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pprint(count)