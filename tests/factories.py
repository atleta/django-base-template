import factory
from django.contrib.auth.hashers import make_password


DEFAULT_PASSWORD = 'password'

def _pick_choice(choices: Choices):
    return random.choice(list(choices._db_values))

class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User

    @classmethod
    def _create(cls, *args, **kwargs):
        # TODO: implement more robust checking whether password is encrypted or not
        if 'password' in kwargs and not kwargs['password'].startswith('bcrypt_sha'):
            kwargs['password'] = make_password(kwargs['password'])

        # return super(UserFactory, cls)._create(*args, **kwargs)
        return super()._create(*args, **kwargs)

    @factory.post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for group in extracted:
                self.groups.add(group)

    email = factory.Sequence(lambda n: 'user%d@whatever.com' % n)
    username = factory.Faker('user_name')
    password = make_password(DEFAULT_PASSWORD)
    full_name = factory.Faker('name')
