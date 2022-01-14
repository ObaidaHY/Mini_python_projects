import time
import concurrent.futures
from allowed_characters import open_list
from allowed_characters import close_list

MAX_THREADS = 10
balanced_sentence_set = set()


def log_sentence(sentence):
    with open('temp.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def reverse_check(sentence):
    stack = []
    new_sentence = ""
    print("checking reverse balance for {}".format(sentence))
    for chara in sentence[::-1]:
        if chara not in open_list + close_list:
            new_sentence = chara + new_sentence
        if chara in close_list:
            stack.append(chara)
            new_sentence = chara + new_sentence
        elif chara in open_list:
            pos = open_list.index(chara)
            if ((len(stack) > 0) and
                    (close_list[pos] == stack[len(stack) - 1])):
                stack.pop()
                new_sentence = chara + new_sentence
            else:
                print("Excluding bracket at index ", sentence.find(chara))
    # check if after exclusion duplicates arise
    if len(stack) == 0 and new_sentence not in balanced_sentence_set:
        balanced_sentence_set.add(new_sentence)
        log_sentence(new_sentence)


def check_balance(sentence):
    stack = []
    new_sentence = ""
    print("check balance for {}".format(sentence))
    for chara in sentence:
        if chara not in open_list + close_list:
            new_sentence += chara
        if chara in open_list:
            stack.append(chara)
            new_sentence += chara
        elif chara in close_list:
            pos = close_list.index(chara)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
                new_sentence += chara
            else:
                print("Excluding bracket at index ", sentence.find(chara))
    # check if after exclusion duplicates arise
    if len(stack) == 0 and new_sentence \
            not in balanced_sentence_set:
        balanced_sentence_set.add(new_sentence)
        log_sentence(new_sentence)
    else:
        reverse_check(new_sentence)


def concurrent_run(sens):
    # bracket_list = ["（）席類製造）（", "（）席類製造", "（）席類{}製造", "席類製造（", "]席[類(製{造"]
    threads = min(MAX_THREADS, len(sens))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        # check if after delimiting, unbalanced bracket sentences arise
        executor.map(check_balance, sens)


def main():
    lines = []
    with open("example_sentences.txt", encoding='utf-8', errors='ignore') as file:
        for line in file:
            if "Title:" in line:
                continue
            lines.append(line.rstrip('\n').replace("―", "").replace("_", "").replace("＼", "")
                         .replace("／", "").replace("＊", "").replace("★", "").replace("●", "")
                         .replace("○", "").replace("▲", "").replace("△", "").replace("┐", "")
                         .replace("┌", "").replace("└", "").replace("┘", "").replace("├", "")
                         .replace("　", ""))

    # Create new line when relevant symbol is found
    body_text = ''.join(lines).replace("。", "。\n").replace("？", "？\n").replace("?", "?\n") \
        .replace("！", "！\n").replace("!", "!\n").replace("‼", "‼\n").replace("⁉", "⁉\n") \
        .replace("………", "…").replace("……", "…").replace("…", "…\n")
    sentences = body_text.split('\n')

    t0 = time.time()
    concurrent_run(sentences)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sentences)} stories.")


main()
