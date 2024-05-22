def render_user_list(users):
    return [
        {
            "id": user.id,
            "username": user.username,
            "password": user.password_hash,
            "roles": user.roles,
        }
        for user in users
    ]

def render_user_detail(user):
    return {
            "id": user.id,
            "username": user.username,
            "password": user.password_hash,
            "roles": user.roles,
        }
    