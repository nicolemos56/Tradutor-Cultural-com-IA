# Cultural Translator with AI

## Overview
A Python-based CLI application that translates Angolan cultural slang and expressions for tourists. The app uses spaCy for natural language processing to detect cultural terms in Portuguese phrases and provides their meanings, explanations, examples, and cultural context.

## Project Structure
- `main.py` - Main application with NLP engine and CLI interface
- `datasets/dicionario_cultural2.csv` - Dictionary of Angolan cultural terms and slang
- `requirements.txt` - Python dependencies (spacy, pandas)

## Technology Stack
- **Language**: Python 3.11
- **NLP**: spaCy with Portuguese language model (pt_core_news_sm)
- **Data**: Pandas for CSV processing
- **Interface**: Command-line interface (CLI)

## Features
- Tokenizes Portuguese phrases using spaCy
- Detects Angolan cultural terms and slang
- Provides detailed explanations including:
  - Direct translation/meaning
  - Detailed explanation
  - Usage examples
  - Cultural contextualization
- Tracks usage statistics

## Dependencies
- spacy (3.8.7)
- pandas (2.3.3)
- pt_core_news_sm (Portuguese language model for spaCy)

## How It Works
1. User enters a phrase in Portuguese
2. spaCy tokenizes the text
3. Each token is checked against the cultural dictionary
4. Matching terms display their cultural translation and context
5. User can continue translating or exit

## Recent Changes
- 2025-10-02: Initial setup in Replit environment
  - Installed Python 3.11 and dependencies
  - Downloaded Portuguese language model for spaCy
  - Configured workflow for CLI application
  - Added .gitignore for Python project
