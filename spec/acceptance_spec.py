# encoding: utf-8
# from .context import cetacean
from expects import *
import json

from cetacean import Cetacean

with describe("Cetacean"):
    with context("when fed a valid HAL document"):
        with before.each:
            self.subject = Cetacean(
                json.dumps(
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
                )
            )

        with it("can find links by rel"):
            expect(self.subject.get_uri('self')).to(equal('/'))

        with it("hands out the links hash"):
            expect(self.subject.links).to(equal({ 'self': { 'href': '/' } }))

        with it("allows access to attributes with []"):
            expect(self.subject['api_ranking']).to(equal('the best'))

        with it("allows access to attributes with get()"):
            expect(self.subject.get('api_ranking')).to(equal('the best'))

        with it("does defaulting on attribute get()s"):
            expect(self.subject.get('not_an_attribute', 'default')).to(equal('default'))

        with it("hands out a hash of attributes"):
            expect(self.subject.attributes).to(equal({'api_ranking': 'the best'}))

        with _it("lists embedded resources"):
            pass

        with _it("handles singular embedded resources"):
            pass

        with _it("handles plural embedded resources"):
            pass

        with _it("allows index access on plural embedded resources"):
            pass

    with context("when fed non-JSON"):
        with it("raises an error"):
            try:
                Cetacean("<html></html>")
            except Exception, e:
                expect(e).to(be_a(ValueError))
