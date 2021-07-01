import time
import concurrent.futures
from allowed_characters import open_list
from allowed_characters import close_list


def log_sentence(sentence):
    with open('new_analysed_text.txt', 'a+', encoding='utf-8') as new_file:
        new_file.write(sentence + "\n")


def reverse_balance(sentence):
    stack = []
    newest_sentence = ""
    print("checking reverse balance for {}".format(sentence))
    for i in sentence[::-1]:
        if i not in open_list + close_list:
            newest_sentence = i + newest_sentence
        if i in close_list:
            stack.append(i)
            newest_sentence = i + newest_sentence
        elif i in open_list:
            pos = open_list.index(i)
            if ((len(stack) > 0) and
                    (close_list[pos] == stack[len(stack) - 1])):
                stack.pop()
                newest_sentence = i + newest_sentence
            else:
                print("Excluding ", i)

    if len(newest_sentence) < 6:
        return

    if len(stack) == 0 and newest_sentence not in new_seen_set:
        new_seen_set.add(newest_sentence)
        log_sentence(newest_sentence)


def check_balance(sentence):
    stack = []
    new_sentence = ""
    print("check balance for {}".format(sentence))
    for i in sentence:
        if i not in open_list + close_list:
            new_sentence += i
        if i in open_list:
            stack.append(i)
            new_sentence += i
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
                new_sentence += i
            else:
                print("Excluding ", i)

    if len(new_sentence) < 6:
        return

    if len(stack) == 0 and new_sentence not in new_seen_set:
        new_seen_set.add(new_sentence)
        log_sentence(new_sentence)
    else:
        reverse_balance(new_sentence)


def concurrent_run(sens):
    # bracket_list = ["（）席類製造）（", "（）席類製造", "（）席類{}製造", "席類製造（", "]席[類(製{造"]
    threads = min(MAX_THREADS, len(sens))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(check_balance, sens)


def main(sens):
    t0 = time.time()
    concurrent_run(sens)
    t1 = time.time()
    print(f"{t1 - t0} seconds to analyse {len(sens)} stories.")


MAX_THREADS = 10

lines = []
with open("aozora_full_text.txt", encoding='utf-8', errors='ignore') as file:
    for line in file:
        if "Title:" in line:
            continue
        lines.append(line.rstrip('\n').replace("―", "").replace("_", "").replace("＼", "")
                     .replace("／", "").replace("＊", "").replace("★", "").replace("●", "")
                     .replace("○", "").replace("▲", "").replace("△", "").replace("┐", "")
                     .replace("┌", "").replace("└", "").replace("┘", "").replace("├", "")
                     .replace("　", ""))

body_text = ''.join(lines).replace("。", "。\n").replace("？", "？\n").replace("?", "?\n") \
    .replace("！", "！\n").replace("!", "!\n").replace("‼", "‼\n").replace("⁉", "⁉\n") \
    .replace("………", "…").replace("……", "…").replace("…", "…\n")
sentences = body_text.split('\n')

seen_set = set()
for filtered_line in sentences:
    print("filtering duplicates")
    if len(filtered_line) >= 6 and filtered_line not in seen_set:
        seen_set.add(filtered_line)

new_seen_set = set()
main(seen_set)
