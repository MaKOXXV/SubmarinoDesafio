class shopping_car:
    def __init__(self, driver):
        self.driver = driver
        
    def add_item(self):
        self.URL = 'https://www.submarino.com.br/garantia/134171201?buyboxField=&buyboxToken=smartbuybox-suba-v2-790814fa-656b-43f8-a5bc-2a89710f5653&condition=NEW&offerType&pricingId=5cc6f59a4cedfd0017a68fbd&productId=134171201&productSku=134171219&sellerId=00776574000660'
        self.driver.get(self.URL)

    def reflesh(self):
        self.CURRENT_URL = 'https://sacola.submarino.com.br/simple-basket/?cartId=96e198ba-82a4-4a31-bef7-164f5495c7b7'
        self.driver.get(self.CURRENT_URL)
        
    def remove_item(self):
        self.link = self.driver.find_element_by_xpath('/html/body/div[4]/section/section/div[1]/div[1]/section/ul/li/div[2]/div[2]/a')
        self.link.click()

    def text_h2(self):
        self.element = self.driver.find_element_by_xpath('/html/body/div[4]/section/section/div[1]/section')
        self.inner_element = self.driver.find_element_by_xpath('/html/body/div[4]/section/section/div[1]/section/h2')
        return self.inner_element.text