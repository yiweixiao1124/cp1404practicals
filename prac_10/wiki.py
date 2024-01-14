import wikipedia

while True:
    title = input("Enter a page title or search phrase: ")
    if title == '':
        break
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary}")
        print(f"URL: {page.url}")
        print()
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)


