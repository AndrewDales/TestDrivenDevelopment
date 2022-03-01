from main import square_it, Car
import pytest

test_data = [(5, 25), (-2, 4), (0, 0), (0.1, 0.01)]


@pytest.mark.parametrize("value, result", test_data)
def test_square_it(value, result):
    assert square_it(value) == pytest.approx(result)


class TestCar:
    @pytest.fixture()
    def my_car(self):
        return Car(50)

    def test_accelerate(self, my_car):
        my_car.accelerate()
        assert my_car.speed == 55

    def test_brake(self, my_car):
        my_car.brake()
        assert my_car.speed == 45

    def test_average_speed(self, my_car):
        my_car.accelerate()
        my_car.step()
        my_car.accelerate()
        my_car.step()
        my_car.brake()
        my_car.step()
        assert my_car.average_speed() == (55 + 60 + 55) / 3

    def test_zero_time_exception(self, my_car):
        my_car.time = 0
        with pytest.raises(ZeroDivisionError):
            my_car.average_speed()
