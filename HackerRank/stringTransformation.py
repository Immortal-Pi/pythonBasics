def transformSentence(sentence):
    sentence_list = sentence.split(" ")
    updated_sentence=""
    for i in sentence_list:
        if len(i) > 1:
            word = f'{i[0]}'
            for letter in range(1, len(i)):

                if i[letter]>i[letter-1]:
                    word+=i[letter].upper()
                elif i[letter]<i[letter-1]:
                     word+=i[letter].lower()
                else:
                    word+=i[letter]
            updated_sentence+=f'{word}'

        else:
            updated_sentence+=i
        updated_sentence += ' '
    return updated_sentence
string='a Blue MOON'
updated=transformSentence(string)
print(updated)