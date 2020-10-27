from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=7E788850-6861-41B3-97E0-1AE3959BB906")
        # need to validate any return, invalid zipcode may return null.
        try:
            api = json.loads(api_request.content)
            if api[0]['Category']['Name'] == "Good":
                category_color = "good"
                category_description = "( 0 - 50) Air quality is considered satisfactory, and air polluation poses little or no risk."
            elif api[0]['Category']['Name'] == "Moderate":
                category_color = "moderate"
                category_description = "( 51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health convern for a very small number of people who are unusually sensitive to air polluion."
            elif api[0]['Category']['Name'] == "Unhealthy Senitive Groups":
                category_color = "USG"
                category_description = "( 101 - 150) ..."
            elif api[0]['Category']['Name'] == "Unhealthy":
                category_color = "unhealthy"
                category_description = "( 151 - 200) ..."
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_color = "veryunhealthy"
                category_description = "( 201 - 250) ..."
            elif api[0]['Category']['Name'] == "Hazardous":
                category_color = "hazardous"
                category_description = "( 251 - 300) ..."

        except Exception as e:
            api = "Error"

        return render(request, 'home.html', {
            'api': api,
            'category_color': category_color,
            'category_description': category_description})
    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=7E788850-6861-41B3-97E0-1AE3959BB906")

        try:
            api = json.loads(api_request.content)
            if api[0]['Category']['Name'] == "Good":
                category_color = "good"
                category_description = "( 0 - 50) Air quality is considered satisfactory, and air polluation poses little or no risk."
            elif api[0]['Category']['Name'] == "Moderate":
                category_color = "moderate"
                category_description = "( 51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health convern for a very small number of people who are unusually sensitive to air polluion."
            elif api[0]['Category']['Name'] == "Unhealthy Senitive Groups":
                category_color = "USG"
                category_description = "( 101 - 150) ..."
            elif api[0]['Category']['Name'] == "Unhealthy":
                category_color = "unhealthy"
                category_description = "( 151 - 200) ..."
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                category_color = "veryunhealthy"
                category_description = "( 201 - 250) ..."
            elif api[0]['Category']['Name'] == "Hazardous":
                category_color = "hazardous"
                category_description = "( 251 - 300) ..."

        except Exception as e:
            api = "Error"

        return render(request, 'home.html', {
            'api': api,
            'category_color': category_color,
            'category_description': category_description})


def about(request):
    return render(request, 'about.html', {})
