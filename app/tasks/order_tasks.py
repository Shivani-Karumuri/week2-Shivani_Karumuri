import asyncio
import logging


logger = logging.getLogger("shopping_api")


async def process_order_background(
    order_id: int,
    user_email: str,
) -> None:
    """
    Background processing after checkout.

    Later, this can send an email, generate an invoice,
    or notify another service.
    """

    try:
        logger.info(
            "Background order processing started: order_id=%s",
            order_id,
        )

        # This is only to simulate asynchronous work.
        await asyncio.sleep(2)

        logger.info(
            "Order confirmation processed successfully: "
            "order_id=%s, email=%s",
            order_id,
            user_email,
        )

    except Exception:
        logger.exception(
            "Background order processing failed: order_id=%s",
            order_id,
        )
