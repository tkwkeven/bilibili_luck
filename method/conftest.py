# -*- codeing = utf-8 -*-
# @File:conftest.py
# @Software:PyCharm
# @Author:keven
# @Time:2023/5/30 17:39
import pytest

success = {}

@pytest.fixture
def set_success():
    def _set_success(di,su):
        success[di] = su
    return _set_success()

@pytest.fixture()
def get_success():
    def _get_success(di):
        return success.get("di")
    return _get_success()