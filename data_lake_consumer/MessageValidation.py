def validate_message(msg) -> None:
    if msg.error():
        raise RuntimeError(msg.error())