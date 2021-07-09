#!/usr/bin/env python
# coding: utf-8

#import libraries
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#import CSV file to pandas (make sure excell is in csv format)
df = pd.read_csv ("/Users/heatherruddy/Downloads/HCI Python/Recipe Project/recipe_Project_Ruddy/recipe2.csv")


#print 5 rows of data
df.head(5)
print(df)

#print columns 
col_list = df.columns
print(col_list)

#print a row
df.loc[3]



'''
#is the recipe available
def is_recipe_available(user_input,df):
    
    recipe_list = df["Recipe title"]
    
    #if else loop for if a recipe is available
    if user_input in recipe_list:
        print("Recipe is available")
        
    else:
        print("Recpie is not available")
'''
'''
#print entire recipe 
def print_recipe(user_input, df):
    r = df.loc[df["Recipe title"] == user_input]
    r.reset_index(drop=True, inplace=True)
    print(r) # Debug
    if r.empty:
	    print("Not found")
    else:
	    print(r.loc[0].tolist())
'''


#prints directions line by line
def print_directions(directions):
    
    split = 0
    #loop through all the characters to find where we have '1.' and '2.' and '3.'
    for i in range(len(directions) - 1): 
        
        if (directions[i].isnumeric()) and (directions[i+1] == '.'):
            
            print(directions[split:i], '\n')
            
            split = i  



def find_similar_recipe(user_input):
    
    #store similar recipes to what user inputs
    recipes = []    
    
    #split the user input
    inp = user_input.lower().split()
    
    #make the recipe name lowercase
    recipe_list = df['Recipe title'].tolist()
    
    recipe_list_adjusted = [''.join(s.split()).lower() for s in recipe_list]
    
    #find if the any words in the user input matches the recipe list
    for i in inp:
        
        for r, recipe in enumerate(recipe_list_adjusted):
            
            if i in recipe:
                
                recipes.append(recipe_list[r])
    #one result per title will print out           
    return np.unique(recipes)






'''#user leaves recipe review
def leave_review(user_review):
    
    #if else loop for acceptable review length
    if len(user_review) < 200:
        print("Thank you for your review.")
    else: 
        print("Error. Your review exceeds the character limit.")
'''
'''
#user adds a note to a recipe
def leave_note(user_note):
    
    #if else loop to determine if not is correct length
    if len(user_note) < 200:
        print("Your note has been saved.")
    else:
        print("Error. Your note was too long.")
'''

'''
#import an image for a recipe
def plot_image(image):
    
    img = mpimg.imread(image)
    imgplot = plt.imshow(img)
    plt.show()'''

'''def return_best_match(search_term, word_list):
    Given a search term, which is the closest match from a list of strings?
    if not reasonably good match is found, None is returned
    Based on a difference metric, here i'm using the Jaro-Winkler metric from this package:
    https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-distance
    
    similarity_list = []
    for word in word_list:
        similarity = Levenshtein.jaro_winkler(search_term, word) # https://rawgit.com/ztane/python-Levenshtein/master/docs/Levenshtein.html#Levenshtein-jaro_winkler
        similarity_list.append([similarity, word])  # 0: similarity, 1: word

    sorted_similarity_list = sorted(similarity_list, reverse=True) # sort decending, largest similarity on top
    best_match = sorted_similarity_list[0] # list with largest similarity

    if best_match[0] < 0.5: # no good enough metric was found
        return None
    else:
        return best_match[1] # word with best metric (> 0.5)
'''
 







