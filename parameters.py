
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


# instead of using this We are going to read form the db

from database import DBAmbienceKeywords, DBServiceKeywords, DBProductKeywords, DBDrinks, DBMenu

menu_items_lookup = DBMenu().view(as_df=True)['name'].tolist()
drink_items_lookup = DBDrinks().view(as_df=True)['name'].tolist()
service_keywords = DBServiceKeywords().view(as_df=True)['name'].tolist()
key_words_related_to_ambience = DBAmbienceKeywords().view(as_df=True)['name'].tolist()
food_keywords = DBProductKeywords().view(as_df=True)['name'].tolist()

keywords = service_keywords + key_words_related_to_ambience + food_keywords
