import json
from agents import Agent, WebSearchTool, function_tool
from agents.tool import UserLocation
import app.real_estate_api as real_estate_api  # Simulación o API real

STYLE_INSTRUCTIONS = (
    "You are a real estate assistant. Use a conversational tone, avoid bullet points or formal formatting."
)

# --------------------------
# TOOLS DEFINITIONS
# --------------------------

@function_tool
def search_properties_for_sale(location: str):
    """Search for properties available for sale in a given location."""
    return real_estate_api.search_properties_for_sale(location)


@function_tool
def search_properties_for_rent(location: str):
    """Search for properties available for rent in a given location."""
    return real_estate_api.search_properties_for_rent(location)


@function_tool
def get_property_details(property_id: str):
    """Get details for a specific property by its ID."""
    return real_estate_api.get_property_details(property_id)
# --------------------------
# AGENTS DEFINITIONS
# --------------------------

sale_agent = Agent(
    name="Property Sales Agent",
    model="gpt-4o-mini",
    instructions=f"You help users find properties to buy. {STYLE_INSTRUCTIONS}",
    tools=[search_properties_for_sale, get_property_details],
)

rental_agent = Agent(
    name="Property Rental Agent",
    model="gpt-4o-mini",
    instructions=f"You help users find properties to rent. {STYLE_INSTRUCTIONS}",
    tools=[search_properties_for_rent, get_property_details],
)

triage_agent = Agent(
    name="Real Estate Triage Agent",
    model="gpt-4o-mini",
    instructions=f"Understand if the user wants to buy or rent a property, and route them to the appropriate agent. {STYLE_INSTRUCTIONS}",
    handoffs=[sale_agent, rental_agent],
)

starting_agent = triage_agent
