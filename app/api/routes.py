import requests as req
from requests import RequestException
from app.api import bp
from flask import request, jsonify, make_response
from datetime import datetime


API_URL = "https://api.github.com"


@bp.route('/repos/<username>/<repo>', methods=['GET',])
def details(username, repo):
    if request.method == 'GET':
        try:
            res = req.get(f"{API_URL}/repos/{username}/{repo}")
        except RequestException:
            json_ = {'status':'error',\
                         'message':'github.com is unreachable!'}
        else:
            res_json = res.json()
            if res_json.get('message'):
                json_ = {'status':'error',\
                         'message':'Invalid username or repo'}
            else:
                json_ = {'status':'ok', 'result':res_json}
    else:
        json_ = {'status':'error', 'message':'Method not supported'}
    response = make_response(jsonify(json_))
    response.headers['Content-Type'] = 'application/json'
    return response, 200


@bp.route('/repos/<username>/<repo>/pulls', methods=['GET',])
def pulls(username, repo):
    if request.method == 'GET':
        period = request.args.get('period', '')
        period = period if period.isdigit() else '0'
        try:
            res = req.get(f"{API_URL}/repos/{username}/{repo}/pulls")
        except RequestException:
            json_ = {'status':'error',\
                         'message':'github.com is unreachable!'}
        else:
            res_json = res.json()
            if isinstance(res_json, dict) and\
                    res_json.get('message') == 'Not Found':
                json_ = {'status':'error', 'message':'Invalid username or repo'}
            else:
                result = []
                now = datetime.now()
                for pull_request in res_json:
                    if not period:
                        result.append(pull_request['html_url'])
                    else:
                        pull_date = datetime.strptime(
                                pull_request['created_at'],
                                "%Y-%m-%dT%H:%M:%SZ")
                        delta = now - pull_date
                        if not pull_request['merged_at'] and\
                                delta.days > int(period):
                            result.append(pull_request['html_url'])
                json_ = {'status':'ok', 'result':result}
    else:
        json_ = {'status':'error', 'message':'Method not supported'}
    response = make_response(jsonify(json_))
    response.headers['Content-Type'] = 'application/json'
    return response, 200


@bp.route('/repos/<username>/<repo>/issues', methods=['GET',])
def issues(username, repo):
    if request.method == 'GET':
        try:
            res = req.get(f"{API_URL}/repos/{username}/{repo}/issues")
        except RequestException:
            json_ = {'status':'error',\
                         'message':'github.com is unreachable!'}
        else:
            res_json = res.json()
            if isinstance(res_json, dict) and\
                    res_json.get('message') == 'Not Found':
                json_ = {'status':'error', 'message':'Invalid username or repo'}
            else:
                result = []
                for issue in res_json:
                    result.append(issue['html_url'])
                json_ = {'status':'ok', 'result':result}
    else:
        json_ = {'status':'error', 'message':'Method not supported'}
    response = make_response(jsonify(json_))
    response.headers['Content-Type'] = 'bp.ication/json'
    return response, 200


@bp.route('/repos/<username>/<repo>/forks', methods=['GET',])
def forks(username, repo):
    if request.method == 'GET':
        a = b/0
        try:
            res = req.get(f"{API_URL}/repos/{username}/{repo}/forks")
        except RequestException:
            json_ = {'status':'error',\
                         'message':'github.com is unreachable!'}
        else:
            res_json = res.json()
            if isinstance(res_json, dict) and\
                    res_json.get('message') == 'Not Found':
                json_ = {'status':'error', 'message':'Invalid username or repo'}
            else:
                result = []
                for fork in res_json:
                    result.append(fork['html_url'])
                json_ = {'status':'ok', 'result':result}
    else:
        json_ = {'status':'error', 'message':'Method not supported'}
    response = make_response(jsonify(json_))
    response.headers['Content-Type'] = 'application/json'
    return response, 200

