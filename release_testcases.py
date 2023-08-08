import requests, os


def get_testcase_name(project_id, testcase_id, username, password, base_url):
    url = f"{base_url}/Services/v5_0/RestService.svc/projects/{project_id}/test-cases/{testcase_id}"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        test_case = response.json()
        return test_case['Name']


def get_release_testcases(project_id, release_id, username, password, base_url):
    url = f"{base_url}/Services/v5_0/RestService.svc/projects/{project_id}" \
          f"/releases/{release_id}/test-cases"
    response2 = requests.get(url, auth=(username, password))
    if response2.status_code == 200:
        test_cases = response2.json()
        for test_case in test_cases:
            name = get_testcase_name(project_id, test_case['TestCaseId'], username, password, base_url)
            print(f"Testcase ID: {test_case['TestCaseId']}, Name : {name}")


if __name__ == "__main__":
    print(get_release_testcases(project_id, release_id, os.environ.get('SPIRAPLAN_USERNAME'),
                                os.environ.get('SPIRAPLAN_KEY'),
                                base_url))

