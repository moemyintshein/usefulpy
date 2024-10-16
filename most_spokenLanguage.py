import json

def most_spoken_language(fname, limit):
    with open(fname, 'r') as file:
        data = json.load(file)

    languages = {}
    for country in data:
        if 'languages' in country:
            for language in country['languages']:
                if language in languages:
                    languages[language] += 1
                else:
                    languages[language] = 1

    sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:limit]

print(most_spoken_language('countries_data.json', 10))