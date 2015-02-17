# encoding: utf-8
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

        with it("hands out the links dict"):
            expect(self.subject.links).to(equal({ 'self': { 'href': '/' } }))

        with it("allows access to attributes with []"):
            expect(self.subject['api_ranking']).to(equal('the best'))

        with it("allows access to attributes with get()"):
            expect(self.subject.get('api_ranking')).to(equal('the best'))

        with it("does defaulting on attribute get()s"):
            expect(self.subject.get('not_an_attribute', 'default')).to(equal('default'))

        with it("hands out a dict of attributes"):
            expect(self.subject.attributes).to(equal({'api_ranking': 'the best'}))

        with it("lists embedded resources"):
            expect(self.subject.embedded()).to(have_keys('singular', 'plural'))

        with it("handles singular embedded resources"):
            expect(self.subject.embedded('singular').get_uri('self')).to(equal('/singular'))

        with it("handles plural embedded resources"):
            for index, plur in enumerate(self.subject.embedded('plural')):
                expect(plur.get_uri('self')).to(equal('/plural/{0}'.format(index + 1)))

        with it("allows index access on plural embedded resources"):
            expect(self.subject.embedded('plural')[0].get_uri('self')).to(equal('/plural/1'))

    with context("when fed non-JSON"):
        with it("raises an error"):
            try:
                Cetacean("<html></html>")
            except Exception as e:
                expect(e).to(be_a(ValueError))
