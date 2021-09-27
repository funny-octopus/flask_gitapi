USAGE:

Get repo details:
    "curl http://127.0.0.1:5000/repos/<git_user>/<git_repo>"

Get a list of all pull requests: 
    "curl http://127.0.0.1:5000/repos/<git_user>/<git_repo>/pulls"

Get a list of all pull requests which have not been merged for "X" days or more:
    "curl http://127.0.0.1:5000/repos/<git_user>/<git_repo>/pulls?period=14"

Get a list of all issues:
    "curl http://127.0.0.1:5000/repos/<git_user>/<git_repo>/issues"

Get a list of all forks:
    "curl http://127.0.0.1:5000/repos/<git_user>/<git_repo>/forks"
