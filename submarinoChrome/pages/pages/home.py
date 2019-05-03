class home:
    def __init__(self, driver):
        self.URL = 'https://www.submarino.com.br/'
        self.driver = driver
        self.PRODUCT_NAME = 'Motorola X4' #letras maíusculas para definir constante

    #Acessar a página principal
    def go_home(self):
        self.driver.get(self.URL)

    #Pesquisar produto
    def search_product(self):
        element = self.driver.find_element_by_id('h_search-input')
        element.click()
        element.send_keys(self.PRODUCT_NAME)
        element.submit()

    def go_login(self):
        self.element = self.driver.find_element_by_xpath('/html/body/header/div[2]/div[2]/div[1]/div[3]/span[2]/a/span[1]')
        self.element.click()
        self.button = self.driver.find_element_by_xpath('//*[@id="h_usr-signin"]')
        self.button.click()

    def more_info(self):
        self.button = self.driver.find_element_by_xpath("/html/body/footer/div[3]/div/div[2]/a/span")
        self.button.click()
    
    def hotels_link(self):
        self.link = self.driver.find_element_by_link_text("Hotéis")
        self.link.click()
        
    
