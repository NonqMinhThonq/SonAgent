import logging
import pytest
from test_module import gc_set_threshold, gc_setup

def test_gc_set_threshold_debug_called(gc_setup, mocker):
    logger_debug_mock = mocker.patch.object(logging.Logger, 'debug')
    
    # Gọi hàm cần kiểm tra
    gc_set_threshold()

    # Kiểm tra xem logger.debug đã được gọi chưa
    logger_debug_mock.assert_called_once_with("Adjusting python allocations to reduce GC runs")

def test_gc_set_threshold_set_threshold_called(gc_setup, mocker):
    set_threshold_mock = mocker.patch('gc.set_threshold')

    # Gọi hàm cần kiểm tra
    gc_set_threshold()

    # Kiểm tra xem gc.set_threshold đã được gọi chưa với đúng các tham số
    set_threshold_mock.assert_called_once_with(50_000, 500, 1000)


