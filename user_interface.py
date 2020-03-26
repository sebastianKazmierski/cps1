import time
import curses

from draw_plot import display
from file_manager import write, read
from signal import Signal
from signal_generators2.impulse_noise import ImpulseNoise
from signal_generators2.noise_gaus_distribution import GausDistribution
from signal_generators2.noise_uniform_distribution import UniformDistribution
from signal_generators2.rectagular_simetric_signal import RectangularSymetricSignal
from signal_generators2.rectangular_signal import RectangularSignal
from signal_generators2.sin import SinGenerator
from signal_generators2.sin_straightened_in_one_half import SinStraightenedInOneHalf
from signal_generators2.sin_straightened_in_two_half import SinStraightenedInTwoHalf
from signal_generators2.traiangul_signal import TriangularSignal
from signal_generators2.unit_impuls import UnitImpuls
from signal_generators2.unit_jump import UnitJump
from signal_operation import SignalOperation
from signal_parameters import SignalParameters


def get_parameter(parameter: SignalParameters):
    print(parameter.name + ": ")
    return float(input())


def show_statistics(read_signal: Signal):
    print("Wartość średnia:                                        " + str(read_signal.average_signal_value()))
    print("Wartość średnia bezwzględna:                            " + str(read_signal.absolute_average_signal_value()))
    print("Moc średnia:                                            " + str(read_signal.average_power_of_signal()))
    print("Wariancja sygnału w przedziale wokół wartości średniej: " + str(read_signal.signal_variance()))
    print("Wartość skuteczna:                                      " + str(read_signal.effective_value()))


def load_signal_from_file():
    print("Podaj nazwę pliku:")
    file_name = input()
    return read(file_name)


def generete_signal():
    global signal
    list = [ImpulseNoise(), GausDistribution(), UniformDistribution(), RectangularSymetricSignal(),
            RectangularSignal(), SinGenerator(), SinStraightenedInOneHalf(), SinStraightenedInTwoHalf(),
            TriangularSignal(), UnitImpuls(), UnitJump()]
    print("Wybierz funkcje: ")
    for i in range(len(list)):
        print(str(i) + " " + list[i].get_name())
    index = int(input())
    signal_generator = list[index]
    print(list[index].get_name())
    required_parameters = []
    for parameter in signal_generator.get_list_required_parameters():
        required_parameters.append(get_parameter(parameter))
    return signal_generator.generate(*required_parameters)


def present_signal():
    global signal, answer
    signal = generete_signal()
    show_statistics(signal)
    display(signal)
    print("Czy chcesz zapisac sygnał do pliku? (t/N)")
    answer = input()
    if answer == "t" or answer == "T":
        print("Podaj nazwę pliku:")
        file_name = input()
        write(signal, file_name)


present_signal()


def get_one_element_of_operation():
    global answer
    print("1. Wczytaj sygnał z pliku")
    print("2. Wygeneruj nowy sygnał")
    answer = int(input())
    if answer == 1:
        return load_signal_from_file()
    else:
        return generete_signal()


def get_elements_of_operation():
    print("Wybierz pierwszy składnik operacji")
    element1 = get_one_element_of_operation()
    print("Wybierz drugi składnik operacji")
    element2 = get_one_element_of_operation()
    return element1, element2


def perform_operation():
    global answer, signal_operation
    print("Wybierz rodzaj operacji")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    answer = int(input())
    signal1, signal2 = get_elements_of_operation()
    signal_operation = SignalOperation()
    if answer == 1:
        result = signal_operation.add(signal1, signal2)
    elif answer == 2:
        result = signal_operation.subtract(signal1, signal2)
    elif answer == 3:
        result = signal_operation.multiply(signal1, signal2)
    elif answer == 4:
        result = signal_operation.division(signal1, signal2)
    present_signal(result)


perform_operation()








