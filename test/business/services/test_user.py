# test/business/services/test_users.py

from unittest.mock import MagicMock

import pytest

from app.business.users.models.user import CreateUserRequest
from app.business.users.services.user import UserService
from app.domain.users.models.user import User
from app.domain.users.repositories.user import UserSQLRepository


class TestUserService:

    @pytest.mark.asyncio
    async def test_create_user(self):
        # Arrange
        mock_repository = MagicMock(spec=UserSQLRepository)
        user_service = UserService(repository=mock_repository)

        create_req = CreateUserRequest(username="testuser", email="test@example.com", password="testpassword")
        expected_user = User(id=1, username="testuser", email="test@example.com", password="testpassword")

        # Mock the repository's create method to return the expected user
        mock_repository.create.return_value = expected_user

        # Act
        actual_user = await user_service.create_user(create_req)

        # Assertions
        assert actual_user == expected_user
        mock_repository.create.assert_called_once_with(create_req=create_req)
