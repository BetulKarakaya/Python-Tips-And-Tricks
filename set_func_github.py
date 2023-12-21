
def remove_duplicates(test_list):
    unique_set = set(test_list)
    return list(unique_set)


if __name__ == "__main__":

    test_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9, 9, 10]
    test_list2 = ["a","b","c","d","e","f","f","g","a","b","e"]
    test_list3 = ["test","test1","test","test2","test2"]
    
    print("Original Test List:", test_list)   
    print(f"Test List with Duplicate Values Removed: {remove_duplicates(test_list)} \n")

    print("Original Test List:", test_list2)
    print(f"Test2 List with Duplicate Values Removed: {remove_duplicates(test_list2)} \n")

    print("Original Test List:", test_list3)
    print(f"Test3 List with Duplicate Values Removed: {remove_duplicates(test_list3)} \n")
