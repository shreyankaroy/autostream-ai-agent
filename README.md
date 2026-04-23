# AutoStream AI Agent

## Overview
This project is a conversational AI agent built for a fictional SaaS product, AutoStream. The agent can understand user intent, answer pricing-related questions using a knowledge base, and capture high-intent leads.

## Features
- Intent Detection (Greeting, Pricing, High Intent)
- RAG-based knowledge retrieval
- Lead qualification workflow
- Tool execution for lead capture
- Multi-turn conversation memory

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the agent:
python main.py

## Architecture

This project uses LangGraph to design a structured conversational workflow instead of a simple chatbot. The system is divided into nodes such as intent detection and lead handling. Intent detection determines whether the user is asking for pricing or showing high intent.

For knowledge retrieval, a FAISS vector store is used with HuggingFace embeddings. This enables the agent to retrieve relevant information from a local knowledge base instead of hardcoding responses.

State is managed using a shared dictionary that persists across conversation turns. This allows the agent to remember user inputs like name, email, and platform.

A state-machine-based approach is used for lead capture, ensuring that user details are collected step-by-step before triggering the tool.

## WhatsApp Integration

This agent can be integrated with WhatsApp using Meta's WhatsApp Cloud API. Incoming messages are received through Webhooks in a backend server (Flask/FastAPI). The message is passed to the agent, and the generated response is sent back using the WhatsApp API.

This allows real-time conversational interaction with users on WhatsApp.