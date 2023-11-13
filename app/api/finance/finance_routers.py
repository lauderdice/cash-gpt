from http import HTTPStatus

from flask import Blueprint, current_app, jsonify, request
from flask_pydantic_spec import Request, Response

import app.common.constants as C
from app.api.finance.finance_schemas import NewSingleTransactionResponseSchema, \
    NewSingleTransactionRequestSchema
from app.dependencies.apispec import apispec
from app.dependencies.security import sample_apikey_auth
from app.services.transactions_management import add_single_transaction

finance = Blueprint('finance', __name__, url_prefix="/finance")


@finance.route('/', methods=[C.POST_METHOD])
@sample_apikey_auth.login_required()
@apispec.validate(body=Request(NewSingleTransactionRequestSchema), resp=Response(HTTP_200=NewSingleTransactionResponseSchema, HTTP_403=None), tags=['finance'])
def get_sample_response():
    try:
        request_body: NewSingleTransactionRequestSchema = request.context.body
        result = add_single_transaction(request_body)
        return result
    except:
        current_app.logger.exception(C.THERE_WAS_PROBLEM_PROCESSING)
        return Response(status=HTTPStatus.BAD_REQUEST, response=C.THERE_WAS_PROBLEM_PROCESSING)