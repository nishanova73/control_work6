def guest_validate(name, email, text):
    errors = {}
    if not name:
        errors['name'] = "The name field is required."
    elif len(name) > 30:
        errors['name'] = "Name's len must be less than 30!!!"
    if not text:
        errors['text'] = "The text field is required."
    elif len(text) > 2000:
            errors['text'] = "Text's len must be less than 2000!!!"
    if not email:
        errors['email'] = "Email field is required"
    if self.status == "active":
        return self.status
    elif self.status == "blocked":
        pass
    return errors