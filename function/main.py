def handler(context, event):
    heads_string = ""
    for key, value in event.heads.items():
        heads_string = heads_string + key + "=" + value + ", "
    return "body=" + event.body + ". heads: " + heads_string
