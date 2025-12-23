from the_app import application

def new_app(environ, start_response):
    environ['the_app.configval1'] = 'something'
    return application(environ, start_response)
