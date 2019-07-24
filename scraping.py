from bs4 import BeautifulSoup
import requests
import json

def scrape():
    l = []
    for page in range(0, 3):
        page = page + 1
        base_url = 'https://poslovi.infostud.com/oglasi-za-posao-python/beograd' + str(page)
        # print(base_url)

        # Request URL and Beautiful Parser
        r = requests.get(base_url)
        soup = BeautifulSoup(r.text, "html.parser")

        all_jobs = soup.find_all('div', class_="uk-panel uk-panel-box uk-margin-small-bottom istaknuti-oglas-lista-lyt")
        # print(len(all_jobs))

        for item in all_jobs:
            d = { }

            # skills
            jobs_tag = item.find("div", {"class": "uk-width-large-3-4"})
            jobs_tag = jobs_tag.text.replace('\n', " ").strip()
            d['jobs_tag'] = jobs_tag

            # company
            company = item.find("p", {"class": "uk-h3 uk-margin-remove"})
            company = company.text.replace('\n', " ").strip()
            d['company'] = company

            l.append(d)
            
            with open('job.json', 'w+') as outfile:
                json.dump(l, outfile)

    return l



if __name__ == "__main__":
    print(scrape())
