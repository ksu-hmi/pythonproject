# Recipease

## Intro

This recipe site focuses on meals that are quick, easy, healthy and only have up to 8 ingredients.

Designed to fit around busy lifestyles, the user experience is simple and clean with limited clutter.

## Site flow

Meals can be filtered on the home screen by ingredient, category(ie breakfast) and name

User can save favourites and comment on recipes by signing up to premium

## Technologies

I shall be using Python with the following packages and technologies:

* django for the web framework
* postgresql for the database
* python-decouple, to seperate config info from code
* django-filter, to siplify the user filtering of objects in browser
* stripe to aid in the process of taking payments

## Run on your local machine
* Make sure you have pip and virtualenv

* Clone the repository into your virtual environment:

`$ git clone https://github.com/danieldeiana/recipease.git`

* Go to recipease/settings.py and scroll to the DATABASES variable. and comment/comment out base on if it's a local or Heroku server

* Activate you virtual environment and whilst in the root folder (containing manage.py) run the following:

`$ python manage.py runserver`

* Then visit [localhost](http://127.0.0.1:8000/) in your browser

## Additional info

The css for the project has been kept in one file, within the recipe app

Due to complications using images with Heroku as a hobbyist, I've decided to create a image charfield(string) in the Meal model and link to external images

## References

Vitor Freitas has a wonderfull Django blog which helped a lot:

* [deploy django and postgresql using heroku](https://simpleisbetterthancomplex.com/tutorial/2016/08/09/how-to-deploy-django-applications-on-heroku.html)

* [how to use python decouple to seperation config data](https://simpleisbetterthancomplex.com/2015/11/26/package-of-the-week-python-decouple.html)

* [how to extend django's user model](https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone) (I spotted this article late and with better planning, I could have integrated some of the concepts better)
* Data Analytics with Jupyter and Pandas
  > COMING SOON
  
