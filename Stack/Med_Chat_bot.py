
#!/usr/bin/env python
# coding: utf-8

# # Activity: Creating a chatbot with Python
# You are developing an AI-powered medical diagnosis assistant chatbot within a Jupyter Notebook environment. This chatbot will use spaCy to analyze user symptoms and provide preliminary diagnoses and recommendations, simulating a realistic medical interaction.
# 
# In this exercise, you will create the chatbot logic, define a knowledge base, and ensure the chatbot can effectively extract symptoms and provide appropriate advice, all within a Jupyter Notebook for automated assessment.
# 
# ## Tips for completing this lab
# As you navigate this lab, keep the following tips in mind:
# - `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook.
# - You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook.

# ## Step 1: Set up environment
# To start a chatbot, you will need to ensure spaCy is installed and install a language model (in this case, the core spaCy English language model). You have decided to set this up as a Jupyter Notebook for the moment. 
# 
# First, verify installation of spaCy by running the cell labeled **Step 1a**:

# ### Step 1a
# This exercise uses a specific version of spaCy (3.7.2) intentionally to avoid conflicts.

# In[2]:


pip install spacy==3.7.2


# Once you run this cell, you may be prompted to reload the notebook. This will only need to be done one time on the machine.

# Once the installation is complete/verified, install the English language model. Inside of the notebook, the process to install spaCy's languages is different from doing it from the command line. 
# 
# Run the cell labeled **Step 1b**.

# ### Step 1b: Install and load core English spaCy model

# In[3]:


import spacy

spacy.cli.download('en_core_web_sm')


# Once you run this cell, you may be prompted to reload the notebook. This will only need to be done one time on the machine.

# ## Step 2: Load the medical knowledge base
# You'll be provided with a medical knowledge base in a JSON file named `medical_data.json`. This file contains information about various symptoms, potential medical conditions, and general recommendations. Your chatbot will use this knowledge base to understand user input and provide helpful responses.
# 
# Instructions:
#  - **Examine the structure:** Carefully review the structure of the medical_data.json file. Notice how the data is organized into dictionaries and lists. Pay attention to the keys and values used to represent symptoms, conditions, and recommendations. 
#  - **Understand the content:** Familiarize yourself with the symptoms, conditions, and recommendations included in the knowledge base. This will help you understand the scope of your chatbot's potential diagnoses and advice.
#  - **Consider limitations:** Think about the limitations of this knowledge base. What types of medical conditions or scenarios might not be covered? How can your chatbot handle situations where the user's symptoms don't have a clear match in the data?
#  
# Run the cell labeled **Step 2.1** to create the knowledge base.

# ### Step 2.1: Populate JSON knowledge base

# In[ ]:


import json

def generate_json_file(data, filename):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)  # indent=4 for pretty printing (optional)
        print(f"JSON data saved to {filename}")
    except Exception as e:
        print(f"Error saving JSON data: {e}")

medical_data = {
  "symptoms": {
    "headache": ["common cold", "flu", "migraine", "tension headache", "sinusitis"],
    "fever": ["common cold", "flu", "infection", "strep throat"],
    "cough": ["common cold", "flu", "bronchitis", "pneumonia", "allergies"],
    "sneezing": ["common cold", "flu", "allergies"],
    "fatigue": ["common cold", "flu", "stress", "lack of sleep", "anemia"],
    "nausea": ["flu", "food poisoning", "stomach virus", "migraine", "pregnancy"],
    "vomiting": ["flu", "food poisoning", "stomach virus", "motion sickness"],
    "diarrhea": ["stomach virus", "food poisoning", "irritable bowel syndrome", "lactose intolerance"],
    "rash": ["allergies", "chickenpox", "measles", "eczema", "poison ivy"],
    "dizziness": ["dehydration", "inner ear infection", "low blood sugar", "vertigo"],
    "weakness": ["muscle strain", "flu", "electrolyte imbalance", "multiple sclerosis"],
    "insomnia": ["stress", "anxiety", "depression", "sleep apnea"],
    "itchy": ["allergies", "eczema", "dry skin", "psoriasis"],
    "bloating": ["irritable bowel syndrome", "lactose intolerance", "food intolerance", "celiac disease", "constipation"],
    "chills": ["flu", "common cold", "pneumonia", "infection", "sepsis"],
    "constipation": ["irritable bowel syndrome", "dehydration", "lack of fiber", "medication side effects", "hypothyroidism"],
    "sweating": ["anxiety", "menopause", "hyperthyroidism", "low blood sugar", "infection"],
    "thirst": ["dehydration", "diabetes", "kidney problems", "medication side effects"],
    "tremors": ["anxiety", "Parkinson's disease", "multiple sclerosis", "alcohol withdrawal", "low blood sugar"],
    "weight gain": ["thyroid disorders", "diabetes", "depression", "eating disorders", "certain medications"],
    "weight loss": ["thyroid disorders", "diabetes", "depression", "eating disorders", "cancer", "certain medications"],
    "burning": ["urinary tract infection", "heartburn", "acid reflux", "sunburn", "nerve pain"],
    "cramps": ["menstrual cramps", "muscle cramps", "dehydration", "irritable bowel syndrome"],
    "discharge": ["vaginal infection", "STI", "ear infection"],
    "pain": ["arthritis", "injury", "infection", "nerve damage", "cancer"],
    "swelling": ["injury", "inflammation", "infection", "lymphedema", "heart failure"],
    "tingling": ["nerve damage", "vitamin deficiency", "multiple sclerosis", "diabetes"]
  },
  "recommendations": {
    "common cold": "Rest, stay hydrated, and consider over-the-counter medications for symptom relief.", 
    "flu": "Rest, stay hydrated, and consider over-the-counter medications for symptom relief.", 
    "migraine": "Rest in a quiet, dark room. Apply a cold compress to your forehead. Consider over-the-counter pain relievers.", 
    "tension headache": "Apply a warm compress to your neck and shoulders. Practice stress management techniques. Consider over-the-counter pain relievers.", 
    "sinusitis": "Use a humidifier or saline nasal spray. Consider over-the-counter pain relievers and decongestants.", 
    "infection": "Consult a doctor for diagnosis and appropriate treatment, which may include antibiotics.",
    "strep throat": "Consult a doctor for diagnosis and appropriate treatment, which usually involves antibiotics.",
    "tonsillitis": "Gargle with salt water and drink warm liquids. Consider over-the-counter pain relievers.", 
    "allergies": "Identify and avoid allergens. Consider over-the-counter antihistamines.", 
    "bronchitis": "Rest, stay hydrated, and use a humidifier. Consider over-the-counter pain relievers and cough suppressants.", 
    "pneumonia": "Consult a doctor for diagnosis and appropriate treatment, which may include antibiotics.",
    "muscle strain": "Rest the affected muscle, apply ice, and consider over-the-counter pain relievers.", 
    "stress": "Practice stress management techniques such as exercise, meditation, or deep breathing.",
    "lack of sleep": "Aim for 7-9 hours of quality sleep per night. Establish a regular sleep schedule.",
    "food poisoning": "Stay hydrated and rest. Consider over-the-counter medications for symptom relief.", 
    "stomach virus": "Stay hydrated and rest. Consider over-the-counter medications for symptom relief.", 
    "irritable bowel syndrome": "Consult a doctor for diagnosis and management strategies. Dietary changes and stress management may help.",
    "chickenpox": "Consult a doctor for diagnosis and treatment. Isolate yourself to prevent spreading the virus.",
    "measles": "Consult a doctor for diagnosis and treatment. Isolate yourself to prevent spreading the virus.",
    "eczema": "Keep your skin moisturized. Avoid triggers that worsen your eczema.", 
    "asthma": "Use your prescribed inhaler as directed. Avoid triggers that worsen your asthma.",
    "heart attack": "Seek immediate medical attention. Call emergency services or go to the nearest hospital.",
    "angina": "Consult a doctor for diagnosis and treatment. Follow your doctor's recommendations for managing your condition.",
    "anxiety": "Practice relaxation techniques such as deep breathing and meditation. Seek professional help if anxiety is persistent or severe.",
    "appendicitis": "Seek immediate medical attention. Call emergency services or go to the nearest hospital.",
    "stomach ulcer": "Consult a doctor for diagnosis and treatment. Avoid foods and medications that irritate your stomach.",
    "menstrual cramps": "Apply heat to your lower abdomen. Consider over-the-counter pain relievers.",
    "irritable bowel syndrome": "Consult a doctor for diagnosis and management strategies. Dietary changes and stress management may help.",
    "lactose intolerance": "Avoid consuming lactose-containing products. Consider lactase supplements.",
    "food intolerance": "Identify and avoid trigger foods. Consult a doctor or registered dietitian for guidance.",
    "celiac disease": "Maintain a strict gluten-free diet. Consult a doctor or registered dietitian for management.",
    "sepsis": "Seek immediate medical attention. Sepsis is a life-threatening condition.",
    "hypothyroidism": "Consult a doctor for diagnosis and treatment, which typically involves hormone replacement therapy.",
    "menopause": "Discuss hormone replacement therapy or other management options with your doctor. Manage symptoms with lifestyle changes.",
    "hyperthyroidism": "Consult a doctor for diagnosis and treatment, which may include medication, radioactive iodine therapy, or surgery.",
    "Parkinson's disease": "Consult a neurologist for diagnosis and a comprehensive treatment plan.",
    "multiple sclerosis": "Consult a neurologist for diagnosis and a comprehensive treatment plan.",
    "alcohol withdrawal": "Seek medical supervision for safe detoxification. Support groups and therapy can aid in recovery.",
    "urinary tract infection": "Consult a doctor for diagnosis and treatment, which usually involves antibiotics.",
    "heartburn": "Avoid trigger foods, eat smaller meals, and don't lie down immediately after eating. Consider over-the-counter antacids.",
    "acid reflux": "Similar to heartburn, avoid trigger foods, eat smaller meals, and don't lie down immediately after eating. Consult a doctor if symptoms persist.",
    "sunburn": "Apply cool compresses and aloe vera. Avoid further sun exposure. Use sunscreen regularly.",
    "nerve pain": "Consult a doctor for diagnosis and treatment, which may include medication, physical therapy, or other therapies.",
    "arthritis": "Consult a doctor for diagnosis and a treatment plan, which may include medication, physical therapy, and lifestyle changes.",
    "lymphedema": "Consult a doctor or lymphedema specialist for management, which may include compression therapy and specialized exercises.",
    "heart failure": "Consult a cardiologist for diagnosis and a comprehensive treatment plan, which may include medication, lifestyle changes, and other therapies.",
    "vaginal infection": "Consult a doctor for diagnosis and treatment, which may depend on the type of infection.",
    "STI": "Consult a doctor for diagnosis and treatment."
  }
}
generate_json_file(medical_data, "medical_data.json")


# ### Step 2.2: Load the data from the JSON knowledge base
# This file contains information about various symptoms, potential medical conditions, and general recommendations. Your chatbot will use this knowledge base to understand user input and provide helpful responses. The data could be loaded directly into a dictionary; however, this setup ensures modularity and will better translate if you want to further develop this project outside of the Jupyter environment in the future. 
# 
# Run the cell labeled **Step 2.2a** to load the knowledge base. The data will be displayed as a JSON dictionary.

# ## Step 2.2a

# In[ ]:


import spacy
nlp = spacy.load("en_core_web_sm")

def print_json_from_file(filename):
    """Prints the contents of a JSON file to the console with indentation."""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)  # Load the JSON data
            print(json.dumps(data, indent=4)) # Print with indentation
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{filename}'.")
    except Exception as e:  # Catch any other potential errors
        print(f"An error occurred: {e}")
print_json_from_file("medical_data.json")


# ## Step 3: Develop the chatbot logic
# Now it's time to build the core logic of your medical diagnosis assistant chatbot. You'll use `spaCy` to process user input, extract symptoms, and provide relevant responses based on the medical knowledge base.

# ### Step 3.1: Extract the symptoms
# The `extract_symptoms` function will process the user's input using `spaCy` to identify individual symptoms. It will iterate through each word (or token) in the input and check if its lowercase form matches any known symptom in the medical knowledge base. To avoid duplicates, it ensures that each symptom is added to the `extracted_symptoms` list only once. Finally, the function returns a list of unique symptoms found in the user's input.
# 
# The code to process the `user_input` and initialize and then return the extracted symptoms has been provided. In the middle of the function locate the section labeled `### YOUR CODE HERE ###`.
# 
# Hints:
#  - Locate the area in **Step 3.1a** labeled `### YOUR CODE HERE ###`
#  - You will need four lines of code to complete this function.
#  - Sample code for testing purposes is provided at the bottom of the cell. This can be uncommented for testing purposes.
#  - You can use a `for` loop to iterate through the tokens in the doc object.
#  - The `.text` attribute of a token gives you the text of the token.
#  - The `.lower()` method can be used to convert a string to lowercase.
#  - The `in` operator can be used to check if a value exists in a dictionary or a list.

# ### Step 3.1a

# In[ ]:


def extract_symptoms(user_input):
    """Extracts symptoms from user input using spaCy."""
    doc = nlp(user_input)
    extracted_symptoms = []
    ### YOUR CODE HERE ###

    return extracted_symptoms

user_input = "I have a headache and a fever."
user_symptoms = extract_symptoms(user_input)
print(user_symptoms)


# In[ ]:


# Checking your Results


# ## Step 3.2: Analyze the symptoms
# The `analyze_symptoms` function takes a list of extracted symptoms and determines the possible medical conditions associated with those symptoms.  It uses the `medical_data` dictionary to look up the conditions linked to each symptom. For every symptom provided, it iterates through the corresponding list of potential conditions and tallies how often each condition appears. The function ultimately returns a dictionary containing each possible condition along with a count of how many input symptoms are associated with it. This count helps determine the likelihood of each condition. 
# Hints:
#  - Locate the area in **Step 3.2a** labeled `### YOUR CODE HERE ###`
#  - You will need five lines of code to complete this function.
#  - Sample code for testing purposes is provided in the *# Checking your Results* cell below.
#  - This step involves a `for` loop, followed by an if statement, followed by another if statement, plus one other line of code.
#  - You can use a `for` loop to iterate through the `extracted_symptoms` list and the list of conditions for each symptom.
#  - The `in` operator can be used to check if a key exists in a dictionary.
#  - Example: If the `extracted_symptoms` list is `["headache", "fever"]`, the code should analyze these symptoms based on the `medical_data` and return a dictionary like this:
#  
# ```
# {
# 	"common cold": 2,		# headache and fever match common cold
# 	"flu": 2,				# headache and fever match flu
# 	"migraine": 1,			# headache matches migraine
# 	"tension headache": 1,  # headache matches tension headache
# 	"sinusitis": 1,			# Only headache matches sinusitis
# 	"infection": 1,			# Only fever matches infection
# 	"strep throat": 1		# Only fever matches strep throat
# }
# ```
#  - The goal is to count how many times each possible condition appears across the given symptoms.
#  - The `possible_conditions` dictionary should contain the conditions as keys and their counts as values.
# 

# ## Step 3.2a

# In[ ]:


def analyze_symptoms(extracted_symptoms):
    """Analyzes symptoms and returns possible conditions with counts."""
    possible_conditions = {}  # Use a dictionary to count occurrences
    for symptom in extracted_symptoms:
        ### YOUR CODE HERE ###

    return possible_conditions


# In[ ]:


# Checking your Results
extracted_symptoms = ["headache", "fever"]  
possible_conditions = analyze_symptoms(extracted_symptoms)
print(extracted_symptoms)
print(possible_conditions)


# ## Step 3.3: Generate responses
# 
# The `generate_response` function takes the extracted symptoms and possible conditions as input and constructs a response for the user. If no symptoms are recognized, it informs the user. Otherwise, it acknowledges the symptoms and, if applicable, presents the possible conditions sorted by their likelihood, along with corresponding recommendations from the medical knowledge base. If no matching conditions are found, it informs the user accordingly. Finally, it adds a disclaimer advising the user to consult a doctor for definitive medical advice.
# 
# Hints:
#  - Locate the area in **Step 3.3a** labeled `### YOUR CODE HERE ###`
#  - You will need five lines of code to complete this function.
#  - Sample code for testing purposes is provided in the *# Checking your Results* cell below.
#  - The `items()` method of a dictionary can be used to iterate through its key-value pairs.
#  - The in operator can be used to check if a key exists in a dictionary.
#  - Example: If the `possible_conditions` dictionary is:
# ```
# 	{
# 		"common cold": 2,
# 		"flu": 2,
# 		"migraine": 1
# 	}
# ```
#  - The code should generate a response like this:
# 
# ```
# Based on your symptoms, the most likely possibilities are:
# 	- common cold (2 matching symptom(s))
# 		* Rest, stay hydrated, and consider over-the-counter medications for symptom relief.
# 	- flu (2 matching symptom(s))
# 		* Rest, stay hydrated, and consider over-the-counter medications for symptom relief.
# 	- migraine (1 matching symptom(s))
# 		* Rest in a quiet, dark room. Apply a cold compress to your forehead. Consider over-the-counter pain relievers.
# ```
# 

# ### Step 3.3a

# In[ ]:


def generate_response(extracted_symptoms, possible_conditions):
    """Generates a response based on extracted symptoms and possible conditions."""
    response = ""
    if extracted_symptoms:
        response += "I understand you have " + ", ".join(extracted_symptoms) + "."  
        response += "\nBased on your symptoms, the most likely possibilities are:"

        if possible_conditions:
            sorted_conditions = sorted(possible_conditions.items(), key=lambda item: item[1], reverse=True)  # Sort by count
            ### YOUR CODE HERE ###

        else:
            response += "\nI'm sorry, I don't recognize those symptoms.\n" 
    else:
        response = "I'm sorry, I didn't recognize any symptoms in your description." 

    response += "Remember, I am just a chatbot and cannot provide definitive medical advice. Please consult a doctor for proper diagnosis and treatment."
    return response


# In[ ]:


# Checking your Results
extracted_symptoms = ["headache", "fever"]
possible_conditions = {
    "common cold": 2,
    "flu": 2,
    "migraine": 1
}
print(generate_response(extracted_symptoms, possible_conditions))
# Test for header


# In[ ]:


# Test for common cold


# In[ ]:


# Test for flu


# In[ ]:


# Test for migraine


# In[ ]:


# Test for disclaimer


# ## Step 3.4: Test the program
# 
# Run the cell for Step **3.4a**. No changes are necessary to this cell. Ensure you are able to get a diagnosis.

# ### Step 3.4a

# In[ ]:


possible_conditions = []
extracted_symptoms = []

# Get user's symptoms
user_input = input("Please enter your primary concern: ")

# Extract symptoms
extracted_symptoms = extract_symptoms(user_input)

# Analyze symptoms
possible_conditions = analyze_symptoms(extracted_symptoms)

# Generate initial response
response = generate_response(extracted_symptoms, possible_conditions)
print("Chatbot:", response)


# ## Step 4: Enhance the chatbot with multi-turn conversation
# 
# Step 4 implements a loop that repeatedly asks the user for additional symptoms. Inside the loop, the chatbot takes the user's input and checks if they want to add more symptoms. If they do, it extracts any valid symptoms from their input and adds them to the list of extracted symptoms. It then re-analyzes the updated list of symptoms and generates a new response with the updated diagnosis and recommendations. If the user doesn't enter any new symptoms or enters an invalid symptom, the chatbot prompts them to try again. After the user finishes entering symptoms, the chatbot prints the final response with the complete diagnosis and recommendations.

# ## Step 4.1: Complete multi-turn conversation
# 
# Complete the code to better handle a multi-turn conversation.
# 
# Hints:
#  - Locate the area in **Step 4.1a** labeled `### YOUR CODE HERE ###`
#  - You will need two lines of code to complete this function.
#  - Update the diagnosis: After adding the `new_symptoms` to the `extracted_symptoms` list, you need to re-analyze the symptoms to update the possible conditions. Use the `analyze_symptoms()` function for this.
#  - Generate a new response: After re-analyzing the symptoms, generate an updated response using the `generate_response()` function. Make sure to use the updated `extracted_symptoms` and `possible_conditions` as arguments.
#  
# Run the cell to test the program.
# 

# ### Step 4.1a

# In[ ]:


while True:
    additional_symptoms = input("Please enter an additional symptom, or 'no' if you have no more: ")
    if additional_symptoms.lower() in ("no", "nope", "none"):
        break  # Exit the loop if the user has no more symptoms

    new_symptoms = extract_symptoms(additional_symptoms)
    if new_symptoms:  # Only add and analyze if new symptoms are found
        extracted_symptoms.extend(new_symptoms)
        ### YOUR CODE HERE ###

        print("Chatbot:", response)  # Print the updated response
    else:
        print("Chatbot: I didn't recognize that symptom. Please try again.")

print("Chatbot:", response)


# In[ ]:


# Checking your Results


# ## End of project and areas for improvement
# 
# Congratulations on completing your medical diagnosis assistant chatbot! You've successfully built a chatbot that can:
#  - Extract symptoms from user input using `spaCy`.
#  - Analyze symptoms to identify potential medical conditions.
#  - Provide basic recommendations and advice.
#  - Engage in a multi-turn conversation.
# 
# However, as with any real-world project, there's always room for improvement. Here are some areas you could explore to enhance your chatbot:
#  - **More sophisticated diagnostic logic:** Consider implementing more advanced techniques like weighted symptoms, symptom combinations, or decision trees to improve the accuracy of the diagnosis. For example, you could assign higher weights to more severe symptoms or create rules to identify specific combinations of symptoms that indicate particular conditions.
#  - **Contextual awareness:** Enhance the chatbot's ability to understand and utilize the context of the conversation to provide more relevant responses.
#  - **User-specific information:** Incorporate user details like age, gender, and medical history to personalize the diagnosis and recommendations. For example, you could avoid suggesting "menstrual cramps" as a possible condition for a male user.
#  - **Error handling:** Improve the chatbot's robustness by adding more comprehensive error handling for various scenarios, such as invalid input or missing data.
#  - **External knowledge bases:** Explore integrating more extensive medical knowledge bases or ontologies to provide a wider range of diagnoses and more detailed information.
#  - **Ethical considerations:** Continue to refine the chatbot's responses to ensure they are responsible, ethical, and prioritize the user's well-being. Always emphasize the importance of consulting a medical professional for accurate diagnosis and treatment.
#  
# By exploring these areas for improvement, you can further develop your chatbot into a more sophisticated, reliable, and helpful tool for preliminary medical diagnosis.
# 
