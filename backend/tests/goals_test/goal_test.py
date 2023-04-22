import pytest


@pytest.mark.django_db
def test_goal_create(client, get_credentials, goal, goal_category, board_participant):
    """Создание цели"""

    data = {
        "category": goal_category.id,
        "title": "title",
        "description": "description",
        "status": goal.status,
        "priority": goal.priority,
        "due_date": '2023-05-01T00:00:00+03:00',
    }

    response = client.post(
        path='/goals/goal/create',
        HTTP_AUTHORIZATION=get_credentials,
        data=data,
        content_type='application/json'
    )

    assert response.status_code == 201
    assert response.data['category'] == data['category']
    assert response.data['title'] == data['title']
    assert response.data['description'] == data['description']
    assert response.data['status'] == data['status']
    assert response.data['priority'] == data['priority']
    assert response.data['due_date'] == '2023-05-01T00:00:00+03:00'


@pytest.mark.django_db
def test_goal_update(client, get_credentials, goal, board_participant):
    """Обновление цели"""

    title = 'title'

    response = client.patch(
        path=f'/goals/goal/{goal.id}',
        HTTP_AUTHORIZATION=get_credentials,
        data={'title': title},
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.data.get('title') == title


@pytest.mark.django_db
def test_goal_delete(client, get_credentials, goal, board_participant):
    """Удаление цели"""

    response = client.delete(
        path=f'/goals/goal/{goal.id}',
        HTTP_AUTHORIZATION=get_credentials,
    )

    assert response.status_code == 204
    assert response.data is None
