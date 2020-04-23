# -*- coding: utf-8 -*-

# Copyright © 2017 Roberto Alsina and others.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from __future__ import print_function, unicode_literals

import json
import os

from medium import Client
from nikola import utils
from nikola.plugin_categories import Command

LOGGER = utils.get_logger('Medium')


class CommandMedium(Command):
    """Publish to Medium."""

    name = "medium"
    needs_config = True
    doc_usage = ""
    doc_purpose = "publish to Medium"

    def _execute(self, options, args):
        """Publish to Medium."""
        if not os.path.exists('medium.json'):
            LOGGER.error(
                'Please put your credentials in medium.json as described in the README.')
            return False
        with open('medium.json') as inf:
            creds = json.load(inf)
        client = Client()
        client.access_token = creds['TOKEN']

        user = client.get_current_user()

        self.site.scan_posts()
        feed = client.list_articles(user['username'])

        # https://stackoverflow.com/questions/36097527/how-to-retrieve-medium-stories-for-a-user-from-the-api
        # https://medium.com/@mattioo/latest?format=json
        # https://medium.com/feed/@mattioo
        # https://api.rss2json.com/v1/api.json?rss_url=https://medium.com/feed/@mattioo/

        posts = self.site.timeline

        medium_titles = {item["title"] for item in feed}
        to_post = [post for post in posts if post.title(
        ) not in medium_titles and post.meta('medium')]

        if len(to_post) == 0:
            LOGGER.info("Nothing new to post...")

        for post in to_post:
            m_post = client.create_post(
                user_id=user["id"],
                title=post.title(),
                content=post.text(),
                content_format="html",
                publish_status="public",
                canonical_url=post.permalink(absolute=True),
                tags=post.tags
            )
            LOGGER.info('Published %s to %s' %
                        (post.meta('slug'), m_post['url']))
