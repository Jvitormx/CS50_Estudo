import emoji

def main():
    code=input("Input: ")
    emoji_vers(code)

def emoji_vers(word):
    print("Output: "+emoji.emojize(word))

main()
