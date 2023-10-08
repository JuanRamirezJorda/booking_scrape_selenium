from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency=2)
    bot.select_place_to_go('New York')

    bot.select_dates(check_in_date='2023-10-15',
                     check_out_date='2023-10-20')
    
    #bot.select_adults(10)
    
    
    bot.click_search()
    
 