# AI Meeting Notes Agent

This project uses OpenAI APIs to analyze meeting notes and generate:

- Meeting summaries
- Action items
- Risks
- Follow-up tasks

## Tech Stack

- Python
- OpenAI API
- python-dotenv

## Features

- Reads meeting notes from text file
- Sends notes to OpenAI model
- Generates structured AI summary
- Writes output into a fresh text file

## Project Structure

ai-meeting-agent/
│
├── app.py
├── meeting_notes.txt
├── meeting_summary.txt
├── requirements.txt
├── .gitignore

## How To Run

Install packages:

pip install -r requirements.txt

Run application:

python app.py