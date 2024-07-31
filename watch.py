import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^<iframe.+?(?:https?://)?(?:www.)?youtu(?:.)?be(?:.com)?/(?:embed/)?(\w+).+</iframe>$", s):
        return "https://youtu.be/" + match.group(1)
    return None

if __name__ == "__main__":
    main()