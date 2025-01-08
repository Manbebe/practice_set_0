def main():
    emoticon = input("Yo type any emojicon and ill translate it into an emoji: ")
    emoticon = emoji(emoticon)

def emoji(emoticon):
    emoticon = emoticon.replace(":)", "🙂")
    emoticon = emoticon.replace(":(", "🙁")
    emoticon = emoticon.replace(":D", "😀")
    emoticon = emoticon.replace(":'(", "😢")
    emoticon = emoticon.replace("8=D", "🍆")
    print(f"Here is the emojicon translated to an emoji: {emoticon}")
    return emoticon


main()
