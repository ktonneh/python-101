
story = "this is my story this is my song"

print('story' in story)

print('Search with find')
print(f"Find story':  {story.find('story')}")
print(f"Find is':  {story.find('is',0,8)}")

new_story = story.replace(story,'this is my story this is my song, all the day long')

print(story)

str_lowercase = "this is awsome"
str_uppercase = "THIS IS UPPERCASE"

print(str_lowercase.upper())
print(str_uppercase.lower())


