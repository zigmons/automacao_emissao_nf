from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

def pd_set_df_view_options(max_rows=1000, max_columns=350, display_width=320):
    pd.set_option('display.max_rows', max_rows)
    pd.set_option('display.max_columns', max_columns)
    pd.set_option('display.width', display_width)
pd_set_df_view_options(max_rows=1000, max_columns=350, display_width=320)

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\rafae\teste",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})


driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

driver.get(r'C:\Users\rafae\OneDrive\PhytonAulas\AulasHashtag - windows\Automacao Web(Web-Scraping)\exercicio_automatizaremissaonf\login.html')

login = driver.find_element(By.XPATH, '/html/body/div/form/input[1]')
senha = driver.find_element(By.XPATH, '/html/body/div/form/input[2]')

login.send_keys('Rafael')
senha.send_keys('123456')

driver.find_element(By.XPATH,'/html/body/div/form/button').click()

