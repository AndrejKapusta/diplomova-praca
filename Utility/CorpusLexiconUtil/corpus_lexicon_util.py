import codecs
from matplotlib import pyplot as plt
from phon_slovak import ipa_slovak


# Pomocna funkcia pripravi pozadovany typ dat pre vykreslenie
def priprav_data(data, typ):
    datax = []
    datay = []

    samohlasky = ['a', 'e', 'i', 'o', 'u', 'ä', 'á', 'é', 'í', 'ó', 'ú']
    spoluhlasky = ['d', 't', 'n', 'l', 'ch', 'h', 'g', 'k', 'ď', 'ť', 'ň', 'ľ', 'c', 'č', 'ž', 'š', 'dz', 'dž', 'j',
                   'm', 'b', 'p', 'v', 'z', 's', 'f', 'r']
    dvojhlasky = ['ia', 'ie', 'iu', 'ô']

    if typ.__eq__("samohlasky"):
        datax = samohlasky
        for s in samohlasky:
            datay.append(data[s])
    elif typ.__eq__("spoluhlasky"):
        datax = spoluhlasky
        for s in spoluhlasky:
            datay.append(data[s])
    elif typ.__eq__("dvojhlasky"):
        datax = dvojhlasky
        for s in dvojhlasky:
            datay.append(data[s])

    return datax, datay


# Funkcia vykresli histogram ktory je definovany ako parameter
def vykresli_histogram(histogram):

    fig, ((ax1), (ax2), (ax3)) = plt.subplots(3, 1, figsize=(7, 7))
    fig.tight_layout(pad=4.0)

    x_values1, y_values1 = priprav_data(histogram, "samohlasky")
    ax1.bar(x_values1, y_values1, color="#858585")
    ax1.set(xlabel='Samohlásky', ylabel='pocet', title='Početnosť samohlások')

    x_values2, y_values2 = priprav_data(histogram, "spoluhlasky")
    ax2.bar(x_values2, y_values2, color="#858585")
    ax2.set(xlabel='Spoluhlásky', ylabel='pocet', title='Početnosť spoluhlások')

    x_values3, y_values3 = priprav_data(histogram, "dvojhlasky")
    ax3.bar(x_values3, y_values3, color="#858585")
    ax3.set(xlabel='Dvojhlásky', ylabel='pocet', title='Početnosť dvojhlások')

    plt.show()
    pass


# Funkcia vytvara histogram zo suboru corpus.txt
def histogram_corpus():

    # Definovanie abecedy a pocetnosti znakov v texte - dictionary
    histogram = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
                 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0,
                 'ch': 0, 'ä': 0, 'ô': 0, 'á': 0, 'é': 0, 'í': 0, 'ó': 0, 'ú': 0, 'ý': 0, 'ĺ': 0, 'č': 0, 'š': 0,
                 'ž': 0, 'ď': 0, 'ť': 0, 'ň': 0, 'ľ': 0, 'ia': 0, 'ie': 0, 'iu': 0, 'dz': 0, 'dž': 0}

    # Otvorenie suboru s textom
    with open("data/corpus.txt", "rb") as file:
        contents = file.read().decode("UTF-8")

    # Zlucenie slov do jedneho stringu a odstranenie medzier
    znaky = ""
    for word in contents.split("\r\n"):
        znaky = znaky + word + " "
    znaky = znaky.replace(" ", "")

    # Naplenenie histogramu
    for i in range(0, len(znaky)):
        if i + 1 < len(znaky) and znaky[i].__eq__('c') and znaky[i + 1].__eq__('h'):
            histogram['ch'] = histogram['ch'] + 1
            i += 1
        elif i + 1 < len(znaky) and znaky[i].__eq__('i') and znaky[i + 1].__eq__('a'):
            histogram['ia'] = histogram['ia'] + 1
            i += 1
        elif i + 1 < len(znaky) and znaky[i].__eq__('i') and znaky[i + 1].__eq__('e'):
            histogram['ie'] = histogram['ie'] + 1
            i += 1
        elif i + 1 < len(znaky) and znaky[i].__eq__('i') and znaky[i + 1].__eq__('u'):
            histogram['iu'] = histogram['iu'] + 1
            i += 1
        elif i + 1 < len(znaky) and znaky[i].__eq__('d') and znaky[i + 1].__eq__('z'):
            histogram['dz'] = histogram['dz'] + 1
            i += 1
        elif i + 1 < len(znaky) and znaky[i].__eq__('d') and znaky[i + 1].__eq__('ž'):
            histogram['dž'] = histogram['dž'] + 1
            i += 1
        else:
            histogram[znaky[i]] = histogram[znaky[i]] + 1

    vykresli_histogram(histogram)

    file.close()
    pass


# Funkcia pre vytvorenie lexikonu
def make_lexicon():

    # Nacitanie korpusu
    with open("data/corpus.txt", "rb") as file:
        corpus = file.read().decode("UTF-8")

    # Otvorenie suboru lexikonu pre zapisovanie
    lexicon = codecs.open("data/lexicon.txt", "w", "utf-8")

    # Prevod slov na fonemy
    for word in corpus.split("\r\n"):
        translated = word.replace(" ", "")
        translated = ipa_slovak(translated)
        print(word + " " + translated)
        lexicon.write(word + " " + translated + "\r\n")

    # Zatvorenie suborov
    lexicon.close()
    file.close()
    pass


# Hlavna funkcia programu
if __name__ == '__main__':

    # Vykreslenie histogramu (samohlasky, spoluhlasky, dvojhlasky)
    histogram_corpus()

    # Vytvorenie lexikonu
    make_lexicon()
