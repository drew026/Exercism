def is_pangram(sentence):
    sent = sentence.lower()
    sent = ''.join([i for i in sent if i.isalpha()])
    sent = ''.join(set(sent))
    if len(sent) == 26:
        return True
    return False
        