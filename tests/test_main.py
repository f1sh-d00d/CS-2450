from main import *
import pytest

def test_multiply():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and gets multiplied by the 1st item in memory which is 0002 to form 0004 in the Acc.
    VM._memory = ["0000", "0002", "3301", "0000", "4300"]
    VM._accumulator = "0002"
    VM.run()
    assert(VM.get_accumulator() == "0004")

    #Sets Acc. to 9999 and gets multiplied by the 0th item in memort to throw a ValueError (Value Overflow as Acc. == 10,088,991)
    VM._memory = ["9999", "0000", "3300", "0000", "4300"]
    VM._accumulator = "9999"
    with pytest.raises(ValueError):
        VM.run()

    # Attempts to multiply the 99th element but throws a IndexError (Memory Address 99 out of range)
    VM._memory = ["0000", "0000", "3399", "4300"]
    VM._accumulator = "9999"
    with pytest.raises(IndexError):
        VM.run()

def test_divide():
    VM = VirtualMachine()

    # Sets Acc. to 0002 and divdes Acc. by the 1st element which is 0050, leaving 0025 in the Acc.
    VM._memory = ["0000", "0050", "3201", "4300"]
    VM._accumulator = "0002"
    VM.run()
    assert(VM.get_accumulator() == "0025")

    # Attempts to use the 99th element but throws a Index Error.
    VM._memory = ["0000", "0000", "3299", "4300"]
    VM._accumulator = "0002"
    with pytest.raises(IndexError):
        VM.run()

def test_branch():
    VM = VirtualMachine()

    # Branches to the 4th item in memory to divide 16 // 2, then halts 
    VM._memory = ["0000", "0016", "4004", "4300", "3201", "4300"]
    VM._accumulator = "0002"
    VM.run()
    assert(VM._accumulator == "0008")