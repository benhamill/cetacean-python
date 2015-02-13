> Everything the system does *for* you, the system also does *to* you.
> <br>—Don Leaver

# Cetacean

The [HAL](http://stateless.co/hal_specification.html) client that does almost
nothing for/to you.

Cetacean is tightly coupled to [Requests](https://pypi.python.org/pypi/requests),
but doesn't actually call it. You set up your own Requests client and use it to
make requests. You feed Cetacean Requests response objects and it helps you
figure out if they're HAL documents and pull useful data out of them if they
are.

## Usage

Something like this:

```python
import requests
from cetacean import Cetacean

root = Cetacean(requests.get("http://api.example.com/"))
users = Cetacean(requests.get(root.get_uri))
user = users.embedded('users')[0]

important_blog_post = Cetacean(requests.get(user.expand_uri('post', { 'id': 2 })))

interesting_blog_posts = Cetacean(requests.get(user.expand_uri('search_posts', { 'q': 'interesting' })))
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
