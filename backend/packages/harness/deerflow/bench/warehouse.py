"""What the warehouse answers about an order."""

import json


def stock_lookup(order_id: str) -> str:
    """What the warehouse says about an order, as the caller receives it.

    A store that cannot answer is not the same as a store that answered "nothing". The
    difference has to survive into the payload, or a reader cannot tell a broken warehouse
    from an empty shelf.
    """
    return json.dumps({"error": "warehouse unavailable", "order_id": order_id})
