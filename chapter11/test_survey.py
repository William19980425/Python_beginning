from survey import AnonymousSurvey
import pytest #引入夹具

@pytest.fixture #装饰器
def language_survey():
    question = "What language did you first learn to speak"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_three_response(language_survey):
    responses = ['English','Spanish','Madarin']

    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses

# -----------------------------------------------------------------------------------------------        
# def test_store_single_response():
#     question = "What language did you first learn to speak"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses

# def test_store_three_response():
#     question = "What language did you first learn to speak"
#     language_survey = AnonymousSurvey(question)
#     responses = ['English','Spanish','Madarin']

#     for response in responses:
#         language_survey.store_response(response)

#     for response in responses:
#         assert response in language_survey.responses