def tituloBienvenida():
  class color:
      GREEN = '\033[32m'     
      YELLOW = '\033[33m'    
      WHITE = '\033[37m'     
      BOLD = '\033[1m'       
      END = '\033[0m'        
  title = f"""
{color.BOLD}{color.GREEN}******************************{color.END}
{color.BOLD}*{color.YELLOW} BIENVENIDO A CENTRO MÉDICO{color.END} {color.BOLD}*
{color.BOLD}*     CARLOS ARDILA LULLE   {color.END} {color.BOLD}*
{color.BOLD}{color.GREEN}******************************{color.END}
    """
  print(title)

def tituloPacientes():
    class color:
        GREEN = '\033[32m'     
        YELLOW = '\033[33m'    
        WHITE = '\033[37m'     
        BOLD = '\033[1m'       
        END = '\033[0m'        
    title = f"""
{color.BOLD}{color.GREEN}******************************{color.END}
{color.BOLD}*{color.YELLOW}   PACIENTES CENTRO MÉDICO  {color.END}{color.BOLD}*
{color.BOLD}*     CARLOS ARDILA LULLE   {color.END} {color.BOLD}*
{color.BOLD}{color.GREEN}******************************{color.END}
    """
    print(title)

def tituloEspecialistas():
    class color:
        GREEN = '\033[32m'     
        YELLOW = '\033[33m'    
        WHITE = '\033[37m'     
        BOLD = '\033[1m' 
        END = '\033[0m'        
    title = f"""
{color.BOLD}{color.GREEN}******************************{color.END}
{color.BOLD}*{color.YELLOW}        ESPECIALISTAS       {color.END}*
{color.BOLD}*        {color.WHITE}CENTRO MÉDICO       {color.BOLD}*
{color.BOLD}*{color.YELLOW}     CARLOS ARDILA LULLE    {color.END}{color.BOLD}*
{color.BOLD}{color.GREEN}******************************{color.END}
    """
    print(title)