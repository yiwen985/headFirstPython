import requests
from pprint import pprint

urls = ('https://www.baidu.com', 'https://www.bilibili.com')

# delay output, wait for all data produced
# for resp in [requests.get(url) for url in urls]:
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)

# orderly output
# for resp in (requests.get(url) for url in urls):
#     print(len(resp.content), '->', resp.status_code, '->', resp.url)

# function generator
# error
# def gen_from_urls(urls) -> tuple:
#     for resp in (requests.get(url) for url in urls):
#         return len(resp.content), resp.status_code, resp.url

# fine
def gen_from_urls(urls) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url

for resp_len, status, url in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)
print()

# the underscore '_' tells to ignore the status code
# good look
urls_res = {url:size for size, _, url in gen_from_urls(urls) }

pprint(urls_res)