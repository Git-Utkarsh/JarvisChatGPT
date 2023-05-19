# JarvisChatGPT 
<p float="left">
  <img src="https://uploads-ssl.webflow.com/5b105a0c66f2f636c7884a17/64063dbcad97bd421b437096_chatgpt.jpg" alt="Image 1" width="200" height='120'style="margin-right: 20px;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/935px-Python-logo-notext.svg.png" alt="Image 2" width="100">
</p>

# Speech Recognition and Text-to-Speech with ChatGPT

This Python project utilizes OpenAI's ChatGPT, speech recognition, and pyttsx3 modules to create a speech-enabled AI chatbot. Users can speak into a microphone, and the AI model will recognize the speech, generate a response, and convert it into spoken text using text-to-speech functionality.

## Prerequisites

To run this project, you need to have the following installed:

- Python 3.x
- OpenAI Python library
- SpeechRecognition library
- pyttsx3 library

You will also need an OpenAI API key to access the ChatGPT model. Make sure to set up your API key as an environment variable or configure it within the code.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/Git-Utkarsh/JarvisChatGPT.git
   pip install -r requirements.txt
## Configuration

You can modify the behavior of the chatbot by adjusting the following parameters in the `main.py` script:

## Limitations

- The accuracy of speech recognition depends on various factors, such as microphone quality and ambient noise. For optimal results, it is recommended to use a good quality microphone and minimize background noise during interactions with the chatbot.
- The project relies on the OpenAI ChatGPT model, which has its own limitations. The responses generated by the model might occasionally be incorrect, nonsensical, or sensitive to input phrasing. The model's behavior is based on the data it was trained on and may not always align perfectly with human expectations.
- The usage of the OpenAI API is subject to rate limits and potential costs associated with API calls. Make sure to review the OpenAI documentation to understand the limitations and pricing details of using the ChatGPT API.
- It is essential to handle user input and system output securely, especially if dealing with sensitive or personal information. Take appropriate measures to protect user privacy and ensure data security when deploying or extending this project.

Please consider these limitations while using the speech-enabled chatbot and adjust your expectations accordingly.

