import pytest
import requests

class TestPETEndpoint:
    @classmethod
    def setup_class(cls):
        cls.scheme = "https://"
        cls.host = "petstore.swagger.io"
        cls.basepath = "/v2"
        cls.pet_endpoint = "/pet"
        cls.header = {'accept': 'application/json'}
        cls.base_url = "{0}{1}{2}{3}".format(cls.scheme, cls.host,
                                             cls.basepath, cls.pet_endpoint)

    @classmethod
    def teardown_class(cls):
        pass

    def get_request(self, endpoint_path, query_param=""):
        url = "{0}{1}{2}".format(self.base_url, endpoint_path, query_param)
        req = requests.get(url, headers=self.header)
        return req

    @pytest.mark.skip(reason="backlog")
    def test_upload_img(self):
        pass

    @pytest.mark.skip(reason="backlog")
    def test_add_a_new_pet(self):
        pass

    @pytest.mark.skip(reason="backlog")
    def test_update_existing_pet(self):
        pass

    """
    Parameterized tests for the endpoints for:
    1. Find pets by status
    2. Find pet by ID
    """
    @pytest.mark.parametrize(
        "endpoint_path, param, expected_resp_code",
        [
            pytest.param(
                "/findByStatus", "?status=available", 200, id="find_pets_by_status-GET-available-200"
            ),
            pytest.param(
                "/findByStatus", "?status=pending", 200, id="find_pets_by_status-GET-pending-200"
            ),
            pytest.param(
                "/findByStatus", "?status=sold", 200, id="find_pets_by_status-GET-sold-200"
            ),
            pytest.param(
                "/findByStatus", "?status=available,pending", 200, id="find_pets_by_status-GET-available,pending-200"
            ),
            pytest.param(
                "/findByStatus", "?status=available,pending,sold", 200, id="find_pets_by_status-GET-available,pending,sold-200"
            ),
            pytest.param(
                "/findByStatus", "?status=invalidstatus", 400, id="find_pets_by_status-GET-invalidstatus-400"
            ),
            pytest.param(
                "/1804", "", 200, id="find_pet_by_id-GET-Pet_ID_exists-200"
            ),
            pytest.param(
                "/abcde12345", "", 400, id="find_pet_by_id-GET-Invalid_ID-400"
            ),
            pytest.param(
                "/999999999", "", 404, id="find_pet_by_id-GET-Pet_not_found-404"
            )
        ],
    )
    def test_find_pets(self, endpoint_path, param, expected_resp_code):
        resp = self.get_request(endpoint_path, param)
        assert resp.status_code == expected_resp_code

    @pytest.mark.skip(reason="backlog")
    def test_updates_a_pet(self):
        pass

    @pytest.mark.skip(reason="backlog")
    def test_deletes_a_pet(self):
        pass

if __name__ == "__main__":
    pytest.main()