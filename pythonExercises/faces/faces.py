def main():
    emoji=input("Emoji: ")
    print(convert(emoji))

def convert(emojiStr):
    new=emojiStr.replace(":)","🙂").replace(":(","🙁")

    return new


main()