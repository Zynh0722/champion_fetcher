import requests
from bs4 import BeautifulSoup



def main():
    soup = BeautifulSoup(requests.get('https://leagueoflegends.fandom.com/wiki/List_of_champions').text, 'html.parser')

    soup = soup.findAll('tbody')[1].findAll('tr')

    soup = [node for node in [*map(lambda node: node.findAll('td'), soup)] if node != []]

    for node in soup:
        node[0] = node[0].findAll('a', href=True, title=True)[1].contents
        node[0] = [node[0][0], node[0][2]]

        node[1] = node[1].findAll('a', href=True, title=True)
        node[1] = [i.text for i in node[1] if len(i.findAll()) == 0]
        node[1].sort()
        node[1] = '-'.join(node[1])

        for i in range(-1, -4, -1):
            node[i] = node[i].contents[0].text.strip()
        
        node[-4] = node[-4].text.strip()

    soup = [[node[0][0], node[0][1], *node[1:]] for node in soup]

    for champ in soup:
        for j in champ:
            print(j + ',', end='')
        print()

if __name__ == '__main__':
    main()