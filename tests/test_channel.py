import pytest
from src.channel import Channel


#@pytest.fixture()
def test_init():
    channel = Channel('UC-lHJZR3Gqxm24_Vd_AJ5Yw')
    assert channel.channel_id == 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'

def test_print_info():
    channel = Channel('UC-lHJZR3Gqxm24_Vd_AJ5Yw')
    channel.print_info()
    assert channel.channel_id == 'UC-lHJZR3Gqxm24_Vd_AJ5Yw'
