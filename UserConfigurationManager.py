test_settings={'Theme':'light','Notifications':'disabled'}

def add_setting(settings,keyvalpair):
    key=keyvalpair[0].lower()
    val=keyvalpair[1].lower()

    if key in settings:
        return f'''Setting '{key}' already exists! Cannot add a new setting with this name.''' 

    else:
        settings[key]=val
        return f'''Setting '{key}' added with value '{val}' successfully!'''

print(add_setting({'theme': 'light'}, ('volume', 'high')))

def update_setting(settings,keyvalpair):
    key=keyvalpair[0].lower()
    value=keyvalpair[1].lower()

    if key in settings:
        settings[key]=value
        return f'''Setting '{key}' updated to '{value}' successfully!'''
    
    else:
        return f'''Setting '{key}' does not exist! Cannot update a non-existing setting.'''

def delete_setting(settings,key):
    key=str(key).lower()
    if key in settings:
        settings.pop(key)
        return f'''Setting '{key}' deleted successfully!'''
    
    else:
        return 'Setting not found!'


def view_settings(settings):
    if settings=={}:
        return 'No settings available.'
    else:
        l=list(settings.items())
        n=len(l)
        s='Current User Settings:\n'
        for j in range(n):
            s+=f'{l[j][0].capitalize()}: {l[j][1]}\n'
        
        return s

print(view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}))

    
    
