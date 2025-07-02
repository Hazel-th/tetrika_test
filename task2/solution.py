import requests
import csv
from LxmlSoup import LxmlSoup
from typing import Dict

BASE_URL = "https://ru.wikipedia.org"
START_URL = f"{BASE_URL}/wiki/Категория:Животные_по_алфавиту"


def get_soup(url: str) -> LxmlSoup:
    response = requests.get(url)
    response.raise_for_status()
    return LxmlSoup(response.text)


def count_animals_by_letter(page: str) -> Dict[str, int]:
    results = {}
    letter = ""

    while page:
        soup = get_soup(page)
        letter_groups = soup.find("div", id="mw-pages").find_all(
            "div", class_="mw-category-group"
        )

        for group in letter_groups:
            letter = group.find("h3").text().strip()
            if letter == "A":  # начинается английский
                return results
            
            items = group.find_all("li")
            results[letter] = results.get(letter, 0) + len(items)

        next_page = soup.find("div", id="mw-pages").find_all("a")[-1]
        page = BASE_URL + next_page.get("href")

    return results


def csv_writer(animal_count_by_letter: Dict[str, int]):
    with open("task2/beasts.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for row in sorted(animal_count_by_letter.items()):
            writer.writerow(row)


def main():
    page = START_URL
    animal_count_by_letter = count_animals_by_letter(page)

    csv_writer(animal_count_by_letter)

    print("Готово")


if __name__ == "__main__":
    main()
