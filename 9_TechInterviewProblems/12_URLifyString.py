"""
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the 'true' length of the string.

"""
input_test_str = 'Yulia Bezginova'
input_test_len = len(input_test_str)

def URLify(input_str, input_len):
    url = ''
    # looping through the string we are given
    for i in range(input_len):
        if input_str[i] == ' ':
            url += '%20'
        else:
            url = url + input_str[i]
    return url

print(URLify(input_test_str, input_test_len))
