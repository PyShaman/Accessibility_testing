from axe_selenium_python import Axe


class AccessSite:

    def __init__(self):
        pass

    @staticmethod
    def inject_axe(driver, site, file_name):
        """Using selenium driver, axe injects its own js to the specific site and writes WCAG validations to file"""
        axe = Axe(driver)
        axe.inject()
        results = axe.run()
        f = open("results/" + file_name.replace("/", "_"), "w", encoding="utf-8")
        f.write(site + "\n")
        f.write(axe.report(results["violations"]))
        f.close()
