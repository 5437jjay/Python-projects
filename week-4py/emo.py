# A text to emoji convertor
import emoji
def emojy():
    import emoji

    print(" Some of the available emojis:")
    print("heart          -> ❤️")
    print("thumbs_up      -> 👍")
    print("fire           -> 🔥")
    print("star           -> ⭐")
    print("clap           -> 👏")
    print("rocket         -> 🚀")
    print("ok_hand        -> 👌")
    print("100            -> 💯")
    print("check_mark     -> ✅")
    print("cross_mark     -> ❌")

    emo=input("Enter the text you want to convert to emoji: ")
    emo=":" + emo + ":"
    print(emoji.emojize(emo))
emojy()
