####################### ALL IMPORTS FOR FILE #######################
from urllib import response
from flask import Flask, render_template  
app = Flask(__name__)
import requests 
import re 

####################### START OF CODE #######################

#COUNTER VARIABLE AND BREAK VARIABLE FOR INFO CHECK
doesBreak = False
counter = 0
organizedRecipeList = []
#ADD NEW LIST FOR EACH DESIRED PIECE OF DATA
tempRecipeList = []
tempTitleList = []
tempCaloriesList = []
tempPrepTimeList = []
tempServingsList = []

#GLOBAL VARIABLES TO REPLACE THE INPUT "QUERY", EXCLUDED INGREDIENTS (NOT INCLUDED YET - WIP) IN THE QUERYSTRING ARRAY - USE THESE TO LINK THE TWO SEARCH METHODS - WILL BE SWITCHED TO GET USER INPUTS ONCE CODE IS INTEGRATED INTO WEB INTERFACE
searchInput = "burger"
excludedIngredients = ""
allergies = "peanut"
desiredIngredients = "tomato"
calLimit = 300

#ALL DESIRED INFORMATION THAT THE USER WISHES TO RECEIVE
desiredInformation = ['"title"', '"calories"','"readyInMinutes"','"servings"']

#SIMPLE SEARCH DATA PULL - PULLS COMPLETION TIME AND SERVINGS - WIP
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

querystring = {"query":searchInput,"diet":"vegetarian","excludeIngredients":excludedIngredients,"intolerances":allergies,"number":"10","offset":"0","type":"main course"}

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "618623e3a9msh2bde9f08f506715p10d82ejsn767640c583f9"
    }


#ARRAY SPLITTING
responseSimple = requests.request("GET", url, headers=headers, params=querystring)
responseSimpleText = (responseSimple.text)
parsedArraySimple = (re.split(",|:", responseSimpleText))

#COMPLEX SEARCH DATA PULL - PULLS TITLE AND CALORIES (WIP)
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/searchComplex"

querystring = {"limitLicense":"<REQUIRED>","offset":"0","number":"10","minIron":"0","minCalcium":"0","maxVitaminB2":"1000","maxMagnesium":"1000","minPotassium":"0","maxVitaminB6":"1000","intolerances":allergies,"maxVitaminB5":"1000","minFolicAcid":"0","minVitaminA":"0","maxSodium":"1000","maxSugar":"1000","maxVitaminA":"5000","maxFluoride":"1000","minFluoride":"0","minVitaminB1":"0","minCholine":"0","ranking":"2","minFat":"5","maxVitaminB1":"1000","minVitaminB12":"0","maxSelenium":"1000","minZinc":"0","minFolate":"0","maxManganese":"1000","maxVitaminB12":"1000","maxPotassium":"1000","maxIron":"1000","minSelenium":"0","minVitaminK":"0","maxFiber":"1000","minSodium":"0","maxCopper":"1000","minCalories":"0","maxCholine":"1000","minCholesterol":"0","maxVitaminE":"1000","minProtein":"5","minVitaminB3":"0","minVitaminB6":"0","maxIodine":"1000","excludeIngredients":excludedIngredients,"maxProtein":"100","minMagnesium":"0","minCarbs":"5","cuisine":"american","maxCaffeine":"1000","maxSaturatedFat":"50","maxVitaminK":"1000","minAlcohol":"0","minIodine":"0","query":searchInput,"minSaturatedFat":"0","includeIngredients":desiredIngredients,"minVitaminE":"0","maxCalcium":"1000","minFiber":"0","minVitaminC":"0","maxZinc":"1000","maxCalories":calLimit,"maxAlcohol":"1000","minPhosphorus":"0","minVitaminD":"0","minVitaminB2":"0","minSugar":"0","maxFolate":"1000","type":"main course","maxCholesterol":"1000","maxVitaminB3":"1000","minCaffeine":"0","minVitaminB5":"0","maxFolicAcid":"1000","maxCarbs":"100","maxVitaminD":"1000","equipment":"pan","maxFat":"100","minCopper":"0","maxVitaminC":"1000","maxPhosphorus":"1000","minManganese":"0"}
##limit license required????

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "618623e3a9msh2bde9f08f506715p10d82ejsn767640c583f9"
    }


responseComplex = requests.request("GET", url, headers=headers, params=querystring)
responseComplexText = (responseComplex.text)
parsedArray = (re.split(",|:", responseComplexText))



for x in desiredInformation:

    if (x in parsedArray):
        for y in parsedArray:
            if (x in parsedArray):
                tempDataTag = (parsedArray[parsedArray.index(x)]+ ":")
                tempDataName = (parsedArray[parsedArray.index(x)+ 1])
                #SPECIFIC CHECK FOR THE TITLE TAG - CHECKS IF THE SECOND HALF OF TITLE IS SEPARATED VIA COMMA
                if(x == '"title"'):
                    tempDataSecondHalf = (parsedArray[parsedArray.index(x)+2])
                    if (tempDataSecondHalf[0] != '"'):
                        tempDataName += tempDataSecondHalf
                fullDataName = (tempDataTag + tempDataName)
                parsedArray.pop(parsedArray.index(x))
                tempRecipeList.append(fullDataName)
                #print (tempRecipeList)
                #print(fullDataName)
                
            else:
                break
    elif (x in parsedArraySimple):
        for y in parsedArraySimple:
            if (x in parsedArraySimple):
                tempDataTag = (parsedArraySimple[parsedArraySimple.index(x)]+ ": ")
                tempDataName = (parsedArraySimple[parsedArraySimple.index(x)+1])
                parsedArraySimple.pop(parsedArraySimple.index(x))
                fullDataName = (tempDataTag + tempDataName)
                tempRecipeList.append(fullDataName)
                #print(tempRecipeList)
                #print(fullDataName)
            else:
                break
    #SORT THE OUTPUT ARRAY INTO SEPARATE ARRAYS SO THAT EACH FINAL RECIPE CAN BE ASSEMBLED
    for y in tempRecipeList:
        if (x == '"title"' and '"title"' in y):
            tempTitleList.append(y)
        elif (x == '"calories"' and '"calories"' in y):
            tempCaloriesList.append(y)
        elif (x == '"readyInMinutes"' and '"readyInMinutes"' in y):
            tempPrepTimeList.append(y)
        elif (x == '"servings"' and '"servings"' in y):
            tempServingsList.append(y)

#ASSEMBLE EACH RECIPE INTO THE FINAL ARRAY

while counter < len(tempTitleList):
    organizedRecipeList.append(tempTitleList[counter] + " " + tempCaloriesList[counter] + " " + tempPrepTimeList[0] + " " + tempServingsList[0])
    counter += 1

random_recipe = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"

@app.route('/')
def get_recipes():
    querystring = {"limitLicense":"<REQUIRED>","offset":"0","number":"10","minIron":"0","minCalcium":"0","maxVitaminB2":"1000","maxMagnesium":"1000","minPotassium":"0","maxVitaminB6":"1000","intolerances":allergies,"maxVitaminB5":"1000","minFolicAcid":"0","minVitaminA":"0","maxSodium":"1000","maxSugar":"1000","maxVitaminA":"5000","maxFluoride":"1000","minFluoride":"0","minVitaminB1":"0","minCholine":"0","ranking":"2","minFat":"5","maxVitaminB1":"1000","minVitaminB12":"0","maxSelenium":"1000","minZinc":"0","minFolate":"0","maxManganese":"1000","maxVitaminB12":"1000","maxPotassium":"1000","maxIron":"1000","minSelenium":"0","minVitaminK":"0","maxFiber":"1000","minSodium":"0","maxCopper":"1000","minCalories":"0","maxCholine":"1000","minCholesterol":"0","maxVitaminE":"1000","minProtein":"5","minVitaminB3":"0","minVitaminB6":"0","maxIodine":"1000","excludeIngredients":excludedIngredients,"maxProtein":"100","minMagnesium":"0","minCarbs":"5","cuisine":"american","maxCaffeine":"1000","maxSaturatedFat":"50","maxVitaminK":"1000","minAlcohol":"0","minIodine":"0","query":searchInput,"minSaturatedFat":"0","includeIngredients":desiredIngredients,"minVitaminE":"0","maxCalcium":"1000","minFiber":"0","minVitaminC":"0","maxZinc":"1000","maxCalories":calLimit,"maxAlcohol":"1000","minPhosphorus":"0","minVitaminD":"0","minVitaminB2":"0","minSugar":"0","maxFolate":"1000","type":"main course","maxCholesterol":"1000","maxVitaminB3":"1000","minCaffeine":"0","minVitaminB5":"0","maxFolicAcid":"1000","maxCarbs":"100","maxVitaminD":"1000","equipment":"pan","maxFat":"100","minCopper":"0","maxVitaminC":"1000","maxPhosphorus":"1000","minManganese":"0"}
    #querystring = {"query":searchInput,"diet":"vegetarian","excludeIngredients":excludedIngredients,"intolerances":allergies,"number":"10","offset":"0","type":"main course"}
    #response = organizedRecipeList
    organizedRecipeList = requests.request("GET", url + find, headers=headers, params=querystring).json()
    print("hi")
    return render_template('recipes.html', recipes=organizedRecipeList)



####################### END OF CODE #######################

####################### TEST PRINTS #######################

#print (parsedArray)
#print (len(parsedArray))
#testTitle = (parsedArray[parsedArray.index('"title"')] + ": " + parsedArray[parsedArray.index('"title"') + 1])
#print (parsedArraySimple)
#print (tempRecipeList)
print(organizedRecipeList)
#print (tempTitleList)
#print(tempCaloriesList)
#print(tempPrepTimeList)
#print(tempServingsList)
####################### END OF TESTS #######################