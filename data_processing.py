def process_weather_data(weather_data):
    # Assuming `weather_data` contains a 'main' section with 'temp' in Kelvin
    temp_k = weather_data['main']['temp']
    temp_c = temp_k - 273.15  # Convert Kelvin to Celsius
    # Add other processing logic as needed
    return {"temperature_celsius": temp_c}
