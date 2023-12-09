def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        data = [line.strip().split(',') for line in in_file]
        del data[0]
    champions = count_champions(data)
    countries = print_countries(data)
    print_results(champions, countries)
    return data


def count_champions(data):
    champions = {}
    for row in data:
        champion = row[2]
        if champion in champions:
            champions[champion] += 1
        else:
            champions[champion] = 1
    return champions


def print_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(list(countries))


def print_results(champions, countries):
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")
    print("These", len(countries), "countries have won Wimbledon:")
    print(', '.join(countries))


main()
