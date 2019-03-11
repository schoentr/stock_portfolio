from src.models import Company, Portfolio, User

class TestCompanyModel:
    """
    """
    def test_create_company(self, company):
        """
        """
        assert comapny.id > 0

    def test_company_name(self, company):
        """
        """
        assert company.name == 'Microsoft'

    def test_company_symbol(self, company):
        """
        """
        assert company.symbol == 'MSFT'

    def test_company_portfolio_id(self, company):
        """
        """
        assert company.portfolio_id > 0


class TestCategoryModel:
    """
    """
    def test_create_category(self, category):
        """
        """
        assert category.id > 0

    def test_category_name(self, category):
        """
        """
        assert category.name is not None

    def test_category_user_id(self, category):
        """
        """
        assert category.user_id > 0


class TestUserModel:
    """
    """
    def test_user_create(self, user):
        """
        """
        assert user.id > 0

    def test_user_email(self, user):
        """
        """
        assert user.email == 'default@example.com'

    def test_user_check_password(self, user):
        """
        """
        from src.models import User
        assert User.check_password_hash(user, 'secret')
