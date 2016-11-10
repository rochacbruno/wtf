# coding: utf-8
from flask import abort, redirect, request, url_for
from flask_security import current_user
from flask_admin.contrib.mongoengine import ModelView
from flask_admin import Admin

from .models import Noticia
from .security_models import User, Role


admin = Admin(name='Noticias', template_mode='bootstrap3',
              base_template='admin_base.html')


# Create customized model view class
class SafeModelView(ModelView):

    def is_accessible(self):
        if current_user.is_anonymous:
            return False

        if not current_user.is_active or not current_user.is_authenticated:
            return False
        # if not current_user.has_role('admin'):
        #     return False
        return True

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a
        view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated and not current_user.is_anonymous:
                abort(403)  # denied
            else:
                return redirect(url_for('security.login', next=request.url))


class UserModelView(SafeModelView):
    column_list = ("name", "email", "active", "last_login_at", "login_count")


def configure_admin(app):
    admin.init_app(app)
    admin.add_view(SafeModelView(Noticia))
    admin.add_view(UserModelView(User, category='accounts'))
    admin.add_view(SafeModelView(Role, category='accounts'))
