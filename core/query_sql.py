import pyodbc
from decouple import config

def conexao(NIF_FORMULARIO):
    SERVER_NAME = 'MPGPTSQL11\\MPGNAVPROD'
    DATABASE_NAME = 'mpg_Gest_Logins'
    USERNAME = 'GestLoginsApp'
    PASSWORDDB = '{DW+o4.wkdVd9_M#gmf-E}'

    SERVER_NAME_ = config('_SERVER_NAME', default="")
    DATABASE_NAME_ = config('_DATABASE_NAME', default="")
    USERNAME_ = config('_USERNAME', default="")
    PASSWORDDB_ = config('_PASSWORDDB', default="")

    conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                          f'Server={SERVER_NAME};Database={DATABASE_NAME};'
                          f'UID={USERNAME};PWD={PASSWORDDB}')


    print("Conexão Bem Sucedida")
    cursor = conn.cursor()
    #N = input("Insira o NIF para validação: ")
    cursor.execute("SELECT  Nome, %s , OPERATION, Contract_N , Active FROM [mpg_Gest_Logins].[dbo].[Vw_M2] where Active= 1 " % (NIF_FORMULARIO))
    resultado = cursor.fetchall()
    #if N in resultado:
    print(F' NOME                            NIF           POJECT     N_CONTRATO  ATIVO ')
    print(resultado)

    #else:
        #print('Contrato Não encontrado')




    ''' SELECT[CodEmp]
    , [Emp]
    , [Active_Today]
    , [Active]
    , [Training]
    , [Canceled]
    , [In_Termination]
    , [Privacy_Blocked]
    , [Right_to_forget]
    , [N]
    , [Contract_N]
    , [Start_Date]
    , [Senior_Date]
    , [Expected_End_Date]
    , [Suspension_Start]
    , [Suspension_End]
    , [Nome]
    , [Telefone]
    , [Telemovel]
    , [EMAIL]
    , [Sexo]
    , [Term_Contract_Type]
    , [Contract_Type]
    , [BUSINESS_LINE_LOC]
    , [STRUCTURE]
    , [OPERATION]
    , [Cod Cliente]
    , [Cliente]
    , [CONSULTANT]
    , [Chf_Emp]
    , [Chf_Tlmv]
    , [Chf_Email]
    , [Chf_Name]


    FROM[dbo].[Vw_M2]'''

    return resultado



