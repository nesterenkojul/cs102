import string

import nltk
from bayes import NaiveBayesClassifier
from bottle import redirect, request, route, run, template
from db import News, session
from scraputils import get_news

nltk.download("punkt")


def prepare(s):
    translator = str.maketrans("", "", string.punctuation)
    s = s.translate(translator)
    tokens = nltk.word_tokenize(s)
    return tokens


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template("news_template", rows=rows)


@route("/add_label/")
def add_label():
    label = request.query.label
    id = request.query.id
    s = session()
    record = s.query(News).filter(News.id == id).all()[0]
    record.label = label
    s.add(record)
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    new_news = get_news("https://news.ycombinator.com/newest", n_pages=5)
    s = session()
    print(new_news[:5])
    for record in new_news:
        if (
            s.query(News)
            .filter(News.title == record["title"] and News.author == record["author"])
            .first()
            is None
        ):
            data = News(
                title=record["title"],
                author=record["author"],
                url=record["url"],
                comments=record["comments"],
                points=record["points"],
                label=None,
            )
            s.add(data)
    s.commit()
    redirect("/news")


@route("/classify")
def classify_news():
    s = session()
    labeled = s.query(News).filter(News.label != None).all()
    X = [row.title for row in labeled]
    Y = [row.label for row in labeled]
    X = [prepare(x) for x in X]
    X_train, Y_train = X[: round(len(labeled) * 0.7)], Y[: round(len(labeled) * 0.7)]
    X_test, Y_test = X[round(len(labeled) * 0.7) :], Y[round(len(labeled) * 0.7) :]
    model = NaiveBayesClassifier(1)
    model.fit(X_train, Y_train)
    print(model.score(X_test, Y_test))
    unlabeled = s.query(News).filter(News.label == None).all()
    X_class = [prepare(row.title) for row in unlabeled]
    predictions = model.predict(X_class)
    classified_news = []
    second_priority = []
    third_priority = []
    for i in range(len(unlabeled)):
        if predictions[i] == "good":
            classified_news.append(unlabeled[i])
        elif predictions[i] == "maybe":
            second_priority.append(unlabeled[i])
        else:
            third_priority.append(unlabeled[i])
    classified_news.extend(second_priority)
    classified_news.extend(third_priority)
    return template("news_recommendations", rows=classified_news)


if __name__ == "__main__":
    run(host="localhost", port=8080)
