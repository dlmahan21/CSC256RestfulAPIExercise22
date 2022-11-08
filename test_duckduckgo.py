import pytest
import requests


url_ddg = "https://api.duckduckgo.com"


def test_ddg_search():
    the_presidents = ["Lincoln", "Trump", "Biden", "Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson",
                      "Tyler", "Taylor", "Garfield", "Wilson", "Reagan", "Obama", "Buren", "Harrison", "Polk",
                      "Fillmore", "Pierce", "Buchanan", "Johnson", "Grant", "Hayes", "Arthur", "Cleveland", "McKinley",
                      "Roosevelt", "Taft", "Harding", "Coolidge", "Hoover", "Truman", "Eisenhower", "Kennedy", "Nixon",
                      "Ford", "Carter", "Bush", "Clinton"]
    response = requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
    response_data = response.json()
    topic_list = response_data['RelatedTopics']
    president_names = []
    for topic in topic_list:
        president_names.append(topic['Text'])
    for last_name in the_presidents:
        # checks if each last name is in any of the search results
        president_found = any(last_name in president for president in president_names)
        assert president_found
