FILENAME = "wimbledon.csv"
INDEX_COUNTRY = 1
INDEX_CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champions_to_count, countries = process_records(records)
    print_results(champions_to_count, countries)


def get_records(FILENAME):
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(',')
            records.append(parts)
    return records


def process_records(records):
    champions_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[1])
        try:
            champions_to_count[record[2]] += 1
        except KeyError:
            champions_to_count[record[2]] = 1
    return champions_to_count, countries


def print_results(champions_to_count, countries):
    print("Wimbledon Champions:")
    for name, count in champions_to_count.items():
        print(f"{name} {count}")
    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(', '.join(country for country in countries))


main()
