import random
import word_silly


def full_sentence(nouns, verbs, templates):
    index = 0
    nounCh = len("{{noun}}")
    verbCh = len("{{verb}}")
    output = []
    template = random.choice(templates)
    while index < len(template):
        if template[index:index + nounCh] == "{{noun}}":
            noun = random.choice(nouns)
            index += nounCh
            output.append(noun)
        elif template[index:index + nounCh] == "{{verb}}":
            verb = random.choice(verbs)
            index += verbCh
            output.append(verb)
        else:
            output.append(template[index])
            index += 1
    return "".join(output)


if __name__ == '__main__':
    print(full_sentence(word_silly.nouns, word_silly.verbs,word_silly.templates))
