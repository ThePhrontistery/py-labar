# tests/test_user_service.py

from unittest.mock import MagicMock
import pytest

from app.business.users.models.user import CreateUserRequest
from app.business.users.services.user import UserService
from app.domain.users.models.user import User
from app.domain.users.repositories.user import UserSQLRepository

SOME_USER_DATA = {"username": "testuser", "email": "test@example.com", "password": "testpassword"}
ANOTHER_USER_DATA = {"username": "anotheruser", "email": "another@example.com", "password": "anotherpassword"}


class TestUserService:

    @pytest.fixture
    def mock_repository(self):
        return MagicMock(spec=UserSQLRepository)

    @pytest.fixture
    def user_service(self, mock_repository):
        return UserService(repository=mock_repository)

    @pytest.mark.asyncio
    async def test_create_user(self, user_service, mock_repository):
        # Given
        create_req = CreateUserRequest(**SOME_USER_DATA)
        expected_user = User(id=1, **SOME_USER_DATA)
        mock_repository.create.return_value = expected_user

        # When
        actual_user = await user_service.create_user(create_req)

        # Then
        assert actual_user == expected_user
        mock_repository.create.assert_called_once_with(create_req=create_req)

    @pytest.mark.asyncio
    async def test_authenticate_user_success(self, user_service, mock_repository):
        # Given
        username = SOME_USER_DATA["username"]
        password = SOME_USER_DATA["password"]

        mock_repository.get_by_username.return_value = User(id=1, **SOME_USER_DATA)

        # When
        result = await user_service.authenticate_user(username, password)

        # Then
        assert result is not None
        assert result.username == username
        assert result.password == password
        mock_repository.get_by_username.assert_called_once_with(username)

    @pytest.mark.asyncio
    async def test_authenticate_user_failure(self, user_service, mock_repository):
        # Given
        username = SOME_USER_DATA["username"]
        password = "wrong-password"

        mock_repository.get_by_username.return_value = User(id=1, **SOME_USER_DATA)

        # When
        result = await user_service.authenticate_user(username, password)

        # Then
        assert result is None
        mock_repository.get_by_username.assert_called_once_with(username)

    @pytest.mark.asyncio
    async def test_authenticate_user_user_not_found(self, user_service, mock_repository):
        # Given
        username = "nonexistentuser"
        password = "testpassword"

        # Mock the repository's get_by_username method to return None
        mock_repository.get_by_username.return_value = None

        # When
        result = await user_service.authenticate_user(username, password)

        # Then
        assert result is None
        mock_repository.get_by_username.assert_called_once_with(username)

    @pytest.mark.asyncio
    async def test_get_all_users(self, user_service, mock_repository):
        # Given
        expected_users = [
            User(id=1, **SOME_USER_DATA),
            User(id=2, **SOME_USER_DATA)
        ]
        mock_repository.get_all_users.return_value = expected_users

        # When
        actual_users = await user_service.get_all_users()

        # Then
        assert actual_users == expected_users
        mock_repository.get_all_users.assert_called_once()

    @pytest.mark.asyncio
    async def test_exists_user_true(self, user_service, mock_repository):
        # Given
        username = SOME_USER_DATA["username"]

        mock_repository.get_by_username.return_value = User(id=1, **SOME_USER_DATA)

        # When
        result = await user_service.exists_user(username)

        # Then
        assert result is True
        mock_repository.get_by_username.assert_called_once_with(username)

    @pytest.mark.asyncio
    async def test_exists_user_false(self, user_service, mock_repository):
        # Given
        username = SOME_USER_DATA["username"]

        mock_repository.get_by_username.return_value = None

        # When
        result = await user_service.exists_user(username)

        # Then
        assert result is False
        mock_repository.get_by_username.assert_called_once_with(username)
