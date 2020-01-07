from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from access.inject import AccessSite


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument("--enable-popup-blocking")
options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path = ChromeDriverManager().install(), options = options)

SITES = [
    "https://www.emakina.group/",
    "https://www.emakina.group/en-US/WhoWeAre/Agencies",
    "https://www.emakina.group/en-US/WhatWeDo/Services",
    "https://www.emakina.group/en-US/WhereWeAre/Offices",
    "https://www.emakina.group/en-US/News/Press",
    "https://www.emakina.group/en-US/Contact/Media-relations"
]


def test_emakina_group_home_page():
    AS = AccessSite()
    driver.get(SITES[0])
    site_name = "Home Page"
    AS.inject_axe(driver, f"{site_name}: {SITES[0]}", f"emakina_group_{site_name}.txt")


def test_emakina_group_agencies_site():
    AS = AccessSite()
    driver.get(SITES[1])
    site_name = "Agencies"
    AS.inject_axe(driver, f"{site_name}: {SITES[1]}", f"emakina_group_{site_name}.txt")


def test_emakina_group_services_site():
    AS = AccessSite()
    driver.get(SITES[2])
    site_name = "Services"
    AS.inject_axe(driver, f"{site_name}: {SITES[2]}", f"emakina_group_{site_name}.txt")


def test_emakina_group_offices_site():
    AS = AccessSite()
    driver.get(SITES[3])
    site_name = "Offices"
    AS.inject_axe(driver, f"{site_name}: {SITES[3]}", f"emakina_group_{site_name}.txt")


def test_emakina_group_press_site():
    AS = AccessSite()
    driver.get(SITES[4])
    site_name = "Press"
    AS.inject_axe(driver, f"{site_name}: {SITES[4]}", f"emakina_group_{site_name}.txt")


def test_emakina_group_media_relations_site():
    AS = AccessSite()
    driver.get(SITES[5])
    site_name = "Media_relations"
    AS.inject_axe(driver, f"{site_name}: {SITES[5]}", f"emakina_group_{site_name}.txt")
    driver.quit()
