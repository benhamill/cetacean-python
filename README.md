> Everything the system does *for* you, the system also does *to* you.
> <br>—Don Leaver

# Cetacean [![Build Status](https://travis-ci.org/benhamill/cetacean-python.svg?branch=master)](https://travis-ci.org/benhamill/cetacean-python) [![Code Climate](https://codeclimate.com/github/benhamill/cetacean-python/badges/gpa.svg)](https://codeclimate.com/github/benhamill/cetacean-python)

The [HAL](http://stateless.co/hal_specification.html) client that does almost
nothing for/to you.

Cetacean doesn't know about HTTP. You set up your own Requests client and use it
to make requests. You feed then Cetacean the decoded bodies as strings and it
helps you pull useful data out of them.

## Usage

Something like this:

```python
import requests
import uritemplate

from cetacean import Cetacean

base_url = "http://api.example.com"
response = requests.get(base_url)
root = Cetacean(response.text)
users = Cetacean(requests.get(base_url + root.get_uri('users')).text)
user = users.embedded('users')[0]

blog_post_template = user.get_uri('post')
blog_post_path = uritemplate.expand(blog_post_template, {'id': 2})
blog_post_url = base_url + blog_post_path

important_blog_post = Cetacean(requests.get(blog_post_url).text)


search_template = user.get_uri('search_posts')
search_path = uritemplate.expand(search_template, {'q': 'interesting'})
search_url = base_url + search_path

interesting_blog_posts = Cetacean(requests.get(search_path).text)
```

Check out the specs for more detailed uses.


## Contributing

If you'd like to contribute, please see the [contribution guidelines](CONTRIBUTING.md).


### Tests

```
$ pip install -r requirements.txt && python setup.py develop
$ mamba
```


## Releasing

Maintainers: Please make sure to follow the [release steps](RELEASING.md) when
it's time to cut a new release.
