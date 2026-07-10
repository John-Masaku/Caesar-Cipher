test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume':'high'
}
def add_setting(settings_dict, settings_tup):
    key = settings_tup[0].lower()
    value = settings_tup[1].lower()
    
    if key in settings_dict:
        return f"Setting '{key}' already exits! Cannot add a new setting with this name."

        settings_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dict, settings_tup):
    key = settings_tup[0].lower()
    value = settings_tup[1].lower()
    
    if key in settings_dict:
        settings_tup[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        settings_dict[key] = value
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dict, settings_key):
    key = settings_key[0].lower()

    if key in settings_dict:
        del settings_dict[key]
        return f"Setting '{key}' deleted successfully!"

    else:
        return f"Setting not found!"

def view_settings(settings_dict):
    if settings_dict == {}:
        return "No settings  available"
    else:
        return f'Current User Settings: \n{settings_dict.items()}\n'
    

print(view_settings(test_settings))
   