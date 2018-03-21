from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def clean_profile_changes(first_name, last_name, biography, url, user):
    errors = []
    success_list = []

    if first_name != user.first_name:
        if first_name == '':
            errors.append('first_name')
        else:
            user.first_name = first_name
            success_list.append('first name')

    if last_name != user.last_name:
        if last_name == '':
            errors.append('last_name')
        else:
            user.last_name = last_name
            success_list.append('last name')

    if biography != user.profile.biography: 
        if len(biography) > 300:
            errors.append('biography')
        else:
            user.profile.biography = biography
            success_list.append('biography')

    if url != user.profile.url:
        if '://' not in url:
            url = 'http://' + url
        try:
            url_validate = URLValidator()
            url_validate(url)

            user.profile.url = url
            success_list.append('url')
        except ValidationError:
            errors.append('url')

    return [user, success_list, errors]
