from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [
    	{
    	 "restaurant_name": "KFC",
    	 "food_type": "fast food"
    	},
    	{
   	     "restaurant_name": "Maki",
    	 "food_type": "Japanes food"
    	},
    	{
    	 "restaurant_name": "Melenzane",
    	 "food_type": "italian food"
    	}

    	]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": {
    	"restaurant_name": "katsuya",
    	"food_type": "Asian cousin"
    	}

    }
    return render(request, 'detail.html', context)
