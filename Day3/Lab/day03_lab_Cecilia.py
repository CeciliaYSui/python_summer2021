## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    try:
        t = txt.upper()
    except:
        raise TypeError("Input must be a string.")
    return t

# shout("hello")
# shout(7)

## reverse all characters in string
def reverse(txt):
    # s = []
    # for i in range(0,len(txt)):
    #     s.append(txt[-i]) # AttributeError: 'str' object has no attribute 'append'
    return txt[::-1]
# print(reverse("happy"))

## reverse word order in string
def reversewords(txt):
    # split 
    w = txt.split() # output a list of words, deliminated by space char
    return " ".join(w[::-1])
# print(reversewords("I am happy today"))

## reverses letters in each word
def reversewordletters(txt):
    w = reversewords(reverse(txt))
    # w = txt.split()
    # return " ".join(w[::-1])[::-1]
    return w
# print(reversewordletters("I am happy today"))



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.



import unittest

class TestLab(unittest.TestCase):

    def test_shout(self): 
        self.assertEqual("FOO", shout("foo"))

    def test_reverse(self):
        self.assertEqual("yppah", reverse("happy"))

    def test_reversewords(self):
        self.assertEqual("today happy am I", reversewords("I am happy today"))
    
    def test_reversewordletters(self):
        self.assertEqual("I ma yppah yadot", reversewordletters("I am happy today"))


# if you want to run the test with this script
# if __name__ == '__main__': 
#     unittest.main()



string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

# 

def reverse_list(l):
    # new output list
    out_list = []
    for i in range(0,len(l)):
        try: 
            item = reverse(l[i])
        except TypeError:
            # continue
            item =  None
            print("There was a nonstring item in place {}".format(i))
        finally:
            if item != None:
                out_list.append(item)
    return out_list

print(reverse_list(string_list))
            




