# Zendesk-InSocial Webhook Integration

Welcome to the Zendesk-InSocial Webhook Integration project! This platform automates the process of sending surveys via InSocial APIs to customers when their Zendesk tickets are closed. It also features a live connection feed and user authentication for secure, registered user access.

## Overview

This project integrates Zendesk with InSocial, enhancing customer service efficiency and feedback collection. When a Zendesk ticket is closed, Zendesk sends a webhook call to this platform, then our system triggers a survey dispatch to the customer via InSocial APIs.

## Key Features

- **Webhook Integration:** Automates survey dispatching using Zendesk webhook calls.
- **InSocial API Integration:** Seamlessly sends surveys to customers when tickets are closed.
- **Live Connection Feed:** Provides a real-time feed of webhook activities.
- **User Registration and Authentication:** Ensures that only registered users can access the feed.

## Getting Started

### Prerequisites

- A Zendesk account with admin privileges (to setup webhook calls)
- An InSocial account (To see the responses for surveys)
- An InSocial API secret as well as some template and survey ID's

### Installation

1. **Clone the Repository**
```bash
git clone https://github.com/xmlxss/SocialZendesk.git
```
2. **Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
3. **Configure Variables**
- configure the config.py with the correct API keys, template and survey id's

4. **Run the application**
```bash
python run.py
```

## Usage
- Use ngrok to test the Zendesk webhook events locally. For production, you have to provide the correct url to do the POST requests from zendesk. Also make sure you include the recepients email in the body of the webhook post call in json format.

