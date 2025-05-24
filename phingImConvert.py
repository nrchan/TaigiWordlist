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

#reverse dict of tone_dict
num_dict = {
    ("A", "2"): "Á",
    ("E", "2"): "É",
    ("I", "2"): "Í",
    ("O", "2"): "Ó",
    ("U", "2"): "Ú",
    ("M", "2"): "Ḿ",
    ("N", "2"): "Ń",
    ("a", "2"): "á",
    ("e", "2"): "é",
    ("i", "2"): "í",
    ("o", "2"): "ó",
    ("u", "2"): "ú",
    ("m", "2"): "ḿ",
    ("n", "2"): "ń",

    ("A", "3"): "À",
    ("E", "3"): "È",
    ("I", "3"): "Ì",
    ("O", "3"): "Ò",
    ("U", "3"): "Ù",
    ("M", "3"): "M̀",
    ("N", "3"): "Ǹ",
    ("a", "3"): "à",
    ("e", "3"): "è",
    ("i", "3"): "ì",
    ("o", "3"): "ò",
    ("u", "3"): "ù",
    ("m", "3"): "m̀",
    ("n", "3"): "ǹ",

    ("A", "5"): "Â",
    ("E", "5"): "Ê",
    ("I", "5"): "Î",
    ("O", "5"): "Ô",
    ("U", "5"): "Û",
    ("M", "5"): "M̂",
    ("N", "5"): "N̂",
    ("a", "5"): "â",
    ("e", "5"): "ê",
    ("i", "5"): "î",
    ("o", "5"): "ô",
    ("u", "5"): "û",
    ("m", "5"): "m̂",
    ("n", "5"): "n̂",

    ("A", "6"): "Ǎ",
    ("E", "6"): "Ě",
    ("I", "6"): "Ǐ",
    ("O", "6"): "Ǒ",
    ("U", "6"): "Ǔ",
    ("M", "6"): "M̌",
    ("N", "6"): "Ň",
    ("a", "6"): "ǎ",
    ("e", "6"): "ě",
    ("i", "6"): "ǐ",
    ("o", "6"): "ǒ",
    ("u", "6"): "ǔ",
    ("m", "6"): "m̌",
    ("n", "6"): "ň",

    ("A", "7"): "Ā",
    ("E", "7"): "Ē",
    ("I", "7"): "Ī",
    ("O", "7"): "Ō",
    ("U", "7"): "Ū",
    ("M", "7"): "M̄",
    ("N", "7"): "N̄",
    ("a", "7"): "ā",
    ("e", "7"): "ē",
    ("i", "7"): "ī",
    ("o", "7"): "ō",
    ("u", "7"): "ū",
    ("m", "7"): "m̄",
    ("n", "7"): "n̄",

    ("A", "8"): "A̍",
    ("E", "8"): "E̍",
    ("I", "8"): "I̍",
    ("O", "8"): "O̍",
    ("U", "8"): "U̍",
    ("M", "8"): "M̍",
    ("N", "8"): "N̍",
    ("a", "8"): "a̍",
    ("e", "8"): "e̍",
    ("i", "8"): "i̍",
    ("o", "8"): "o̍",
    ("u", "8"): "u̍",
    ("m", "8"): "m̍",
    ("n", "8"): "n̍",

    ("A", "9"): "A̋",
    ("E", "9"): "E̋",
    ("I", "9"): "I̋",
    ("O", "9"): "Ő",
    ("U", "9"): "Ű",
    ("M", "9"): "M̋",
    ("N", "9"): "N̋",
    ("a", "9"): "a̋",
    ("e", "9"): "e̋",
    ("i", "9"): "i̋",
    ("o", "9"): "ő",
    ("u", "9"): "ű",
    ("m", "9"): "m̋",
    ("n", "9"): "n̋",
}

def toneSeperation(s):
    #split the string into syllables level
    syls = re.split("([^0-9a-zA-ZÁÉÍÓÚḾŃáéíóúḿńÀÈÌÒÙM̀Ǹàèìòùm̀ǹÂÊÎÔÛM̂N̂âêîôûm̂n̂ǍĚǏǑǓM̌Ňǎěǐǒǔm̌ňĀĒĪŌŪM̄N̄āēīōūm̄n̄A̍E̍I̍O̍U̍M̍N̍a̍e̍i̍o̍u̍m̍n̍A̋E̋I̋ŐŰM̋N̋a̋e̋i̋őűm̋n̋o͘ⁿ]+)", s)
    syls = list(filter(lambda x: x != "", syls))
    return syls

def toneToNum(syls):
    #move tone number to the back of the syllable
    for i in range(len(syls)):

        if len(syls[i]) == 0:
            continue

        if re.fullmatch("([^0-9a-zA-ZÁÉÍÓÚḾŃáéíóúḿńÀÈÌÒÙM̀Ǹàèìòùm̀ǹÂÊÎÔÛM̂N̂âêîôûm̂n̂ǍĚǏǑǓM̌Ňǎěǐǒǔm̌ňĀĒĪŌŪM̄N̄āēīōūm̄n̄A̍E̍I̍O̍U̍M̍N̍a̍e̍i̍o̍u̍m̍n̍A̋E̋I̋ŐŰM̋N̋a̋e̋i̋őűm̋n̋o͘ⁿ]+)", syls[i]):
            continue

        if re.fullmatch("([0-9]+)", syls[i]):
            continue

        if syls[i][-1] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
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

    return syls

def numToTone(syls):
    #move tone number to appropiate place
    for i in range(len(syls)):

        if len(syls[i]) == 0:
            continue

        if re.fullmatch("([^0-9a-zA-ZÁÉÍÓÚḾŃáéíóúḿńÀÈÌÒÙM̀Ǹàèìòùm̀ǹÂÊÎÔÛM̂N̂âêîôûm̂n̂ǍĚǏǑǓM̌Ňǎěǐǒǔm̌ňĀĒĪŌŪM̄N̄āēīōūm̄n̄A̍E̍I̍O̍U̍M̍N̍a̍e̍i̍o̍u̍m̍n̍A̋E̋I̋ŐŰM̋N̋a̋e̋i̋őűm̋n̋o͘ⁿ]+)", syls[i]):
            continue

        if re.fullmatch("([0-9]+)", syls[i]):
            continue

        #get the tone number, it is assumed that the tone number is the only number at the back of the syllable
        tone_num = syls[i][-1]
        #since we've got the tone number, we can remove it from the syllable (along with all other numbers)
        syls[i] = re.sub("[0-9]", "", syls[i])
        #if the last character is not tone number, skip
        #if the tone is 1 or 4, we also skip
        if tone_num not in ["2", "3", "5", "6", "7", "8", "9"]:
            continue

        #Adding tone is a complicated process, we will check each rule in their designated order (all case-insensitive)
        #Once a rule is matched, we will add the tone and move to the next syllable

        #Deal with exception first
        #Add tone to "i" in "aih8"
        if "aih" in syls[i].lower() and tone_num == "8":
            #get the index of the "i"
            index = syls[i].lower().index("aih") + 1
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue


        #Rule 1: Add tone to the first "a"
        if "a" in syls[i].lower():
            #get the index of the first "a"
            index = syls[i].lower().index("a")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

        #Rule 2: Add tone to the first "o" of "oo"
        if "oo" in syls[i].lower():
            #get the index of the first "o"
            index = syls[i].lower().index("o")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

        #Rule 3: Add tone to the first "e" of "ere"
        if "ere" in syls[i].lower():
            #get the index of the first "e"
            index = syls[i].lower().index("ere") + 2
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

        #Rule 4: Add tone to the first "e" or "o"
        if "e" in syls[i].lower():
            #get the index of the first "e"
            index = syls[i].lower().index("e")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue
        if "o" in syls[i].lower():
            #get the index of the first "o"
            index = syls[i].lower().index("o")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

        #Rule 5: Add tone to the second charcter of "iu" or "ui"
        if "iu" in syls[i].lower():
            #get the index of the second character
            index = syls[i].lower().index("iu") + 1
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue
        if "ui" in syls[i].lower():
            #get the index of the second character
            index = syls[i].lower().index("ui") + 1
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

        #Rule 6: Add tone to the first "i" or "u"
        if "i" in syls[i].lower():
            #get the index of the first "i"
            index = syls[i].lower().index("i")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue
        if "u" in syls[i].lower():
            #get the index of the first "u"
            index = syls[i].lower().index("u")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

        #Rule 7: Add tone to the "n" in "ng"
        if "ng" in syls[i].lower():
            #get the index of the "n"
            index = syls[i].lower().index("ng")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

        #Rule 8: Add tone to "m"
        if "m" in syls[i].lower():
            #get the index of the "m"
            index = syls[i].lower().index("m")
            syls[i] = syls[i][:index] + num_dict[(syls[i][index], tone_num)] + syls[i][index+1:]
            continue

    return syls

def PhingImtoNUM(s):
    #split the string into syllables level
    syls = toneSeperation(s)
    #move tone number to the back of the syllable
    ret = toneToNum(syls)
    return ret

def NUMtoPhingIm(s):
    #split the string into syllables level
    syls = toneSeperation(s)
    #move tone number to appropiate place
    ret = numToTone(syls)
    return ret

def POJtoTL(s):
    syls = PhingImtoNUM(s)

    for i in range(len(syls)):
        if len(syls[i]) == 0:
            continue

        if re.fullmatch("([^0-9a-zA-ZÁÉÍÓÚḾŃáéíóúḿńÀÈÌÒÙM̀Ǹàèìòùm̀ǹÂÊÎÔÛM̂N̂âêîôûm̂n̂ǍĚǏǑǓM̌Ňǎěǐǒǔm̌ňĀĒĪŌŪM̄N̄āēīōūm̄n̄A̍E̍I̍O̍U̍M̍N̍a̍e̍i̍o̍u̍m̍n̍A̋E̋I̋ŐŰM̋N̋a̋e̋i̋őűm̋n̋o͘ⁿ]+)", syls[i]):
            continue

        syls[i] = syls[i].replace("o͘", "oo")
        syls[i] = syls[i].replace("o·", "oo")
        syls[i] = syls[i].replace("ch", "ts")
        syls[i] = syls[i].replace("chh", "tsh")
        syls[i] = syls[i].replace("oe", "ue")
        syls[i] = syls[i].replace("oa", "ua")
        syls[i] = syls[i].replace("ek", "ik")
        syls[i] = syls[i].replace("eng", "ing")
        syls[i] = syls[i].replace("ⁿ", "nn")

    syls = numToTone(syls)

    return "".join(syls)

def TLtoPOJ(s):
    syls = PhingImtoNUM(s)

    for i in range(len(syls)):
        if len(syls[i]) == 0:
            continue

        if re.fullmatch("([^0-9a-zA-ZÁÉÍÓÚḾŃáéíóúḿńÀÈÌÒÙM̀Ǹàèìòùm̀ǹÂÊÎÔÛM̂N̂âêîôûm̂n̂ǍĚǏǑǓM̌Ňǎěǐǒǔm̌ňĀĒĪŌŪM̄N̄āēīōūm̄n̄A̍E̍I̍O̍U̍M̍N̍a̍e̍i̍o̍u̍m̍n̍A̋E̋I̋ŐŰM̋N̋a̋e̋i̋őűm̋n̋o͘ⁿ]+)", syls[i]):
            continue

        syls[i] = syls[i].replace("nn", "ⁿ")
        syls[i] = syls[i].replace("ⁿg", "nng") #sometimes nn is at the front, this only happens in "nng" (at least for what I have seen)
        syls[i] = syls[i].replace("ing", "eng")
        syls[i] = syls[i].replace("ik", "ek")
        syls[i] = syls[i].replace("ua", "oa")
        syls[i] = syls[i].replace("ue", "oe")
        syls[i] = syls[i].replace("tsh", "chh")
        syls[i] = syls[i].replace("ts", "ch")
        syls[i] = syls[i].replace("oo", "o͘")

    syls = numToTone(syls)

    return "".join(syls)

def TLtoHongIm(s):
    syls = PhingImtoNUM(s)

    #remove those that is space, dash or double dash
    syls = list(filter(lambda x: x not in [" ", "-", "--"], syls))

    for i in range(len(syls)):
        if len(syls[i]) == 0:
            continue

        if re.fullmatch("([^0-9a-zA-ZÁÉÍÓÚḾŃáéíóúḿńÀÈÌÒÙM̀Ǹàèìòùm̀ǹÂÊÎÔÛM̂N̂âêîôûm̂n̂ǍĚǏǑǓM̌Ňǎěǐǒǔm̌ňĀĒĪŌŪM̄N̄āēīōūm̄n̄A̍E̍I̍O̍U̍M̍N̍a̍e̍i̍o̍u̍m̍n̍A̋E̋I̋ŐŰM̋N̋a̋e̋i̋őűm̋n̋o͘ⁿ]+)", syls[i]):
            continue

        syls[i] = re.sub(r"m(?=[^0-9 -])", "ㄇ", syls[i])
        syls[i] = re.sub(r"ng(?=[^0-9 -])", "ㄫ", syls[i])

        syls[i] = syls[i].replace("p8", "ㆴ̇")
        syls[i] = syls[i].replace("t8", "ㆵ̇")
        syls[i] = syls[i].replace("k8", "ㆻ̇")
        syls[i] = syls[i].replace("h8", "ㆷ̇")
        syls[i] = syls[i].replace("p4", "ㆴ")
        syls[i] = syls[i].replace("t4", "ㆵ")
        syls[i] = syls[i].replace("k4", "ㆻ")
        syls[i] = syls[i].replace("h4", "ㆷ")
        syls[i] = syls[i].replace("1", "")
        syls[i] = syls[i].replace("2", "ˋ")
        syls[i] = syls[i].replace("3", "˪")
        syls[i] = syls[i].replace("5", "ˊ")
        syls[i] = syls[i].replace("6", "ˋ")
        syls[i] = syls[i].replace("7", "˫")
        syls[i] = syls[i].replace("9", "ˊ")

        syls[i] = syls[i].replace("ph", "ㄆ")
        syls[i] = syls[i].replace("p", "ㄅ")

        syls[i] = syls[i].replace("b", "ㆠ")
        syls[i] = syls[i].replace("l", "ㄌ")

        syls[i] = re.sub(r"tsh(?=i)", "ㄑ", syls[i])
        syls[i] = syls[i].replace("tsh", "ㄘ")
        syls[i] = re.sub(r"ts(?=i)", "ㄐ", syls[i])
        syls[i] = syls[i].replace("ts", "ㄗ")
        syls[i] = syls[i].replace("th", "ㄊ")
        syls[i] = syls[i].replace("t", "ㄉ")

        syls[i] = re.sub(r"s(?=i)", "ㄒ", syls[i])
        syls[i] = syls[i].replace("s", "ㄙ")

        syls[i] = re.sub(r"j(?=i)", "ㆢ", syls[i])
        syls[i] = syls[i].replace("j", "ㆡ")

        syls[i] = syls[i].replace("am", "ㆰ")
        syls[i] = syls[i].replace("im", "ㄧㆬ")
        syls[i] = syls[i].replace("om", "ㆱ")
        syls[i] = syls[i].replace("m", "ㆬ")

        syls[i] = syls[i].replace("ang", "ㄤ")
        syls[i] = syls[i].replace("ong", "ㆲ")
        syls[i] = syls[i].replace("ing", "ㄧㄥ")
        syls[i] = syls[i].replace("ng", "ㆭ")

        syls[i] = syls[i].replace("ainn", "ㆮ")
        syls[i] = syls[i].replace("aunn", "ㆯ")
        syls[i] = syls[i].replace("ann", "ㆩ")
        syls[i] = syls[i].replace("enn", "ㆥ")
        syls[i] = syls[i].replace("inn", "ㆪ")
        syls[i] = syls[i].replace("onn", "ㆧ")
        syls[i] = syls[i].replace("unn", "ㆫ")
        syls[i] = syls[i].replace("an", "ㄢ")
        syls[i] = syls[i].replace("in", "ㄧㄣ")
        syls[i] = syls[i].replace("un", "ㄨㄣ")
        syls[i] = syls[i].replace("irn", "ㆨㄣ")
        syls[i] = syls[i].replace("n", "ㄋ")
        syls[i] = syls[i].replace("kh", "ㄎ")
        syls[i] = syls[i].replace("k", "ㄍ")
        syls[i] = syls[i].replace("g", "ㆣ")

        syls[i] = syls[i].replace("h", "ㄏ")
        syls[i] = syls[i].replace("oo", "ㆦ")
        syls[i] = syls[i].replace("or", "ㄛ")
        syls[i] = syls[i].replace("ee", "ㄝ")
        syls[i] = syls[i].replace("er", "ㄜ")
        syls[i] = syls[i].replace("ir", "ㆨ")
        syls[i] = syls[i].replace("ai", "ㄞ")
        syls[i] = syls[i].replace("au", "ㄠ")
        syls[i] = syls[i].replace("a", "ㄚ")
        syls[i] = syls[i].replace("e", "ㆤ")
        syls[i] = syls[i].replace("i", "ㄧ")
        syls[i] = syls[i].replace("o", "ㄛ")
        syls[i] = syls[i].replace("u", "ㄨ")

    return " ".join(syls)

def POJtoHongIm(s):
    syls = TLtoPOJ(s)
    return TLtoHongIm(syls)


if __name__ == "__main__":
    print(PhingImtoNUM("ㄅㆪ ㄆㄨㆤˊ"))

    # import pandas as pd

    # with open("TaigiDatabase.csv") as f:
    #     db = pd.read_csv(f)

    # for index, row in db.iterrows():
    #     input = row["TL"]
    #     output = TLtoPOJ(input)
    #     if POJtoTL(output) != row["TL"]:
    #         print(input, output, POJtoTL(output))