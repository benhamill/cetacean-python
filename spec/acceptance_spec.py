# encoding: utf-8
# from .context import cetacean
from expects import *
import requests
import httpretty
import json

from cetacean import Cetacean

from expects.matchers import Matcher

class be_hal(Matcher):
    def _match(self, response):
        return response.is_hal()

with describe("Cetacean"):
    with before.all:
        httpretty.enable()

    with before.each:
        httpretty.reset()

    with after.all:
        httpretty.disable()

    with context("when fed a valid HAL response"):
        with before.each:
            httpretty.register_uri(
                httpretty.GET,
                "http://api.example.com",
                content_type="application/hal+json",
                body=json.dumps(
                    {
                       '_links': {
                            'self': { 'href': '/' },
                        },
                        'api_ranking': 'the best',
                        '_embedded': {
                            'singular': {
                                '_links': { 'self': { 'href': '/singular' } }
                            },
                            'plural': [
                                { '_links': { 'self': { 'href': '/plural/1' } } },
                                { '_links': { 'self': { 'href': '/plural/2' } } },
                            ]
                        }
                    }
                ),
            )

        with it("knows it's HAL"):
            subject = Cetacean(requests.get("http://api.example.com"))

            expect(subject).to(be_hal())

        with it("can find links by rel"):
            subject = Cetacean(requests.get("http://api.example.com"))

            expect(subject.get_uri('self')).to(equal('/'))

        with it("hands out the links hash"):
            subject = Cetacean(requests.get("http://api.example.com"))

            expect(subject.links).to(equal({ 'self': { 'href': '/' } }))

        with _it("allows access to attributes with []"):
            pass

        with _it("hands out a hash of attributes"):
            pass

        with _it("lists embedded resources"):
            pass

        with _it("handles singular embedded resources"):
            pass

        with _it("handles plural embedded resources"):
            pass

        with _it("allows index access on plural embedded resources"):
            pass

    with context("when fed invalid HAL"):
        with before.each:
            httpretty.register_uri(
                httpretty.GET,
                "http://api.example.com",
                content_type="application/hal+json",
                body="<html></html>",
            )

        with it("thinks it's HAL"):
            subject = Cetacean(requests.get("http://api.example.com"))

            expect(subject).to(be_hal())

        with it("can't find links by rel"):
            subject = Cetacean(requests.get("http://api.example.com"))

            expect(subject.get_uri('self')).to(be(None))

    with context("when fed non-HAL"):
        with before.each:
            httpretty.register_uri(
                httpretty.GET,
                "http://api.example.com",
                content_type="text/html",
                body="<html></html>",
            )

        with it("knows it isn't HAL"):
            subject = Cetacean(requests.get("http://api.example.com"))

            expect(subject).not_to(be_hal())

        with it("can't find links by rel"):
            subject = Cetacean(requests.get("http://api.example.com"))

            expect(subject.get_uri('self')).to(be(None))
