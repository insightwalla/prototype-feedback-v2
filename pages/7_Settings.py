# PARAMETERS
service_keywords = [
      'service', 'waiter', 'waitress', 'waiters', 'waitresses', 'waitstaff',
      'host', 'hostess', 'hostesses', 'hosts', 'server', 'servers', 'staff',
      'price', 'bill', 'rush', 'rushing', 'rushes', 'rushed', 'rush','birthday',
      'pricing', 'priced', 'pricey', 'expensive', 'expensiveness', 'expensiveness',
   ]

key_words_related_to_ambience = ['atmosphere', 'ambience', 'chairs', 'tables', 'seating',
                                       'decor', 'interior', 'design', 'lighting', 'music', 'sound',
                                       'noise', 'noisy', 'quiet', 'loud', 'crowded', 'crowd', 'crowds',
                                       'crowding', 'clean', 'peaceful', 'toilets','parking','toilet',
                                       
]
   
food_keywords = [
      'cocktails', 'chilli', 'chutney', 'chutneys',
      'icecream', 'ice-cream', 'ice cream', 'icecreams', 'ice-creams', 'ice creams',
      'food', 'taste', 'tastes', 'flavor', 'flavors', 'dish', 'dishes', 'menu',
      'meal', 'meals', 'portions', 'portion', 'portioned', 'portioning', 'portioned',
      'quality', 'quantity', 'quantities', 'quantitied', 'quantitied', 'quantitied', 'Biryani']

keywords = service_keywords + key_words_related_to_ambience + food_keywords

menu_items_lookup = [
         'Akuri',
         'B & E Naan',
         'Bacon Naan',
         'Basmati Kheer',
         'Basmati Rice',
         'Bhel',
         'Big Bombay',
         'Black Daal',
         'Bowl of Greens',
         'BS Keema Pau',
         'BS Pau Bhaji',
         'Butter Corn OTC',
         'Butter Paanch',
         'Calamari',
         'Ch. Chawal (V)',
         'Ch. Puri(V)',
         'Chck Tikka Roll',
         'Cheese Naan',
         'Chicken Biryani',
         'Chicken Ruby',
         'Chicken Tikka',
         'Chilli Br Salad',
         'Chilli Chicken',
         'Choc Pud w/chil',
         'Choc Pud w/Cinn',
         'Chocolate Chai',
         'Chole Puri',
         'Dbl Bacon Naan',
         'Egg Naan',
         'Garlic Naan',
         'Gulab Jamun',
         'GunpowderPotato',
         'House Chaat',
         'Jackfruit Birya',
         'Kachumber',
         'Keema Per Eedu',
         'Kejriwal',
         'Khichia WChundo',
         'Kulfi Malai',
         'Kulfi Mango',
         'Kulfi Pistach.',
         'Lamb Chops',
         'Lamb Raan',
         'Lamb Raan Bun',
         'Lamb Samosas',
         'Mango& Fenn',
         'Masala Prawns',
         'Mattar Paneer',
         'Murgh Malai',
         'Mutton Chp Korm',
         'Mutton Pepper F',
         'Nihari',
         'Nihari Biryani',
         'Okra Fries',
         'Paneer Roll',
         'Paneer Tikka',
         'Parsi Omelette',
         'Pineapple Tikka',
         'Plain Naan',
         'Prawn Koliwada',
         'Raita',
         'Roomali Roti',
         'S & E Naan',
         'Saus Naan',
         'Sheekh Kabab',
         'Side Beans',
         'Tandoor  Roti',
         'Uttapam Stack',
         'Vada Pau',
         'Veg. Samosas',
         'Vegan Bombay',
         'Vegan Saus Naan',
         'Wrestler Naan',
         'Xmas Feast',
         'CCT',
      ]

drink_items_lookup = [
         'Beer',
         'Colaba Colada',
         'Mojito',
         'Mango Lassi',
         'Breakfast Lassi',
         'Coffee',
         'Americano',
         'Espresso',
         'Latte',
         '33cl Kingfisher',
         '65cl Kingfisher',
         'Aflatoon',
         'Amb. Viog Btl',
         'Bob Sauv Blanc',
         'Bolly Bellini',
         'Quinde Gls',
         'Quinde Malbec',
         'Sali Boti Full',
         'Sali Boti Half',
         'Sonia Negroni',
         'Sparkling Water',
         'Spumante Btl',
         'Spumante Gls',
         'Still Water',
         'Viceroy OF',
         'Watermelon Shbt',
         'Syrah Punctum',
         'Kohinoor Fizz',
         'Meenakshi Moj',
         'Nimbu Soda',
         'Oat Chai',
         'P. Grig Btl',
         'P. Grigio Gls',
         'Passionfr Shbt',
         'Peacock Cider',
         'Grenache Btl',
         'Grenache Gls',
         'Chai',
         'handra Bose',
         'Coloba Colada',
         'Cyrus Irani',
         'Dhoble',
         'Diet Coke 33cl',
         'Dish Esp Mtini',
         'Dishoom IPA',
         'East IndiaGim',
         'Folle Grillo Bt',
         'FolleGrillo Gls',
         'Fresh Orange J']

options_for_classification = [
      'Welcome Not First Class',
      'Welcome Not Big Hearted',
      'Team Missed Special Occasions',
      'Team Missed Allergen / Dietary Requirement',
      'Team Service Not Big Hearted',
      'Team Service Not First Class',
      'Team Failed Service Recovery',
      'Bill Overcharged / Incorrect',
      'Overall End 2 End Poor Experience',
      'Overall Underwhelming / Average Experience',
      'Atmosphere',
      'Cleanliness / Safety Concerns',
      'Drink Delivery Slow',
      'Drinks Missing / Incorrect',
      'Drinks Average Feedback',
      'Drinks Poor Feedback',
      'Food Delivery Slow',
      'Food Missing / Incorrect',
      'Food Average Feedback',
      'Food Poor Feedback',
      'Dishoom General Offering',
      'Dishoom Design',
      'Dishoom Booking Policy / Queue',
      'Dishoom Price',
      'Dishoom Service Charge',
      'Too loud',
      'Other (No Clear Category)',
      '',
      'nan',]

import streamlit as st
import pandas as pd

from database import DBMenu, DBDrinks, DBProductKeywords, DBServiceKeywords, DBAmbienceKeywords
if __name__ == '__main__':
    db = DBMenu()

    c1,c2,c3 = st.columns(3)
    button_delete = c2.button('Delete all')
    if button_delete:
        db.delete_all()

    button_populate = c1.button('Default Menu')
    if button_populate:
        db.delete_all()
        db.populate_db(menu_items_lookup)

    menu = st.experimental_data_editor(db.view(as_df=True), num_rows='dynamic', use_container_width=True)

    button_save = c3.button('Save')
    if button_save:
        list_of_menu_items = menu['name'].tolist()
        # keep non empty values and not none
        list_of_menu_items = [item for item in list_of_menu_items if item is not None]
        list_of_menu_items = [item for item in list_of_menu_items if item != '']
        db.save_all(list_of_menu_items)


    # drinks
    db = DBDrinks()

    c1,c2,c3 = st.columns(3)
    button_delete = c2.button('Delete all (drinks)')
    if button_delete:
        db.delete_all()

    button_populate = c1.button('Default Drinks')
    if button_populate:
        db.delete_all()
        db.populate_db(drink_items_lookup)


    menu_drinks = st.experimental_data_editor(db.view(as_df=True), num_rows='dynamic', use_container_width=True)

    button_save = c3.button('Save (drinks)')
    if button_save:
        list_of_drink_items = menu_drinks['name'].tolist()
        # keep non empty values and not none
        list_of_drink_items = [item for item in list_of_drink_items if item is not None]
        list_of_drink_items = [item for item in list_of_drink_items if item != '']
        db.save_all(list_of_drink_items)

    # product keywords
    db = DBProductKeywords()

    c1,c2,c3 = st.columns(3)
    button_delete = c2.button('Delete all (product keywords)')
    if button_delete:
        db.delete_all()

    button_populate = c1.button('Default Product Keywords')
    if button_populate:
        db.delete_all()
        db.populate_db(keywords)


    menu_product_keywords = st.experimental_data_editor(db.view(as_df=True), num_rows='dynamic', use_container_width=True)

    button_save = c3.button('Save (product keywords)')

    if button_save:
        list_of_product_keywords = menu_product_keywords['name'].tolist()
        # keep non empty values and not none
        list_of_product_keywords = [item for item in list_of_product_keywords if item is not None]
        list_of_product_keywords = [item for item in list_of_product_keywords if item != '']
        db.save_all(list_of_product_keywords)

    # service keywords
    db = DBServiceKeywords()

    c1,c2,c3 = st.columns(3)
    button_delete = c2.button('Delete all (service keywords)')
    if button_delete:
        db.delete_all()

    button_populate = c1.button('Default Service Keywords')
    if button_populate:
        db.delete_all()
        db.populate_db(service_keywords)


    menu_service_keywords = st.experimental_data_editor(db.view(as_df=True), num_rows='dynamic', use_container_width=True)

    button_save = c3.button('Save (service keywords)')
    if button_save:
        list_of_service_keywords = menu_service_keywords['name'].tolist()
        # keep non empty values and not none
        list_of_service_keywords = [item for item in list_of_service_keywords if item is not None]
        list_of_service_keywords = [item for item in list_of_service_keywords if item != '']
        db.save_all(list_of_service_keywords)

    # ambience keywords
    db = DBAmbienceKeywords()

    c1,c2,c3 = st.columns(3)
    button_delete = c2.button('Delete all (ambience keywords)')
    if button_delete:
        db.delete_all()

    button_populate = c1.button('Default Ambience Keywords')
    if button_populate:
        db.delete_all()
        db.populate_db(key_words_related_to_ambience)


    menu_ambience_keywords = st.experimental_data_editor(db.view(as_df=True), num_rows='dynamic', use_container_width=True)

    button_save = c3.button('Save (ambience keywords)')

    if button_save:
        list_of_ambience_keywords = menu_ambience_keywords['name'].tolist()
        # keep non empty values and not none
        list_of_ambience_keywords = [item for item in list_of_ambience_keywords if item is not None]
        list_of_ambience_keywords = [item for item in list_of_ambience_keywords if item != '']
        db.save_all(list_of_ambience_keywords)

