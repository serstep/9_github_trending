import datetime
import requests


def get_week_ago_date_string():
    week = datetime.timedelta(weeks=1)
    today = datetime.date.today()
    week_ago_date = today - week

    return week_ago_date.isoformat()


def get_trending_repositories(required_count):
    week_ago_date = get_week_ago_date_string()
    payload = {'q':'created:>{}'.format(week_ago_date), "per_page":str(required_count), "sort":"stars"}
    response = requests.get("https://api.github.com/search/repositories", params=payload)
    trend_repositories = response.json()
    
    if "items" not in trend_repositories:
        return None

    return [(repo["html_url"], repo["name"], repo["stargazers_count"], repo["open_issues"])\
     for repo in trend_repositories["items"]]
    

if __name__ == '__main__':
    required_count = 20
    try:
        trend_repositories = get_trending_repositories(required_count)
    except requests.exceptions.RequestException:
        print("Ошибка соединения")
        exit(1)

    if trend_repositories is None:
        print("Ошибка обработки данных")
        exit(1)

    for url, name, stars_count, issues_count in trend_repositories:
        print("Имя: {}\nURL: {}\nКоличество звезд: {}\nКоличество задач: {}\n".format(name, url, stars_count, issues_count))
