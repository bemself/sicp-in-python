"""
replace certain contents in a file" Originated for Anki import
2019-01-19 init 1h: %
2019-01-19 add line break "---"

"""
import argparse

files = [
#{"file_name":"/Users/wanjia/Flashcard Decks/伤寒论全部条文.md"},
#{"file_name":"/Users/wanjia/Flashcard Decks/金匮要略背诵条文.md"},
# {"file_name":"/Users/wanjia/Flashcard Decks/刘希彦注解伤寒论.md","s1":"原文：","s2":"注解："}
{"file_name":"/Users/wanjia/Flashcard Decks/医理真传.md","s1":"问曰：","s2":"答曰："}
]

def replace(text, old, new):
    return str.replace(text, old, new)

for dic in files:
    file_name = dic["file_name"]
    s1 = dic["s1"]
    s2 = dic["s2"]
    with open(file_name, "r+", encoding="utf-8") as f:
        contents = f.readlines()
        for index, content in enumerate(contents):
            #contents[index] = replace(content, "%", "\n%\n")
            contents[index] = replace(content, s1, "---\n"+s1)
            contents[index] = replace(contents[index], s2, "%\n"+s2)
        print(contents)
        f.writelines(contents)






