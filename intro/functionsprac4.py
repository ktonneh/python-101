'''
Write a python function to remove a given word from a list ad strip it at the same time.
'''

def remove_from_list(words,word_to_remove):
    # for word in words:
    #     if word.strip() != word_to_remove:
    #         continue
    return [word for word in words if word.strip() != word_to_remove]

words = ["  apple  ", "banana", "  cherry  ", "  apple  "]
print(remove_from_list(words,"apple"))