from flask import Flask, json, Response, request

from flask_test import db
from flask_test import external

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user(request_data):
    # validation
    loan_amount = request_data['loan_amount']
    if loan_amount  < 10000 or loan_amount > 50000:
        # store denied user in db
        db.create_user()
        db.create_loan(loan_amount, status)
        return Response(json.dumps({'status': 'denied'}, status=201))

    # Store User data and loan application
    user_uuid = db.create_user()
    # Make call to get credit lines for person
    credit_lines = external.get_credit_lines()

    # Use info to validate against business rules
    offer = validate_buisness_rules(credit_lines[0])

    # Store Loan application data in db
    db.create_loan(loan_amount, status)

    return Response(json.dumps(user_data), status=201, mimetype='application/json')


def validate_business_rules(credit_lines):
    if credit_lines > 50:
        return {'status': 'denied'}

    if credit_lines < 10:
        return {'status': 'approved', 'term': 36, 'interest': 10}

    if credit_lines <= 50 and credit_lines >=10:
        return {'status': 'approved', 'term': 24, 'interest': 20}
