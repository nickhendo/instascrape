import re

import pytest

from instascrape import Post

@pytest.fixture
def google_post() -> Post:
    google_post_url = f"https://www.instagram.com/p/CAvM5gIp9xX/"
    random_google_post = Post(url=google_post_url)
    random_google_post.static_load()
    return random_google_post

@pytest.mark.scrape_hashtags
def test_scrape_hashtags(google_post, capsys):
    expected_hashtags = ["stayhome", "mysuperg"]

    google_post.scrape_hashtags(status_output=True)

    assert all(hashtags in expected_hashtags for hashtags in google_post.hashtags)

def test_from_shortcode(google_post):
    result_post: Post = Post.from_shortcode(shortcode=google_post.data_points[0].shortcode)
    result_post.static_load()

    assert result_post.url == google_post.url
    assert result_post.data_points[0].caption == google_post.data_points[0].caption
