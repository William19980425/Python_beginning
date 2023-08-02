from operator import itemgetter
import requests

#执行API调用并查看响应
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r= requests.get(url)
print(f"Status Code:{r.status_code}")

#处理有关每篇文章的信息
submission_ids = r.json()
submisson_dicts = []

for submission_id in submission_ids[:5]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r= requests.get(url)
    print(f"id:{submission_id}\t status: {r.status_code}")
    response_dict = r.json()

    #对于每篇文章，都创建一个字典
    submisson_dict = {
        'title':response_dict['title'],
        'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
        'comments':response_dict['descendants']
    }
    submisson_dicts.append(submisson_dict)

submisson_dicts = sorted(submisson_dicts,key=itemgetter('comments'),reverse=True)

for submission_dict in submisson_dicts:
    print(f"\nTitle:{submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")