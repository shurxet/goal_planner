import pytest


@pytest.mark.django_db
def test_user_create(client, django_user_model):
    """Тест создания пользователя"""

    data = {
        'username': 'username',
        'password': 'password00000000',
        'password_repeat': 'password00000000',
    }

    response = client.post(
        path='/core/signup',
        data=data,
        content_type='application/json'
    )

    user = django_user_model.objects.first()

    expected_response = {
        'id': user.id,
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email
    }

    assert response.status_code == 201
    assert response.data == expected_response
