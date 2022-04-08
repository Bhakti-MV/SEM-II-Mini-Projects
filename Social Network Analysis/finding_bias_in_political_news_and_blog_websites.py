import googlesearch
from textblob import TextBlob
import texttable as tt
from time import sleep
from mechanize import Browser

def search(site, search):
    site = site
    search = search
    search_results = googlesearch.search("inurl:" + site + " intext:" + search, stop=2)
    search_results_list = []
    subjectivity_list = []
    polarity_list = []
    num = []
    number = 1

    for result in search_results:
        url = result
        br = Browser()
        br.open(url)
        search_results = br.title()
        search_results_list.append(search_results)

        analysis = TextBlob(search_results)
        subjectivity = analysis.sentiment.subjectivity
        subjectivity_list.append(subjectivity)
        polarity = analysis.sentiment.polarity
        polarity_list.append(polarity)
        number = number + 1
        num.append(number)
        sleep(10)

    tab = tt.Texttable()
    headings = ['Number','Results','Subjectivity', 'Polarity']
    tab.header(headings)

    for row in zip(num, search_results_list, subjectivity_list, polarity_list):
        tab.add_row(row)

    avg_subjectivity = (sum(subjectivity_list) / len(subjectivity_list))
    avg_polarity = (sum(polarity_list) / len(polarity_list))

    table = tab.draw()
    print(site)
    print(search)
    print(table)
    print(site + " average subjectivity: " + str(avg_subjectivity))
    print(site + " average polarity: " + str(avg_polarity))

search("indianexpress", "narendra modi")
sleep(10)
search("news18", "narendra modi")