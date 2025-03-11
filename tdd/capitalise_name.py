def cap_name(name: str) -> str:
    name_list = [n[0].upper() + n[1:].lower() for n in name.split()]
    return ' '.join(name_list)
