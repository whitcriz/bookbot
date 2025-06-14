
def count_words(file_contents):
    return len(file_contents.split())

def count_characters(file_contents):
    file_contents = file_contents.lower()
    character_counts = {}
    for character in file_contents:
        if character in character_counts:
            character_counts[character] += 1
        else:
            character_counts[character] = 1
        
    return character_counts

def sort_characters(character_counts):
    character_counts_list = []
    for character in character_counts:
        character_count_pairs = {}
        character_count_pairs["char"] = character
        character_count_pairs["num"] = character_counts[character]
        character_counts_list.append(character_count_pairs)
    return sorted(character_counts_list, key = lambda character: character["num"], reverse = True)





        