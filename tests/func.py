def main(context):
    """
    Provides a function fixture to be used in tests
    """
    if "cloud_event" in context:
        event = context["cloud_event"]
        return event.data["message"], 200
    else:
        data = context["request"].get_json(silent=True)
        print(data)
        return data["message"]