from cx_Freeze import setup, Executable

setup(
	name = "Naruto 2D",
	version = "0.1",
	description = "First",
	executables = [Executable("Uzumaki Adventures.py",
                                  icon="Data/Effects/narutoS.ico",
                                  base ="Win32GUI",
                                  )
                       ]
      )
