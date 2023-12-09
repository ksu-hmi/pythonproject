from io import BytesIO
from PIL import Image, ImageTk
# Removed import pygame
from py_edamam import PyEdamam
import requests
import tkinter as tk
import webbrowser


# Removed BUTTON_CLICK_SOUND as it's no longer needed
WINDOW_TITLE = "SmartChoiceRecipes"
RECIPE_IMAGE_WIDTH = 350
RECIPE_IMAGE_HEIGHT = 300

class recipeApp(object):

    def __init__(self, recipeApp_id, recipeApp_key):
        self.recipeApp_id = recipeApp_id
        self.recipeApp_key = recipeApp_key
        self.window = tk.Tk()

        # Removed pygame initialization

        # Auto resize geometry
        self.window.geometry("")
        self.window.configure(bg="#9ddfd3")
        self.window.title(WINDOW_TITLE)

        # Search for recipe
        self.search_label = tk.Label(self.window, text="Search Recipe", bg="#ea86b6")
        self.search_label.grid(column=0, row=0, padx=5)

        self.search_entry = tk.Entry(master=self.window, width=40)
        self.search_entry.grid(column=1, row=0, padx=5, pady=10)

        self.search_button = tk.Button(self.window, text="Search", highlightbackground="#ea86b6",
                                       command=self.__run_search_query)
        self.search_button.grid(column=2, row=0, padx=5)

        # Additional search options
        self.diet_label = tk.Label(self.window, text="Diet (e.g., vegan):", bg="#ea86b6")
        self.diet_label.grid(column=0, row=1, padx=5, pady=5)

        self.diet_entry = tk.Entry(master=self.window, width=40)
        self.diet_entry.grid(column=1, row=1, padx=5, pady=5)

    def __run_search_query(self):
        query = self.search_entry.get()
        diet = self.diet_entry.get()
        recipe = self.__get_recipe(query, diet)

        if recipe:
            recipe_image = recipe.image
            recipe_url = recipe.url
        else:
            # Recipe not found
            recipe_image = "https://www.mageworx.com/blog/wp-content/uploads/2012/06/Page-Not-Found-13.jpg"
            recipe_url = ""

        self.__show_image(recipe_image)
        self.__get_ingredients(recipe)

        self.recipe_button = tk.Button(self.window, text="Recipe Link", highlightbackground="#ea86b6",
                                       command=lambda: self.__open_link(recipe_url))
        self.recipe_button.grid(column=1, row=7, pady=10)

    def __open_link(self, recipe_url):
        webbrowser.open(recipe_url)

    def __get_recipe(self, query, diet=None):
        edamam_object = PyEdamam(recipesAppid=self.recipeApp_id, recipesAppkey=self.recipe_app_key)
        query_result = edamam_object.search_recipe(q=query, diet=diet)

        # Get first recipe in list
        for recipe in query_result:
            return recipe

    def __show_image(self, image_url):
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        img = img.resize((RECIPE_IMAGE_WIDTH, RECIPE_IMAGE_HEIGHT))
        image = ImageTk.PhotoImage(img)

        holder = tk.Label(self.window, image=image)
        holder.photo = image  # Keeping a reference
        holder.grid(column=1, row=6, pady=10)

    def __get_ingredients(self, recipe):
        ingredients = tk.Text(master=self.window, height=15, width=50, bg="#ffdada")
        ingredients.grid(column=1, row=4, pady=10)
        ingredients.delete("1.0", tk.END)

        if recipe is None:
            ingredients.insert(tk.END, "No Recipe found for search criteria")
            return

        ingredients.insert(tk.END, "\n" + recipe.label + "\n")
        for ingredient in recipe.ingredient_names:
            ingredients.insert(tk.END, "\n- " + ingredient)

    def run_app(self):
        self.window.mainloop()
        return

# Create and run the app
if __name__ == "__main__":
    APP_ID = "476bffed"  # Put your app id for Edamam
    # You need to replace this with your actual API Key
    APP_KEY = "8f487e87c3936d13ad450decb4dcede2	—"  
    recipeApp = recipeApp(APP_ID, APP_KEY)
    recipeApp.run_app()

