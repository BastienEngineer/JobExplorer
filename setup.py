from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from urllib.parse import quote
import threading

def scraper(name, url, balise, balise_name, balise1, balise_name1, balise2, balise_name2, results):
    # Initialize Selenium webdriver
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    # Fonction de scraping pour une URL donnée
    driver.get(url)

    # Wait for the page to load (you might need to adjust this delay)
    driver.implicitly_wait(10)
    # Get the page source after it's been modified by JavaScript
    html = driver.page_source
    # Utiliser BeautifulSoup pour analyser le HTML
    soup = BeautifulSoup(html, "html.parser")
    # Find all job titles
    job_titles = soup.find_all(balise, class_=balise_name)
    entreprises = soup.find_all(balise1, class_=balise_name1)
    lieux = soup.find_all(balise2, class_=balise_name2)
    results[name] = [(job_title.text.strip(), entreprise.text.strip(), lieu.text.strip()) for job_title, entreprise, lieu in zip(job_titles, entreprises, lieux)]

    # Close the Selenium webdriver
    driver.quit()

def scrap():
    mot = input("Ton job : ")
    print("Offres d'emplois\n")

    results = {}
    
    urls = [...]

    nb_sites = len(urls) - 1

    threads = [threading.Thread(target=scraper, args=(name, url, balise, balise_name, balise1, balise_name1, balise2, balise_name2, results)) for name, url, balise, balise_name, balise1, balise_name1, balise2, balise_name2 in urls]    

    for thread in threads:
        thread.start()

    # Attendez que tous les threads aient terminé
    for thread in threads:
        thread.join()

    # Affichez les résultats
    print("\nTous les threads ont terminé. Résultats affichés dans l'ordre.")
    for name, result in results.items():
        print(f"\n||||||||||     {name}      |||||||||||\n")
        for job_title, entreprise, lieu in result:
            print(job_title, '|',  entreprise, '|' , lieu)

def main():
    while True:
        print("Menu")
        print("1 Recherche d'emploi ")
        print("2 Quitter ")

        choix = input("Choisir l'option : ")

        if choix == "1":
            scrap()
            print("\n")
        elif choix == "2":
            print("Au revoir !")
            return
        else:
            print("Mauvaise saisie !\n")

main()
