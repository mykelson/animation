import os
import pathlib
import unittest
import time

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome('C:\\Users\\mykeltuz\\Downloads\\Programs\\chromedriver') # change this path to run this test on your device.

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("animate0.html"))
        self.assertEqual(driver.title, "My Webpage")

    def test_animate0(self):
        driver.get(file_uri("animate0.html"))
        h1 = driver.find_element_by_tag_name("h1")
        time.sleep(5)
        self.assertEqual(h1.value_of_css_property("font-size"), '100px')

    def test_animate1(self):
        driver.get(file_uri("animate1.html"))
        h1 = driver.find_element_by_tag_name("h1")
        time.sleep(5)
        self.assertEqual(h1.value_of_css_property("position"), 'relative')
    
    def test_animate3(self):
        driver.get(file_uri("animate3.html"))
        h1 = driver.find_element_by_tag_name("h1")
        button = driver.find_element_by_tag_name("button")
        for i in range(4):
            button.click()
            time.sleep(5)
        time.sleep(5)
        
        self.assertEqual(h1.value_of_css_property("animation-play-state"), 'paused')

if __name__ == "__main__":
    unittest.main()