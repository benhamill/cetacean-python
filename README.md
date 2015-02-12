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

TODO: Write usage instructions here


## Contributing

If you'd like to contribute, please see the [contribution guidelines](CONTRIBUTING.md).


## Releasing

Maintainers: Please make sure to follow the [release steps](RELEASING.md) when
it's time to cut a new release.
