from cx_Freeze import setup, Executable

setup(
    name = "Game of Berserk" ,
    version = "0.1" ,
    description = "Incarne le personnage de guts qui lutte dans contre les fantômes des enfers." ,
    executables = [Executables("Game of Berserk.py")]
)