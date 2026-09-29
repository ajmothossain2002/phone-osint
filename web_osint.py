from urllib.parse import quote


def generate_queries(phone):
    # Remove spaces/dashes for one version
    clean = phone.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    # Keep a formatted version as well
    formatted = phone.strip()

    queries = [
        f'"{clean}"',
        f'"{formatted}"',
        f'"{clean}" business',
        f'"{clean}" company',
        f'"{clean}" contact',
        f'"{clean}" address',
        f'"{clean}" WhatsApp',
        f'"{clean}" Facebook',
        f'"{clean}" Instagram',
        f'"{clean}" LinkedIn',
    ]

    return queries


phone = input("Enter phone number: ").strip()

print("\n" + "=" * 60)
print("PUBLIC WEB OSINT SEARCH QUERIES")
print("=" * 60)

for query in generate_queries(phone):
    url = "https://www.google.com/search?q=" + quote(query)

    print("\nQuery :", query)
    print("Search:", url)

print("\n" + "=" * 60)