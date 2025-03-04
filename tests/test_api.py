import json

from flask_test.main import validate_business_rules

# def test_201_create_user(client):
#     request_data = {
#         'name': 'testing user',
#         'address': '123 S Street Seattle WA 98111',
#         'email': 'testing@gmail.com',
#         'phone': '123-123-1234',
#         'ssn': '111-22-3333'
# 
#     }
#     response = client.post('/users', data=json.dumps(request_data))
#     assert response.status_code == 201
#     assert response.json == {"status": "denied"}


def test_validate_business_rules_denied():
    response = validate_business_rules(100)

    assert response == {'status': 'denied'}

def test_36_month_case_validate_business_rules():
    response = validate_business_rules(3)

    assert response['term'] == 36
    assert response['interest'] == 10

def test_24_month_case_validate_business_rules():
    response = validate_business_rules(45)

    assert response['term'] == 24
    assert response['interest'] == 20
