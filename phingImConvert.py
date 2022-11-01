import re
import sys

#every tone has vowels and M, N in both capital and small forms
tone_dict = {
    "Á": ("A", "2"),
    "É": ("E", "2"),
    "Í": ("I", "2"),
    "Ó": ("O", "2"),
    "Ú": ("U", "2"),
    "Ḿ": ("M", "2"),
    "Ń": ("N", "2"),
    "á": ("a", "2"),
    "é": ("e", "2"),
    "í": ("i", "2"),
    "ó": ("o", "2"),
    "ú": ("u", "2"),
    "ḿ": ("m", "2"),
    "ń": ("n", "2"),

    "À": ("A", "3"),
    "È": ("E", "3"),
    "Ì": ("I", "3"),
    "Ò": ("O", "3"),
    "Ù": ("U", "3"),
    "M̀": ("M", "3"),
    "Ǹ": ("N", "3"),
    "à": ("a", "3"),
    "è": ("e", "3"),
    "ì": ("i", "3"),
    "ò": ("o", "3"),
    "ù": ("u", "3"),
    "m̀": ("m", "3"),
    "ǹ": ("n", "3"),

    "Â": ("A", "5"),
    "Ê": ("E", "5"),
    "Î": ("I", "5"),
    "Ô": ("O", "5"),
    "Û": ("U", "5"),
    "M̂": ("M", "5"),
    "N̂": ("N", "5"),
    "â": ("a", "5"),
    "ê": ("e", "5"),
    "î": ("i", "5"),
    "ô": ("o", "5"),
    "û": ("u", "5"),
    "m̂": ("m", "5"),
    "n̂": ("n", "5"),

    "Ǎ": ("A", "6"),
    "Ě": ("E", "6"),
    "Ǐ": ("I", "6"),
    "Ǒ": ("O", "6"),
    "Ǔ": ("U", "6"),
    "M̌": ("M", "6"),
    "Ň": ("N", "6"),
    "ǎ": ("a", "6"),
    "ě": ("e", "6"),
    "ǐ": ("i", "6"),
    "ǒ": ("o", "6"),
    "ǔ": ("u", "6"),
    "m̌": ("m", "6"),
    "ň": ("n", "6"),

    "Ā": ("A", "7"),
    "Ē": ("E", "7"),
    "Ī": ("I", "7"),
    "Ō": ("O", "7"),
    "Ū": ("U", "7"),
    "M̄": ("M", "7"),
    "N̄": ("N", "7"),
    "ā": ("a", "7"),
    "ē": ("e", "7"),
    "ī": ("i", "7"),
    "ō": ("o", "7"),
    "ū": ("u", "7"),
    "m̄": ("m", "7"),
    "n̄": ("n", "7"),

    "A̍": ("A", "8"),
    "E̍": ("E", "8"),
    "I̍": ("I", "8"),
    "O̍": ("O", "8"),
    "U̍": ("U", "8"),
    "M̍": ("M", "8"),
    "N̍": ("N", "8"),
    "a̍": ("a", "8"),
    "e̍": ("e", "8"),
    "i̍": ("i", "8"),
    "o̍": ("o", "8"),
    "u̍": ("u", "8"),
    "m̍": ("m", "8"),
    "n̍": ("n", "8"),

    "A̋": ("A", "9"),
    "E̋": ("E", "9"),
    "I̋": ("I", "9"),
    "Ő": ("O", "9"),
    "Ű": ("U", "9"),
    "M̋": ("M", "9"),
    "N̋": ("N", "9"),
    "a̋": ("a", "9"),
    "e̋": ("e", "9"),
    "i̋": ("i", "9"),
    "ő": ("o", "9"),
    "ű": ("u", "9"),
    "m̋": ("m", "9"),
    "n̋": ("n", "9"),
}

def toneSeperation(s):
    #split the string into syllables level
    syls = re.split("[ \-]+", s)
    if "" in syls:
        syls.remove("")
    return syls

def toneToNum(syls):
    #move tone number to the back of the syllable
    for i in range(len(syls)):

        if len(syls[i]) == 0:
            continue

        found = False
        for tone, seperated in tone_dict.items():
            if tone in syls[i]:
                syls[i] = syls[i].replace(tone, seperated[0])
                syls[i] += seperated[1]
                found = True
                break
        
        if not found:
            if syls[i][-1] in ["P", "T", "K", "H", "p", "t", "k", "h"]:
                syls[i] += "4"
            else:
                syls[i] += "1"

    ret = ""
    for i in range(len(syls)-1):
        ret += syls[i] + " "
    ret += syls[-1]
    return ret.lower()

def PhingImtoNUM(s):
    #split the string into syllables level
    syls = toneSeperation(s)
    #move tone number to the back of the syllable
    ret = toneToNum(syls)
    return ret

if __name__ == "__main__":
    print(PhingImtoNUM(sys.argv[1]))