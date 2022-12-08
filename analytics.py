from Const import bot, dp, cur, region_list, characters, con

def analytics(func: callable):
    total_messages = 0
    users = set()
    total_users = 0

    def analytics_wrapper(message):
        nonlocal total_messages, total_users
        total_messages += 1

        if message.chat.id not in users:
            users.add(message.chat.id)
            total_users += 1
        data = [
            (
                total_users, message.text, total_messages
            )
        ]
        cur.executemany("INSERT INTO analytics VALUES(?, ?, ?)", data)
        con.commit()
        return func(message)

    return analytics_wrapper