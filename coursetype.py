#Le type de cours en fonction de la page d'une matière
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

from genbrowser import Entry


def course_type(browser: Entry):
    # There are three different lesson types
    need_back = 0
    # Deuxième type de page (spécialité ou spécifique) (il faut aller sur spécialité)
    xpathspe = "/html/body/kartable-app/ng-component/div/div/kartable-menu/main/section/section/div/a[2]"
    try:
        if browser.browser.find_element_by_xpath(xpathspe) != None:
            browser.browser.find_element_by_xpath(xpathspe).click()
            need_back = 1
        pass
    except NoSuchElementException:
        pass

    # Troisième type de page (différentes parties déroulables) (onbtenir le nombre de parties et si != de 1 les dérouler
    xpathparties = "/html/body/kartable-app/ng-component/div/div/kartable-menu/main/section/section/section[2]/categories-hierarchy/section"
    parties = browser.browser.find_elements_by_xpath(xpathparties)
    if len(parties) > 1:
        cur: WebElement
        for cur in parties:
            cur.click()

    return need_back
