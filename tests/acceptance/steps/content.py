from behave import *

from tests.acceptance.locators.base_page import BasePageLocators
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@then('There is a title shown on a page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


@step('The title has content "(.*)"')
def step_impl(context, content):
    title = BasePage(context.driver).title
    assert title.text == content


@then('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    tag = page.title
    assert tag.text == content


@then('I can see the posts section on a page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()


@then('I can see a post with title "(.*)" in the posts section')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]
    assert len(posts_with_title) > 0
    assert all([post.is_displayed for post in posts_with_title])

