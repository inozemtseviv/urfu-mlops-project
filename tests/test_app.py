from streamlit.testing.v1 import AppTest


def test_app_front():
    at = AppTest.from_file("app.py")
    at.run()

    assert at.title[0].value == 'Определение качества красного вина по его параметрам'
    assert at.title[1].value == 'Параметры'
    assert at.slider[0].label == 'fixed acidity'
    assert at.slider[1].label == 'volatile acidity'
    assert at.slider[2].label == 'citric acid'
    assert at.slider[3].label == 'residual sugar'
    assert at.slider[4].label == 'chlorides'
    assert at.slider[5].label == 'free sulfur dioxide'
    assert at.slider[6].label == 'total sulfur dioxide'
    assert at.slider[7].label == 'density'
    assert at.slider[8].label == 'pH'
    assert at.slider[9].label == 'sulphates'
    assert at.slider[10].label == 'alcohol'
