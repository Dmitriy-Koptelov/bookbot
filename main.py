from pathlib import Path


def get_text() -> str:
    with Path.open("books/frankenstein.txt") as f:
        return f.read()

def count_symbols(text: str) -> dict[str, int]:
    out_dict = {}
    for letter in text:
        if letter.lower() in out_dict:
            out_dict[letter.lower()] += 1
        else:
            out_dict.update({letter.lower(): 1})
    return out_dict

def report(text: str) -> None:
    symdict = count_symbols(text)
    list_of_syms = [{"char": k, "num": v} for k,v in symdict.items()]
    list_of_syms.sort(reverse=True, key=lambda x: x["num"])
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(text.split())} words found in the document\n")
    for record in list_of_syms:
        if record["char"].isalpha():
            print(f"The '{record["char"]}' character was found {record["num"]} times")
    print("--- End report ---")

def main() -> None:
    text = get_text()
    report(text)

main()
