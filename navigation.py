import os
import random
import shutil
import time

from selenium.webdriver.remote.webelement import WebElement

import fold_generator
from coursetype import course_type
from genbrowser import Entry

waiting_time_min = 1.3
waiting_time_max = 1.5

def level_step(browser: Entry):  # Step 1 : Niveau
    browser.logger.info("lancement de l'étape 1")

    levels = [
              #"ce1", "ce2", "cm1", "cm2",
              #"sixieme", "cinquieme", "quatrieme", "troisieme", "seconde",
              "premiere-s", "terminale-s"]

    for level in levels:
        browser.logger.info("Charging level :"+ level)

        browser.browser.get("https://www.kartable.fr/" + level)
        time.sleep(random.uniform(waiting_time_min, waiting_time_max))
        course_step(browser, level)
        time.sleep(random.uniform(waiting_time_min, waiting_time_max))


def course_step(browser: Entry, level):  # Step 2 : Matière
    browser.logger.info('Matière')
    courses = browser.browser.find_elements_by_xpath("//article")[3:]
    browser.logger.info(courses)

    #choppe les noms des matières
    courses_name_elements = browser.browser.find_elements_by_xpath("//a[@class='course__link']")
    courses_names = []
    cur: WebElement
    for course in courses_name_elements:
        courses_names.append(course.text)
    browser.logger.info('courses_names')

    cur: int
    for course in range(len(courses)):
        url_of_course_home_page = browser.browser.current_url
        try:
            #vas sur la matière
            #course_page = browser.browser.find_elements_by_xpath("//article")[3:][course]`
            course_button = browser.browser.find_element_by_link_text(courses_names[course])
            course_button.click()
            time.sleep(random.uniform(waiting_time_min, waiting_time_max))
            lesson_step(browser, level, courses_names[course])
            time.sleep(random.uniform(waiting_time_min, waiting_time_max))
            browser.browser.back()
        except Exception as e:
            time.sleep(1)
            browser.logger.error('Erreur pour le chargement de la matiere '
                                 + str(course) + ' en '
                                 + level)
            time.sleep(2)
            browser.browser.get(url_of_course_home_page)
            time.sleep(1)

def lesson_step(browser: Entry, level, course): # Step 3 chapitre
    need_back = 0
    xpath = "//section//section//section//section//section//section//article//article"
    course_type(browser)
    lessons = browser.browser.find_elements_by_xpath(xpath)
    for lesson in range(len(lessons)):
        url_of_lesson_home_page = browser.browser.current_url
        try:
            #vas sur le cours
            lesson_page = browser.browser.find_elements_by_xpath(xpath)[lesson]
            lesson_page.click()
            time.sleep(random.uniform(waiting_time_min, waiting_time_max))
            get_file_step(browser, level, course)
            browser.browser.back()
        except Exception as e:
            time.sleep(1)
            browser.logger.error('Erreur pour le telechargement de la leçon numéro'
                                 + str(lesson) + ' en '
                                 + course + ' en '
                                 + level)
            time.sleep(2)
            browser.browser.get(url_of_lesson_home_page)
            time.sleep(1)


    if need_back == 1:
        browser.browser.back()


def get_file_step(browser: Entry, level, course): #step 4 Get the pdf

    #cette partie vas télécharger le cours et le mettre dans le dossier cours (avec des sous dossiers)

    #Fail sometimes
    #cour: WebElement = browser.browser.find_element_by_xpath("//figure//img")

    #Fix tentative
    time.sleep(0.2)
    cour: WebElement = browser.browser.find_element_by_link_text('Cours')

    cour.click()
    #on arrive enfin sur la page du cours
    #trouve le bouton télécharger en pdf
    time.sleep(random.uniform(waiting_time_min, waiting_time_max))
    boutton: WebElement = browser.browser.find_element_by_xpath("//button//span")


    url = browser.browser.current_url
    file = os.getcwd() + "/file" + (url[len("kartable.fr/ressources/"):])
    browser.logger.info("téléchargement dans " + file)
    download_path = 'file'
    params = {'behavior': 'allow', 'downloadPath': download_path}
    browser.browser.execute_cdp_cmd('Page.setDownloadBehavior', params)

    boutton.click()
    # Time to let the downlaoding
    time.sleep(2)

    # génère le bon emplacement du fichier
    emplacement = "cours/" + level + "/" + course + "/"
    fold_generator._folder_generator(emplacement)
    time.sleep(0.3)
    # Copie le fichier au bon endroit et le supprime de file
    browser.logger.info(os.listdir("file/"))
    fichier = os.listdir("file/")[0]
    browser.logger.info(fichier)
    browser.logger.info("copy : ", "file/" + fichier, "  to  ", emplacement + fichier)
    shutil.copy("file/" + fichier, emplacement + fichier)
    browser.logger.info('copy done')
    browser.logger.info("remove : ", "file/" + fichier)
    os.remove("file/" + fichier)
    browser.logger.info('removed from file')


    time.sleep(random.uniform(waiting_time_min, waiting_time_max))
    browser.browser.back()
