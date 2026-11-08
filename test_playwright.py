from playwright.sync_api import Page, expect

URL = "https://www.informatyka.agh.edu.pl/pl/"


def test_strona_glowna(page: Page):
    page.goto(URL)
    assert page.title() != ""


def test_o_wydziale(page: Page):
    page.goto(URL)

    page.get_by_text("Wydział", exact=True).hover()
    page.get_by_role("link", name="O Wydziale").click()

    expect(page.get_by_text("HISTORIA", exact=True)).to_be_visible()


def test_kierunki_studiow(page: Page):
    page.goto(URL)

    page.get_by_text("Kandydaci", exact=True).hover()
    page.get_by_role("link", name="Nasze kierunki").first.click()

    expect(page.get_by_role("heading", name="Nasze kierunki")).to_be_visible()


def test_zmiana_adresu(page: Page):
    page.goto(URL)

    page.get_by_text("Wydział", exact=True).hover()
    page.get_by_role("link", name="O Wydziale").click()

    expect(page).to_have_url("https://www.informatyka.agh.edu.pl/pl/wydzial/o-wydziale/")