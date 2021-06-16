import datetime, http.server, socketserver, http.client, pprint

d = []
with open('info.txt', 'r') as f:
    d = f.read().splitlines()

port = int(d[0])
err = 'ошибок нет'
if len(d) > 1:
    file = str(d[1])
    a = file.find('.')
    type_file = file[a + 1:]
    if type_file != 'html':
        err = 'Error 403'
        file = '2.html'
else:
    err = 'Error 404'
    file = '1.html'


# запуск сервера
class ReqHand(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = file
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# информация
handler = ReqHand
with socketserver.TCPServer(("", port), handler) as httpd:
    info = ("Date: " + str(datetime.datetime.now()) +
            "\nPort: " + str(port) +
            "\nFile name: " + file +
            "\nErrors: " + str(err))
    print(info)
    # вывод заголовков клиента
    connection = http.client.HTTPSConnection("www.journaldev.com")
    connection.request("GET", "/")
    response = connection.getresponse()
    headers = response.getheaders()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint("Headers: {}".format(headers))

    httpd.serve_forever()
