import parlant.sdk as p
from tavily import TavilyClient
from stock_researcher_parlant.config import settings

tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)


@p.tool
async def websearch(context: p.ToolContext, search_query: str) -> p.ToolResult:
    """This tool is performing a websearch.

    Args:
        context (p.ToolContext): The context in which the tool is being used.
        search_query (str): The query to search for.

    Returns:
        p.ToolResult: The result of the websearch.
    """
    response = tavily_client.search(query=search_query)
    return response
