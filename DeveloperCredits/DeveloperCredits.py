import inspect #CHECK DATACODE
import Function #LOCATE TARGET_CODE "__MODULE__"

#CONTAR FUNCIONES Y RETORNAR NUMERO
def count_functions(module):

    function_list = inspect.getmembers(module, inspect.isfunction)
    number = len(function_list)
    number /= 10
    return str(number)

#FUNCION IMPRIMIR CREDITOS AL PROGRAMADOR
def printCodeMaster(defNumber):

    #PROJECT-DATA
    proyectName = "DeveloperCredits"
    developer = "MAURO PEPA"
    proyectVersion = "1"

    developerCretis = "\n"+proyectName+ " - BY "+developer+" - V"+proyectVersion+"."+defNumber
    print(developerCretis)

    LongNumberStick = "-"*len(developerCretis)
    print(LongNumberStick+"\n")

def printCredits():

    printCodeMaster(count_functions(Function))

if __name__ == '__main__':
    printCredits()