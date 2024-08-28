# AlgoWhiz: AI-Powered Chatbot for Learning Computer Science Algorithms

AlgoWhiz is an advanced AI-powered learning tool designed to assist students in mastering computer science algorithms. By leveraging cutting-edge AI technologies, AlgoWhiz serves as an interactive chatbot embedded in a web interface, offering personalized explanations, visualizations, and practice tasks related to various algorithms frequently covered in computer science curricula.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Features](#features)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Technical Details](#technical-details)
- [Challenges and Future Enhancements](#challenges-and-future-enhancements)
- [Contributors](#contributors)
- [License](#license)

## Introduction

AlgoWhiz aims to simplify the learning of complex computer science algorithms by providing a user-friendly AI assistant. The platform covers a wide range of algorithms, including sorting techniques, graph algorithms, and search methods, with detailed explanations and step-by-step instructions to enhance understanding.

The project was developed as part of a senior capstone course (CS4366) at Texas Tech University, under the supervision of Professor [Advisor Name]. It is a collaboration between Dhruv Maniar and Isha Koregave.

## Project Structure

The project consists of the following main components:

- **Frontend Interface**: Built using Carrd for a simple and responsive design.
- **Backend Server**: Hosted on Replit, the backend is implemented using Flask.
- **AI Model Integration**: OpenAI's Assistant API is used for processing user queries and generating responses.
- **Voiceflow Integration**: Manages conversational flows, enhancing user interaction with the AI model.

### Files and Directories

- `main.py`: The main Flask application that handles the backend operations, including communication with OpenAI's API.
- `functions.py`: Utility functions for managing AI assistants and handling interactions with the OpenAI API.
- `assistant.json`: Configuration file for storing the assistant's ID after creation.
- `voiceflow.png`: Visual representation of the Voiceflow integration used in the project.
- `AlgoWhiz Technical Document.pdf`: Detailed documentation of the project, including system architecture, algorithms, and validation results.

## Features

- **Interactive Learning**: Engage with the AI chatbot to receive explanations, examples, and code snippets related to various algorithms.
- **Real-Time Response**: Immediate feedback and answers to algorithm-related queries.
- **Educational Content**: Comprehensive explanations, examples, and step-by-step guides for understanding algorithms.
- **Analytics and Progress Tracking**: Track your learning journey and monitor progress over time.

## Installation and Setup

### Prerequisites

- **Python 3.x**
- **Replit Account**: To run the backend server.
- **OpenAI Account**: To access the Assistant API.
- **Voiceflow Account**: For managing conversational flows.

### Steps to Setup

1. **Fork the Replit Project**: 
   - Visit [AlgoWhiz Replit](https://replit.com/@DhruvManiar/AlgoWhiz?v=1) and fork the project to your own Replit account.
   
2. **Install Dependencies**:
   - Run the following command to install necessary Python packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Set OpenAI API Key**:
   - Obtain your OpenAI API key and set it as an environment variable in Replit:
     ```bash
     export OPENAI_API_KEY='your-api-key'
     ```

4. **Run the Server**:
   - Start the Flask server:
     ```bash
     python main.py
     ```

5. **Access the Frontend**:
   - Navigate to the Carrd website linked with Voiceflow for interaction.

## Usage

- **Starting a Conversation**:
  - Use the `/start` endpoint to initiate a new conversation thread with the assistant.
  
- **Asking Questions**:
  - Send POST requests to the `/chat` endpoint with your question to receive AI-generated responses.

- **Real-Time Interaction**:
  - Interact with the chatbot through the Carrd interface embedded with Voiceflow.

## Technical Details

### System Architecture

- **Frontend**: Built with Carrd, integrated with Voiceflow for managing interactions.
- **Backend**: Implemented using Flask, hosted on Replit.
- **AI Model**: Uses OpenAI's Assistant API for generating responses.
- **Voiceflow**: Manages the conversational logic and ensures a smooth user experience.

### Algorithms and Data Flow

- **Input Processing**: Utilizes NLP to understand user queries and retrieve relevant information.
- **Response Generation**: The AI model generates responses based on the user's input and the context provided.
- **Analytics**: Tracks user interactions to provide insights and improve the learning experience.

## Challenges and Future Enhancements

- **Scalability**: Ensuring the system can handle a large number of users simultaneously.
- **Enhanced Personalization**: Developing features for more personalized learning experiences based on individual progress.
- **Complex Query Handling**: Improving the AI's ability to handle more complex algorithmic questions.

## Contributors

- **Dhruv Maniar**: Website development, AI fine-tuning, and project management.
- **Isha Koregave**: Backend development, Voiceflow integration, and presentation creation.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

For more detailed information about the project, including the system architecture, algorithms, and flowcharts, please refer to the [AlgoWhiz Technical Document](./AlgoWhiz%20Technical%20Document.pdf).
