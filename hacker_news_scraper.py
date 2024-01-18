import requests
from bs4 import BeautifulSoup
import pprint


user_input = int(input('How Much pages you want to print : '))
i = 1
for x in range(user_input):
    i += x
    print(f'Pages {x}')
    res = requests.get(f'https://news.ycombinator.com/news?p={i}')
    soup = BeautifulSoup(res.text, 'html.parser')

    links = soup.select('.titleline')
    votes = soup.select('.score')

    def sorting_by_votes(hnlists):
        return sorted(hnlists, key=lambda k:k['Votes'], reverse=True)

    def create_custom_hn(links, votes):
        hn = []
        for link, vote in zip(links, votes):
            link_element = link.select_one('a')

            if link_element:
                title = link_element.getText()
                href = link_element.get('href', None)
                points = int(vote.getText().replace(' points', ''))  # Assuming each link has a corresponding vote count
                if points > 50:
                    hn.append({'Title': title, 'Link': href, 'Votes': points})
        return sorting_by_votes(hn)
    
    pprint.pprint(create_custom_hn(links, votes))
