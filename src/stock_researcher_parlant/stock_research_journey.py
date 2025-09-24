from stock_researcher_parlant.tools import websearch

import parlant.sdk as p


async def create_book_flight_journey(agent: p.Agent):
    journey = await agent.create_journey(
        title="Stock Research",
        conditions=["The customer wants you to find a company to invest in"],
        description="This journey guides the customer through finding a company to invest in and the due diligance on the company.",
    )

    t1 = await journey.initial_state.transition_to(
        chat_state="Ask if they have a company they want to invest in mind"
    )

    #  Branch out based on the customer's response
    t2 = await t1.target.transition_to(
        condition="They do", chat_state="Get name of the company"
    )

    t3a = await t1.target.transition_to(
        condition="They don't",
        chat_state="Ask them in which region or sector they want to invest in.",
    )

    t3b = await t3a.target.transition_to(tool_state=websearch)

    # Merge back to the main path after choosing a destination.
    # This is done by transitioning into an existing state node.
    await t3b.target.transition_to(state=t2.target, condition="Company selected")

    t4 = await t2.target.transition_to(chat_state="Stock Research")

    t5a = await t4.target.transition_to(tool_state=stock_research)
    t5b = await t5a.target.transition_to(chat_state="Provide ticket details")
