def parse_salary(text): 
    try: 
        salary = float(text) 
        if salary<0:
            return None
        return salary
    except ValueError: 
        return None 
    
def is_valid_email(email):
    if " " in email:
        return False

    if "@" not in email:
        return False

    parts = email.split("@")

    if len(parts) != 2:
        return False

    if not parts[0] or "." not in parts[1]:
        return False

    if parts[1].startswith(".") or parts[1].endswith("."):
        return False

    return True