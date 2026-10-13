def convert(s):
    s = s.replace(":)" , "🙂")
    s = s.replace(":(" , "🙁")
    return s

def main ():
    p = input("type your face-")
    print(convert(p))

main()
