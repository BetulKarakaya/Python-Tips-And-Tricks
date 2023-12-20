def concatenate_strings(words):
    result = " ".join(words)
    return result

if __name__ == "__main__":
    word_list = ["This", "is", "how", "I", "use","join","function"]
    concatenated_string = concatenate_strings(word_list)
    
    print("Concatenated String:", concatenated_string)
