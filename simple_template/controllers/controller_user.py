from typing import List


class UserController:
    def __init__(self, user_service):
        self.user_service = user_service

    def get_users(self) -> List[str]:
        return self.user_service.get_users()
    
    def test_controller(self):
        return "test_controller"