def generate_usernames(email):
    name_part = email.split("@")[0]

    variations = [
        name_part,
        name_part.replace(".", ""),
        name_part.replace("_", ""),
        name_part + "123",
    ]

    return list(set(variations))
