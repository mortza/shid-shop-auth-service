from application.models import User, Token, VCode


class UserRepositoryBase:
    """
    base class for user repository
    """

    def register(self, clean_data: dict) -> None:
        pass

    def update(self, clean_data: dict, key: str):
        pass

    def login(self, clean_data: dict) -> [Token, dict]:
        pass

    def logout(self, clean_data: dict) -> Token:
        pass

    def page_recovery(self, clean_data: dict, key: str) -> dict:
        pass

    def delete(self, clean_data: dict) -> Token:
        pass

    def create_verify_code(self, clean_data: dict, key: str) -> dict:
        pass

    def check_code(self, clean_data: dict, key: str) -> bool:
        pass

    # def add_address(self, clean_data: dict) -> dict:
    #     pass
    #
    # def get_addresses(self, clean_data: dict) -> dict:
    #     pass

    def active_session(self, clean_data: dict) -> dict:
        pass

    def delete_session(self, clean_data: dict) -> None:
        pass
