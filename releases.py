import requests


def get_release_info(username, password, base_url, project_id):
    project_url = f'{base_url}/Services/v5_0/RestService.svc/projects/{project_id}/releases'

    try:
        response = requests.get(project_url, auth=(username, password))
        if response.status_code == 200:
            releases = response.json()  # payload of all details on the various releases in the project
            for release in releases:
                release_details = f"Release ID: {release['ReleaseId']}, Name: {release['Name']}\n"
                print(release_details)

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to SpiraPlan: {e}")


if __name__ == "__main__":
    get_release_info(username, password, base_url, project_id)
