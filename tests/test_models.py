from src.models import Company


class TestClass:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


    def test_create_company(self, session):
        company = Company(name='General Electric Company', company_sym='GE', latest_price= '10.38')
        session.add(company)
        session.commit()
        assert company.id > 0
        companies = Company.query.all()
        assert len(companies) == 1
        assert companies[0].name == 'General Electric Company'

    def test_create_city_again(self, session):
        company = Company(name='General Electric Company', company_sym='GE', latest_price= '10.38')
        session.add(company)
        session.commit()
        assert company.id > 0
        companies = Company.query.all()
        assert len(companies) == 1

    def test_tc2(self):
        pass
