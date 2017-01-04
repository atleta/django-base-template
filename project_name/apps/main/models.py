"""
(C) 2016 - Laszlo Marai <atleta@atleta.hu>
"""

from django.contrib .auth.models import (AbstractBaseUser, AbstractUser, PermissionsMixin,
    UserManager)
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    """User model for email based authentication. As sad as it is, much of it has been copied
    from Django's AbstractUser class
    """

    email = models.EmailField(_('email address'), unique=True, db_index=True)

    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_(
                                       'Designates whether the user can log into this admin '
                                       'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as '
                                        'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_verified = models.BooleanField(_('verified'), default=False,
                                   help_text=_('User email has been verified'))


    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        "Returns the short name for the user."
        return ''

    def get_profile(self):
        return None
