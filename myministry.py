from flask import Flask, render_template, request, redirect, Blueprint, url_for, session

application = Flask(__name__)
application.secret_key = b'7\x18\xba\xb2||.\xd4\x11oL\xc82\xc1\xa4I'

@application.route('/')
def Homepage():
    return render_template('pages/homepage.html', useragent=request.headers.get('User-Agent'))

@application.errorhandler(500)
def internal_server_error(error):
    return render_template('pages/error.html', error_code=500, message="Internal Server Error"), 500

@application.errorhandler(404)
def not_found(error):
    return render_template('pages/error.html', error_code=404, message="Page non trouvée"), 404

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
