import pytest
from goals.serializers import GoalCategorySerializer
from tests.factories import GoalCategoryFactory


@pytest.mark.django_db
def test_category_craete(client, get_credentials, board, user, board_participant):
    """Создание категории"""

    data = {
        'board': board.id,
        'title': 'title',
        'user': user.id,
    }

    response = client.post(
        path='/goals/goal_category/create',
        HTTP_AUTHORIZATION=get_credentials,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data['title'] == data['title']


@pytest.mark.django_db
def test_category_list(client, get_credentials, board_participant):
    """Список категорий"""

    categories = GoalCategoryFactory.create_batch(10, user=board_participant.user, board=board_participant.board)

    response = client.get(
        path='/goals/goal_category/list',
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert response.data == GoalCategorySerializer(categories, many=True).data


@pytest.mark.django_db
def test_category_retrieve(client, get_credentials, goal_category, board_participant):
    """Просмотр категории"""

    response = client.get(
        path=f'/goals/goal_category/{goal_category.id}',
        HTTP_AUTHORIZATION=get_credentials
    )

    assert response.status_code == 200
    assert response.data == GoalCategorySerializer(goal_category).data


@pytest.mark.django_db
def test_category_update(client, get_credentials, goal_category, board_participant):
    """Обновление категории"""

    title = 'title'

    response = client.patch(
        path=f'/goals/goal_category/{goal_category.id}',
        HTTP_AUTHORIZATION=get_credentials,
        data={'title': title},
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.data.get('title') == title


@pytest.mark.django_db
def test_category_delete(client, get_credentials, goal_category, board_participant):
    """Удаление категории"""

    response = client.delete(
        path=f'/goals/goal_category/{goal_category.id}',
        HTTP_AUTHORIZATION=get_credentials,
    )

    assert response.status_code == 204
    assert response.data is None
