# Copyright (c) 2015, Matthew Else matthewelse1997@gmail.com

# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from django.conf.urls import url

from scorer import views

urlpatterns = ['',
    url(r'^bigscreen/$', views.big_screen),
    url(r'^podium/$', views.podium),
    url(r'^rank/$', views.rank),
    url(r'^status/$', views.get_status),
    url(r'^setstatus/(?P<type>\w+)$', views.set_status),
    url(r'^controls/$', views.controls),
    url(r'^exportcsv/$', views.export_csv),
    url(r'^top3/$', views.top3)
              ]
