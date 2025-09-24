# main.py

import asyncio
import parlant.sdk as p
from dotenv import load_dotenv

load_dotenv(override=True)


async def main():
    async with p.Server(nlp_service=p.NLPServices.anthropic) as server:
        agent = await server.create_agent(
            name="Otto Carmen",
            description="You work at a car dealership",
        )


asyncio.run(main())
