Feature: Test that pages have the correct content
  Scenario: Blog page has the correct title
    Given I am on the blog page
    Then There is a title shown on a page
    And The title has content "This is the blog page"

  Scenario: Homepage has the correct title
    Given I am on the homepage
    Then There is a title shown on a page
    And The title has content "This is the homepage"

  Scenario: Blog page loads the posts
    Given I am on the blog page
    And I wait for the posts to load
    Then I can see the posts section on a page

  Scenario: User can create new posts
    Given I am on the new post page
    When I enter "Test post" in the "title" field
    And I enter "Test content" in the "content" field
    And I press the submit button
    Then I am on the blog page
    Given I wait for the posts to load
    Then I can see a post with title "Test post" in the posts section

