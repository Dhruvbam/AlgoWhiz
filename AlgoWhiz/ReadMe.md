# Algorithmic Chat Assistant

## Description

This code implements an AI chat assistant using OpenAI's GPT (Generative Pre-trained Transformer) model. The assistant is specifically designed to engage in conversations related to computer science algorithms, offering explanations, code snippets, and educational content to users.

## Features

- **Starting a Conversation:** Users can initiate a new conversation with the assistant by sending a GET request to `/start`. This initializes a new conversation thread and returns a thread ID. If you encounter an error such as "failed to create thread", you may need to rerun the Python code in Replit.

- **Chatting:** Users can interact with the assistant by sending POST requests to `/chat`, providing the thread ID and their message. The assistant then responds with relevant information or code snippets.

- **OpenAI Compatibility Check:** The code ensures compatibility with the required version of the OpenAI library.

## Components

- **main.py:** This file contains the Flask app setup and endpoints for starting a conversation (`/start`) and chatting (`/chat`) with the assistant.

- **functions.py:** This module includes functions for creating a new assistant or loading an existing one using OpenAI's API. It also manages the assistant's data storage.

## Requirements

- Python 3.x
- Flask
- OpenAI library (`openai`)
- Ensure OpenAI version is compatible (>= 1.1.1)

## Usage

1. Set up the required environment variables, including `OPENAI_API_KEY` in `main.py`. You need to create an OpenAI account and generate an API key, which you would input into the `open_ai_api_key` section of this code. You can use free OpenAI credits for testing, or add funds to your account if needed.
   - [Sign up for OpenAI here](https://platform.openai.com/signup)

2. Add `main.py`, `functions.py`, and the knowledge document to your Replit environment.

3. Run `main.py`. Upon execution, `assistant.json` will be created if it does not exist already. This file will contain an assistant id, reflecting that you have established a connection between OpenAI and your Replit successfully.

4. Voiceflow integration: You need to set up an account with Voiceflow. Download the Voiceflow template from the resources folder on Replit, then import and configure it in your Voiceflow account. Replace the Voiceflow template's URL with the URL of your Replit environment, where all the code files are hosted. Ensure you publish the Voiceflow template to deploy the chat interface. Use the generated HTML script to embed the chat widget on your Carrd website or any other webpage. 

5. Start a conversation with the assistant by sending a GET request to `/start`.

6. Interact with the assistant by sending POST requests to `/chat` with the appropriate data format.

## Additional Notes

- The assistant's behavior and responses are driven by a knowledge document (`knowledge.docx`) provided in the code. This document contains extensive information on algorithms, their complexities, data structures, sorting and search algorithms, dynamic programming, and more.

- The assistant's scope is limited to computer science algorithm-related topics. It provides educational content, explanations, and code snippets tailored to assist users in understanding algorithmic concepts.

- The code structure allows for easy scalability and integration with other systems or platforms.