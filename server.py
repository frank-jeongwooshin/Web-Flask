from flask import Flask
from flask import request, redirect
import random

app = Flask(__name__)

nextID = 7
topics = [
    {'pageNumber' : 1, 'title' : 'html', 'body' : 'Welcome To HTML'},
    {'pageNumber' : 2, 'title' : 'css', 'body' : 'Welcome To CSS'},
    {'pageNumber' : 3, 'title' : 'jave script', 'body' : 'Welcome To JavaScript'},
    {'pageNumber' : 4, 'title' : 'flask', 'body' : 'Welcome To Flask'},
    {'pageNumber' : 5, 'title' : 'python', 'body' : 'Welcome To Python'},
    {'pageNumber' : 6, 'title' : 'C++', 'body' : 'Welcome To C++'}
]

def template(contents, content, pageNumber=None):
    contextUI = ""
    if pageNumber != None:
        contextUI = f'''
            <li><a href="/update/{pageNumber}/"> update </a></li>
            <li><form action="/delete/{pageNumber}/" method="POST"><input type="submit" value="delete"></form></li>
        '''

    return f'''
    <!doctype html>
    <html>
        <body>
            <h1><a href="/"> WEB </a> </h1>
            <ol>
                {contents}
            </ol>
            {content}
            <ul>
                <li><a href="/create/"> create </a></li>
                {contextUI}
            </ul>
        </body>
    </html>
    '''

def getContents():
    liTags = ""
    for topic in topics:
        liTags = liTags + f'<li><a href="/page/{topic["pageNumber"]}/"> {topic["title"]} </a></li>'
    return liTags

@app.route('/')
def index():
    content = '''
    <h2> Index Page </h2>
    <p> Summa Cum Laude </p>
    '''

    idxContent = template(getContents(), content)
    return idxContent

@app.route('/page/<int:pageNumber>/')
def page(pageNumber):
    title = ''
    body = ''
    for topic in topics:
        if topic["pageNumber"] == pageNumber:
            title = topic["title"]
            body = topic["body"]
            break

    content = f'''
    <h2> {title} </h2>
    <p> {body} </p>
    '''
    pageContent = template(getContents(), content, pageNumber)
    return pageContent

@app.route('/create/', methods = ['GET', 'POST'])
def create():
    global nextID
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        newTopic = {'pageNumber':nextID, 'title':title, 'body':body}
        url = '/page/'+str(nextID)+'/'
        nextID += 1
        topics.append(newTopic)
        return redirect(url)
    
    content = '''
    <form action="/create/" method="POST">
        <p><input type = "text" name="title" placeholder="title"></p>
        <p><textarea name="body" placeholder="body"></textarea></p>
        <p><input type="submit" value="create"></p>
    </form>
    '''
    return template(getContents(), content)

@app.route('/update/<int:id>/', methods = ['GET', 'POST'])
def update(id):
    global nextID
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        for topic in topics:
            if topic['pageNumber'] == id:
                topic['title'] = title
                topic['body'] = body
                break

        url = '/page/'+str(id)+'/'
        return redirect(url)
    

    title = ''
    body = ''
    for topic in topics:
        if topic["pageNumber"] == id:
            title = topic["title"]
            body = topic["body"]
            break

    content = f'''
    <form action="/update/{id}/" method="POST">
        <p><input type = "text" name="title" placeholder="title" value="{title}"></p>
        <p><textarea name="body" placeholder="body">{body}</textarea></p>
        <p><input type="submit" value="update"></p>
    </form>
    '''
    return template(getContents(), content)

@app.route('/delete/<int:id>/', methods=['POST'])
def delete(id):
    for topic in topics:
        if id == topic["pageNumber"]:
            topics.remove(topic)
            break
    return redirect('/')

# port를 변경하려면 Parameter로 아래와 같이 실행
# app.run(port=5001)
app.run(debug=True)