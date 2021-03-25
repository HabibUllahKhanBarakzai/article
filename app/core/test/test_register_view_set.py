from django.test import TestCase


class RegisterTestCase(TestCase):
    """This test case will test the register api"""

    @property
    def _payload(self):
        return {
            "first_name": "john",
            "last_name": "doe",
            "email": "habib1@gmail.com",
            "password": "123456"
        }

    @property
    def _failing_payload(self):
        return {"no_password": {"email": "habib1@gmail.com"},
                "wrong_email": {"email": "sdasd", "password": "21212"}}

    def setUp(self) -> None:
        self.url = "/api/v1/register/writer/"

    def test_register_view_set(self):
        response = self.client.post(self.url, self._payload, content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_register_failing_payload(self):
        response = self.client.post(
            self.url,
            self._failing_payload["no_password"],
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)

        response = self.client.post(
            self.url,
            self._payload["wrong_email"],
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
