import urllib
from bs4 import BeautifulSoup

def parse_url(url, fname):
    alphanumeric = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            '.', ',', ';', ':', '-', "'"]

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    text = text.encode('ascii', 'ignore')

    old_text = text.split(' ')
    text = []
    for word in old_text:
        characters = []
        for i in word:
            if i in alphanumeric:
                characters.append(i)
            else:
                characters.append(' ')
        new_word = ''.join(characters)
        text.append(new_word)

    f= open(fname, 'w')
    constant = 15
    for i, word in enumerate(text):
        if i % constant == 0:
            f.write(word)
            f.write('\n')
        else:
            f.write(word)
            f.write(' ')
    f.close()
