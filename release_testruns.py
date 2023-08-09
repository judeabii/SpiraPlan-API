import requests
import os


def get_release_testruns(release_id, testcase_id, project_id, username, password, base_url):
    url = f"{base_url}/Services/v5_0/RestService.svc/projects/{project_id}" \
          f"/test-cases/{testcase_id}/test-runs/search?starting_row=1&" \
          f"number_of_rows=10&sort_field=Release" \
          f"sort_direction=asc"
    try:
        response = requests.post(url, auth=(username, password))
        if response.status_code == 200:
            test_runs = response.json()
            print(f"Testcase -> {testcase_id}: ")
            for test_run in test_runs:
                exec_status = ""
                if test_run['ReleaseId'] == release_id:
                    if test_run['ExecutionStatusId'] == 2:
                        exec_status = "Passed"
                    if test_run['ExecutionStatusId'] == 1:
                        exec_status = "Failed"
                    print(f"Testrun Name: {test_run['Name']}, Testrun ID: {test_run['TestRunId']}, "
                          f"Execution Status: {exec_status}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to SpiraPlan: {e}")


if __name__ == "__main__":
    get_release_testruns(release_id, testcase_id, project_id, os.environ.get('SPIRAPLAN_USERNAME'),
                         os.environ.get('SPIRAPLAN_KEY'), base_url)
