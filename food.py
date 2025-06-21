import requests
api_key ="7cd1e713210445f9a62121cd90126ab0"
food = input("Enter a food item: ")
params = {
    "title": food,
    "apiKey": api_key
}
url = "https://api.spoonacular.com/recipes/guessNutrition"
response = requests.get(url, params=params)
print("Status Code:", response.status_code)
if response.status_code == 200:
    data = response.json()
    print("\n Nutrition Information for:", food.capitalize())
    print("Calories:", data["calories"]["value"], data["calories"]["unit"])
    print("Fat:", data["fat"]["value"], data["fat"]["unit"])
    print("Protein:", data["protein"]["value"], data["protein"]["unit"])
    print("Carbs:", data["carbs"]["value"], data["carbs"]["unit"])
else:
    print(" Error fetching data.")
    print(response.text)
