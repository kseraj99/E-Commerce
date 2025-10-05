## Whenever you have common reusable code across multiple classes then we create utils file.
## To place all common things there.
## utils class treated as a parent class for all other class.

class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

