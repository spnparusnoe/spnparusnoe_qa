import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver


    #method get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print("current url: " + get_url)

    #method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good assert")

     # method screenshot
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\spnpa\\Desktop\\pythonProject\\FinalProject\\screen\\' + name_screenshot)

    # method assert url
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good url")