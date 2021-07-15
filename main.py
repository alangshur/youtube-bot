from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys

import time
import numpy as np

proxy_ip_port = ''

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME.copy()
proxy.add_to_capabilities(capabilities)
capabilities['loggingPrefs'] = {'performance': 'ALL'}

chrome_options = Options()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(
    'env/chromedriver-Darwin', 
    desired_capabilities=capabilities
)

def check_ytd_loaded():
    try: driver.find_element_by_id('ytd-player')
    except NoSuchElementException: return False
    return True

def random_human_delay():
    delay_time = float(np.random.uniform(low=0.5, high=2))
    time.sleep(delay_time)


# load webpage
print('Loading... ', end='', flush=True)
driver.get('https://www.youtube.com/watch?v=EZVcsSkaMmY')
while not check_ytd_loaded(): time.sleep(1)
print('Done.', flush=True)

# find video player element
ytd_el = driver.find_element_by_id('ytd-player')
play_button_el = driver.find_element(By.XPATH, "//button[contains(@class, 'ytp-large-play-button')]")

# wait arbitray time before play
random_human_delay()

# choose arbitrage click area
width, height = play_button_el.size['width'], play_button_el.size['height']
x_offset = int(np.random.uniform(width * 0.1, width * 0.9))
y_offset = int(np.random.uniform(height * 0.1, height * 0.9))

random_human_delay()

# start video with cursor click
ActionChains(driver).move_to_element_with_offset(play_button_el, x_offset, y_offset).click().perform()


time.sleep(10000)
driver.close()


# log = driver.get_log('performance')
# print(log)
