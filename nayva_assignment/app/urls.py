from flask import Blueprint

import views

mod = Blueprint('app', __name__)

mod.add_url_rule('/', view_func=views.index, methods=['GET'])
mod.add_url_rule(
    '/user/<user_id>', view_func=views.get_permissions, methods=['GET'])
mod.add_url_rule(
    '/check_permission/<user_id>/<permission_id>',
    view_func=views.check_permission, methods=['GET'])
mod.add_url_rule(
    '/update_roles/roles/<role_id>',
    view_func=views.update_roles, methods=['POST'])
mod.add_url_rule(
    '/delete_permission/permissions/<permission_id>',
    view_func=views.delete_permission, methods=['DELETE'])
