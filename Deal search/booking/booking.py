import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from booking.booking_filtration import BookingFiltration
import time


#options = webdriver.ChromeOptions()
#options.add_experimental_option("detach", True)

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=True):
        
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", teardown)
        super(Booking, self).__init__(options=options)
        
        self.maximize_window()
        
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit(self)
    

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        """
        08/10/23 identifier values for currencies when starting from EUR:
        @param: currency

        - 1 GBP
        - 2 USD
        - 3 AUD
        - 4 SAR
        - 5 CAD
        - 6 RUB
        """
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-testid="header-currency-picker-trigger"]'
        )
        currency_element.click()

        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            f"[data-testid='Suggested for you'] li:nth-of-type({currency}) .ac7953442b"
            
        )
        selected_currency_element.click()

    
    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(
            By.CSS_SELECTOR,
            "input#\:re\:"
        )
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(1)
        first_result = self.find_element(
            By.CSS_SELECTOR,
            "li:nth-of-type(1) > div[role='button']"
        )
        first_result.click()
    
    def select_dates(self, check_in_date, check_out_date):
        """
        Left sample to do: If check out date is >1 month
        """
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'[data-date="{check_out_date}"]'
        )
        check_out_element.click()
    
    """
    
    def select_adults(self, count=1):
        selection_element = self.find_element(
            By.CSS_SELECTOR,
            '[data-testid="occupancy-config"]')
        selection_element.click()
        current_adults = self.find_element(
            By.CSS_SELECTOR, 
            ".aaf77d2184 .a7a72174b8:nth-of-type(1) .bfb38641b0 [aria-hidden='true']:nth-child(2)"
        )
        print("Adultos leidos por web: ", current_adults.text)
        
        
        
        while True:
            
            decrease_adults_element = self.find_element(
                By.CSS_SELECTOR,
                'button[aria-label="Decrease number of Adults"]'
            )
            decrease_adults_element.click()
            #If the value of adults reaches 1, then we should get out
            #of the while loop
            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute(
                'value'
            ) # Should give back the adults count

            if int(adults_value) == 1:
                break

        increase_button_element = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )

        for _ in range(count - 1):
            increase_button_element.click()
            
    """
    def click_search(self):
        search_button = self.find_element(
            By.CSS_SELECTOR,
            '.a4c1805887.a83ed08757.c082d89982.c21c56c305.cceeb8986b.d2529514af.f671049264'
        )
        search_button.click()
    
