#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2


class MainHandler(webapp2.RequestHandler):
    def post(self):
        km = int(self.request.get("km", 1))
        tiempo = int(self.request.get("tiempo", 1))
        consumoMedio = int(self.request.get("consumoMedio", 1))
        velMedia = str(km / (tiempo / 60))
        consumoTotal = str(consumoMedio * km)
        self.response.write('La velocidad media del trayecto ha sido ' + velMedia + ' km/h y el consumo total ' + consumoTotal + ' litros.')


app = webapp2.WSGIApplication([
    ('/consumo', MainHandler)
], debug=True)
