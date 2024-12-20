from src.decorators import log, my_function
def test_log(capsys):
    # @log(filename=None)
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ок\n"