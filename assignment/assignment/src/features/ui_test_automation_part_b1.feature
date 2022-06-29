@ui_cloudmore_test
Feature: UI: landing page for cloudmore
  description
  This feature file contain test related to Part B.1 (UI test automation, Python)

@TC-1 @ui
Scenario: UI- Verify cloudmore landing page with different icons

When user has navigated to the cloudmore landing page
Then user can verify the "CLOUDMORE_COMPANY_LOGO" on landing page
And user can verify the "PLATFORM_LOGO" on landing page
And user can verify the "SOLUTION_LOGO" on landing page
And user can verify the "ABOUT_US_LOGO" on landing page
And user can verify the "CONTACT_US_LOGO" on landing page
And user can verify the "CASE_STUDIES_LOGO" on landing page

When user clicks the "PLATFORM_LOGO" on landing page
Then user can verify the "SOLUTION_LOGO" on landing page
And user can verify the "ABOUT_US_LOGO" on landing page
And user can verify the "CONTACT_US_LOGO" on landing page
And user can verify the "CASE_STUDIES_LOGO" on landing page


When user clicks the "SOLUTION_LOGO" on landing page
Then user can verify the "PLATFORM_LOGO" on landing page
And user can verify the "ABOUT_US_LOGO" on landing page
And user can verify the "CONTACT_US_LOGO" on landing page
And user can verify the "CASE_STUDIES_LOGO" on landing page

When user clicks the "ABOUT_US_LOGO" on landing page
Then user can verify the "PLATFORM_LOGO" on landing page
Then user can verify the "SOLUTION_LOGO" on landing page
And user can verify the "CONTACT_US_LOGO" on landing page
And user can verify the "CASE_STUDIES_LOGO" on landing page

When user clicks the "CONTACT_US_LOGO" on landing page
Then user can verify the "PLATFORM_LOGO" on landing page
And user can verify the "SOLUTION_LOGO" on landing page
And user can verify the "ABOUT_US_LOGO" on landing page
And user can verify the "CASE_STUDIES_LOGO" on landing page

When user clicks the "CASE_STUDIES_LOGO" on landing page
Then user can verify the "PLATFORM_LOGO" on landing page
And user can verify the "SOLUTION_LOGO" on landing page
And user can verify the "ABOUT_US_LOGO" on landing page
And user can verify the "CONTACT_US_LOGO" on landing page


@TC-2 @ui
Scenario: UI- Verify Search by keyword “Högset” works

When user has navigated to the cloudmore landing page
When user clicks the "ACCEPT_LINK_BUTTON" on landing page

When user finds the "SEARCH_BOX" on cloudmore landing page and then click it
Then user can find the main "SEARCH_BOX_PLACEHOLDER" and can search using keyword "Högset"
Then verify that navigation happened to search result page
Then verify that user can capture screenshot and search results has less than 3 pages, screenshot should be taken from latest result page and in case if search results has more that 3 pages than take screenshot from 3rd page

