# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyCliPHziM3-gnohyS-4lOASdYSYtHjj3GE")

# Initialize the model
model = genai.GenerativeModel("gemini-pro")

# Generate a response
response = model.generate_content("Explain AI in simple terms")

# Print the response
print(response.text)


