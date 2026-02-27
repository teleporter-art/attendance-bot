import requests

LOGIN_URL = "https://itsapi.aperptech.com/api/login"
ATTENDANCE_URL = "https://itsapi.aperptech.com/api/my/final/attendances"

EMAIL = "mohdfarooquemf_ds25@its.edu.in"
PASSWORD = "farhan@1"


def get_attendance():
    session = requests.Session()

    login_payload = {
        "userType": 1,
        "email": EMAIL,
        "password": PASSWORD,
        "deviceType": "web"
    }

    login_res = session.post(LOGIN_URL, json=login_payload)
    token = login_res.json()["token"]

    headers = {"Authorization": f"Bearer {token}"}

    att_res = session.get(ATTENDANCE_URL, headers=headers)
    subjects = att_res.json()["data"]

    overall = next(s for s in subjects if s.get("subjectCode") == "ALL SUBJECTS")

    return overall["subjectTotalPercentage"]


if __name__ == "__main__":
    p = get_attendance()
    print("Attendance %:", p)