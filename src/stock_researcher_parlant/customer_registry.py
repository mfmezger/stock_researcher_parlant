"""Its necessary to register customers."""

import uuid


async def register_new_customer(server, customer_information) -> None:
    customer = await server.create_customer(
        name=customer_information.name,
        metadata={
            "external_id": uuid.uuid4(),
        },
    )
