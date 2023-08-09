# SpiraPlan-API
A project outlining how we can get any required information quickly from SpiraPlan through the use of APIs.

1. Get all release information from a particular project. This
    includes details such as Release ID and Release Name.
   - `releases.py`
2. Get information on all the testcases part of a particular release. Information retrieved includes testcase name and testcase ID
   - `release_testcases.py`
3. View details of all the Test runs associated with a given testcase in a release.
   - `release_testruns.py`

We can import all these individual files in a main py file and make use of all these separate programs.

With API, we can get different types of reports/information and tweak them accordingly.
The ones here are the most basic information that will help any test management project.

View the SpiraPlan API documentation here: [SpiraPlan API](https://api.inflectra.com/spira/services/v5_0/RestService.aspx)