# Cultural Translator with AI - Android App

## Overview
A Python-based Android application that translates Angolan cultural slang and expressions for tourists. The app uses Kivy for the GUI, spaCy for natural language processing, and pandas for data handling. Users can type Portuguese phrases and receive detailed explanations of cultural terms with meanings, examples, and cultural context.

## Project Structure
- `main.py` - Kivy Android app with GUI interface
- `test_app.py` - Test script to validate NLP functionality
- `start_app.sh` - Script to run the app with virtual display (for development)
- `datasets/dicionario_cultural2.csv` - Dictionary of Angolan cultural terms and slang
- `requirements.txt` - Python dependencies (spacy, pandas, kivy)

## Technology Stack
- **Language**: Python 3.11
- **GUI Framework**: Kivy 2.3.1 (cross-platform, Android-ready)
- **NLP**: spaCy with Portuguese language model (pt_core_news_sm)
- **Data**: Pandas for CSV processing
- **Deployment**: Ready for Android packaging with Buildozer

## Features
- Modern GUI interface with text input and scrollable results
- Tokenizes Portuguese phrases using spaCy NLP
- Detects Angolan cultural terms and slang
- Provides detailed explanations including:
  - Direct translation/meaning
  - Detailed explanation
  - Usage examples
  - Cultural contextualization
- Tracks usage statistics
- Responsive design with clear/translate buttons

## Dependencies
- spacy (3.8.7)
- pandas (2.3.3)
- kivy (2.3.1)
- pt_core_news_sm (Portuguese language model for spaCy)
- System: xorg.xvfb, mesa, libGL, mtdev (for development)

## How It Works
1. User enters a phrase in Portuguese through the Kivy GUI
2. spaCy tokenizes the text using NLP
3. Each token is checked against the cultural dictionary
4. Matching terms display their cultural translation and context in a scrollable view
5. User can translate multiple phrases and see statistics

## Running in Development
The app is designed for Android but can be tested in Replit:
- Core NLP functionality can be tested with: `python test_app.py`
- Full GUI requires a display (use VNC or deploy to Android device)
- The workflow runs the app with Xvfb (virtual display) for development

## Packaging for Android
To create an Android APK:
1. Install Buildozer: `pip install buildozer`
2. Initialize: `buildozer init`
3. Edit `buildozer.spec` to include all dependencies
4. Build: `buildozer -v android debug`
5. Deploy to device or emulator

Note: The app is Android-ready and follows Kivy best practices for mobile deployment.

## Recent Changes
- 2025-10-02: Refactored from CLI to Kivy Android app
  - Implemented GUI with BoxLayout, ScrollView, TextInput, and Buttons
  - Configured for headless development environment
  - Added MTDev input provider configuration
  - Created test script for validating core functionality
  - Maintained all original NLP and translation logic
  - Ready for Android packaging with Buildozer
