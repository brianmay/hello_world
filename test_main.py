import pytest
import main


class FakeInputer():
    def read_input(self) -> main.Message:
        return main.TextMessage("input")


class FakeOutputer():
    def write_output(self, message: main.Message) -> None:
        assert str(message) == "input"


def test_xml_inputer() -> None:
    inputer = main.XmlInputer("<p>Hello World</p>")
    assert str(inputer.read_input()) == "Hello World"


def test_xml_inputer_invalid() -> None:
    inputer = main.XmlInputer("<div>Hello World</div>")

    with pytest.raises(RuntimeError):
        assert inputer.read_input()


def test_main() -> None:
    inputer = FakeInputer()
    outputer = FakeOutputer()
    main.do_work(inputer, outputer)
