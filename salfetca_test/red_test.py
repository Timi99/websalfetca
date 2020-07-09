from selenium import webdriver

def testy_test():
    browder = webdriver.Firefox()
    browder.get('http://127.0.0.1:8000/home')

    print(browder.title)

    assert browder.title == 'Salfetca'