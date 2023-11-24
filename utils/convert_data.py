def convert_data_to_msg(data) -> list:

    def get_title():
        return f'Part - {len(msg)+1}\n\n'

    i = 0
    msg = []

    text = get_title()

    while i < len(data):

        one_line = f"{i + 1}. {data[i][0]}\n"

        if len(text + one_line) > 4096:
            msg.append(text)
            text = get_title()
        else:
            text += one_line

        i += 1

    msg.append(text)

    return msg
