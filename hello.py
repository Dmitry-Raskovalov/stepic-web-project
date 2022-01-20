#Возвращает строку из параметров запроса разделенных символом конца строки
def application(env, start_response):
	params = env['QUERY_STRING'].split('&')
	resp = b''
	for each in params:
		resp += (each + '\n').encode('utf-8')
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [resp]

