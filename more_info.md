
## pytest флаги
-s выводить print
-v подробное имя теста - как он называется в формате файл::класс::метод(тест)
-m использование mark конкретного теста
-m "smoke or extended" использование and/or - выбор по параметрам тестов
--browser_name= firefox или chrome

#### @pytest.mark.xfail(reason="fixing this bug right now")
такого рода сообщения можно выводить с ключом -rx    

#### pytest-rerunfailures
плагин для повторного запуска упавшего теста 
--tb=line - сокращение лога с результатами теста
--reruns 1 - количество перезапусков упавшего теста

#### @pytest.mark.parametrize('language', ["ru", "en-gb"]) 
- фикстура с массивом передаваемых параметров в ссылку, например язык
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

#### то же самое, только средствами python с использованием выбора браузера: 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox

@pytest.fixture(scope="function")
def browser(request):

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    options_firefox = OptionsFirefox()
    options_firefox.set_preference("intl.accept_languages", user_language)
...
    if browser_name == "chrome":
...
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
...
        browser = webdriver.Firefox(options=options_firefox)
...

## conftest.py 
файл в который выгружаются общие для каждого файла фикстуры. Используются в зависимости от выставленного scope применительно к  классу, модулю, функции, package, сессии.



## Allure
pytest -v --alluredir=tmp/my_allure_results - запись результатов в отчет Allure


установить локально allure можно через scoop, ссылка на скачивание: http://scoop.sh
также для работы Allure потребуется установить java (с занесением в Path)
выполнить команду: scoop install allure


allure serve <directory-with-results>  
allure serve tmp/my_allure_results - создание временного отчета
allure generate <directory-with-results> -o <directory-with-report> - создание отчета в указанную папку
