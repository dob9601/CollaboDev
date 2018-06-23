from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage, default_storage


def clean_profile_changes(first_name, last_name, biography, url, reset_background, background, reset_avatar, avatar, user):
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

    if reset_background:
        old_filename = user.profile.background.name
        if old_filename != '':
            default_storage.delete(old_filename)
        user.profile.background = None
        success_list.append('background')
    elif background:
        fs = FileSystemStorage()
        extension = background.name[background.name.rfind(".")+1:]
        if extension in ['jpg', 'jpeg', 'jpe', 'jif', 'jfif', 'jfi', 'png']:
            filename = user.username + '_background.' + extension
            old_filename = user.profile.background.name
            if old_filename != '':
                default_storage.delete(old_filename)
            image = fs.save(filename, background)
            user.profile.background = image
            user.profile.background_version += 1
            success_list.append('background')
        else:
            errors.append('background')

    if reset_avatar:
        old_filename = user.profile.avatar.name
        if old_filename != '':
            default_storage.delete(old_filename)
        user.profile.avatar = None
        success_list.append('profile picture')
    if avatar:
        fs = FileSystemStorage()
        extension = avatar.name[avatar.name.rfind(".")+1:]
        if extension in ['jpg', 'jpeg', 'jpe','jif', 'jfif', 'jfi', 'png']:
            filename = user.username + '_avatar.' + extension
            old_filename = user.profile.avatar.name
            if old_filename != '':
                default_storage.delete(old_filename)
            image = fs.save(filename, avatar)
            user.profile.avatar = image
            user.profile.avatar_version += 1
            success_list.append('profile picture')
        else:
            errors.append('profile picture')

    return [user, success_list, errors]


def clean_password_changes(old_pword, new_pword, new_pword_conf, user,
                           request):
    errors = []
    success_list = []

    if old_pword != '' or new_pword != '':
        if not user.check_password(old_pword):
            errors.append('old_pword')

        elif new_pword != new_pword_conf:
            errors.append('pword_conf')
        else:
            user.set_password(new_pword)
            update_session_auth_hash(request, user)
            success_list.append('password')

    return [user, success_list, errors]
