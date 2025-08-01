# Voice Agents SDK Sample App

Real Estate Voice Agent - Take-Home Coding Assessment
This project is a modified version of the OpenAI Voice Agent SDK sample, adapted to serve as a voice-controlled real estate assistant. It routes user queries to specialized subagents that handle either property sales or rentals, using real data samples.

Overview
The app uses a main front agent that directs conversations to one of two subagents:

Sales agent: Searches houses for sale using a dataset sampled from Perth House Prices (Kaggle).

Rental agent: Searches rental listings using a dataset sampled from Airbnb Open Data (Kaggle).

The datasets are loaded from CSV files and filtered by location and price as requested by the user.

Agents return top matching listings in JSON format.

The voice agent backend is built on FastAPI and uses the OpenAI Agents SDK for conversation handling and tool integration.

Implementation Details
Created Python functions to filter sale and rental properties based on user inputs (location and max_price).

Wrapped these functions as tools using the SDK's @function_tool decorator, making them callable by agents.

Defined two subagents with clear instructions and assigned their respective tools.

Developed a main triage agent that interprets user intent and delegates queries to the correct subagent.

Integrated the agents into the existing voice workflow, enabling multi-turn conversations with voice input/output.

Used detailed inline comments to explain code functionality and design decisions.

Known Limitations
The app currently returns results as JSON strings, which is functional but not fully polished for end-user presentation.

Occasional API errors occur related to duplicated message IDs, impacting stability in streaming responses.

Further improvements could include better conversational formatting, error handling, and UI enhancements.

Tools Used
OpenAI Agents SDK for agent orchestration and conversation management.

Pandas for CSV data loading and filtering.

FastAPI to build the backend API and websocket server.

ActivityWatch to track development workflow (included in final submission).
