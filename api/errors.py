# just kiddine
def g_error(text):
	return {'error': text}

def db_error():
	return g_error("Db error")

def query_error():
	return g_error('Query param required')

def wrong_credentials_error():
	return g_error('Wrong credentials provided')

def no_resource_error():
	return g_error('No resource')

def unauthorized_error():
	return g_error('unauthorized access')
