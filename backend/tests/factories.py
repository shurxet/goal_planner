import factory
from core.models import User
from goals.models import Goal, GoalCategory, Board, BoardParticipant, GoalComment


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    first_name = 'name'
    last_name = 'name'
    email = 'email@mail.ru'
    password = 'password00000000'
    age = '30'


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = 'title'
    is_deleted = False


class BoardParticipantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BoardParticipant

    board = factory.SubFactory(BoardFactory)
    user = factory.SubFactory(UserFactory)
    role = 1


class GoalCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalCategory

    title = 'title'
    is_deleted = False
    user = factory.SubFactory(UserFactory)
    board = factory.SubFactory(BoardFactory)


class GoalFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Goal

    title = 'title'
    description = 'description'
    user = factory.SubFactory(UserFactory)
    category = factory.SubFactory(GoalCategoryFactory)

    status = 1
    priority = 2
    due_date = '2023-05-01'


class GoalCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoalComment

    text = 'text'
    goal = factory.SubFactory(GoalFactory)
    user = factory.SubFactory(UserFactory)
