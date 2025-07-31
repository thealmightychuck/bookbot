def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def counted_dict(text):
    new_list = []
    for k,v in text.items():
        temp_dict = {}
        temp_dict["char"] = k
        temp_dict["num"] = v
        new_list.append(temp_dict)
    new_list.sort(reverse=True, key=lambda items: items["num"])
    for value in new_list:
        if value["char"].isalpha():
            print(f"{value['char']}: {value['num']}")

def list_values(my_list):
    pass
