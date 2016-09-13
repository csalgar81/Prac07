from programminglanguage import ProgrammingLanguage
#
def main():
    java = ProgrammingLanguage('Java', 'Static', True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage('Ruby','Dynamic', True,1995)
    print(java)

    languages =[[java.name,java.typing,java.reflection,java.year]]
    languages.append([python.name,python.typing,python.reflection,python.year])
    languages.append([vb.name, vb.typing, vb.reflection, vb.year])
    languages.append([ruby.name, ruby.typing, ruby.reflection, ruby.year])
    print(languages)

    print("The dynamically typed languages are:")
    for language in languages:
        if language[1] =="Dynamic":
            print(language[0])

main()