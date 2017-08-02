def app(environ, start_response):
    try:
        print('start response')
        start_response('200 OK', [('Content-Type', 'text/plain')])
        print('200 ok response')
        queryStr = '\r\n'.join(environ['QUERY_STRING'].split('&'))
        print(queryStr)
    except OSError as err:
        print(err)
    return [bytes(queryStr, encoding="utf8")]
