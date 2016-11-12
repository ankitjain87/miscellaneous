from flask import abort, jsonify, request

from app.data import users, roles, permission


def index():
    return "Hello, World!"


def get_permissions(user_id):
    if user_id not in users:
        abort(404)

    perms = []

    for role in users[user_id]:
        if role in roles:
            for perm in roles[role]:
                if perm in permission:
                    perms.append(permission[perm])

    return jsonify({'permissions': perms})


def check_permission(user_id, permission_id):
    if user_id not in users:
        abort(404)

    for role in users[user_id]:
        if role in roles and permission_id in roles[role]:
            return jsonify({'response': True})

    return jsonify({'response': False})


def update_roles(role_id):
    if role_id not in roles:
        abort(404)

    new_permission = request.json.get('permissions', None)
    roles[role_id] = new_permission

    return jsonify({'role': roles[role_id]}), 200


def delete_permission(permission_id):
    if permission_id not in permission:
        abort(404)

    permission.pop(permission_id)

    return jsonify({'response': True})

