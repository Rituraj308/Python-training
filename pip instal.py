#to install python packeges like pyjokes  we have to 1st go in 1) settings,then 2)project, then 3)python interpreter and
#then we have to click on '+' symbole and type the packege name and intall it.
import pyjokes
joke = pyjokes.get_joke("en","neutral")
print(joke)