""" Правила для email:
email адрес содержит 1 разделитель @, отделяющий имя от доменной части, 
причем обе части не должны быть пустыми.
Ограничения на длину:
1) общая длина адреса < 256 символов
2) длина имени < 64 символа
3) длина домена < 254 символа
Ограничения на используемые символы:
Для имени допускаются заглавные и строчные латинские буквы,
цифры от 0 до 9 и спец символы: ".", "-", "_", но эти символы не могут
стоять в начале и в конце имени. Доменное имя разделяется '.'
при этом каждая часть доменного имени не должна быть пустой.
Доменное имя должно кончаться на одно и стандартных доменных имен:
ru, su, org, com, и так далее. Части доменного имени не могут 
начинаться и заканчиватсья на спец символы: ".", "-"
"""

def check_len(string, bound, operation='<'):
    if operation == '<':
        if len(string) < bound:
            return True
        else:
            return False
    elif operation == '>':
        if len(string) > bound:
            return True
        else:
            return False
    elif operation == '=':
        if len(string) == bound:
            return True
        else:
            return False

    assert operation != '>'
    assert operation != '<'
    assert operation != '='

def correct_email(mail_address):
    
    spec_symbols = ['.','-','_']

    if mail_address.find('@') == -1:
        return False
    if not check_len(mail_address,256):
        return False
    
    name, domain = mail_address.split('@')
    
    if check_len(name,0,'=') or check_len(domain,0,'='):
        return False
    if not check_len(name,254) or not check_len(domain,64):
        return False
    if name[0] in spec_symbols or domain[-1] in spec_symbols or name[-1] in spec_symbols or domain[0] in spec_symbols:
        return False

    # Work with domain
    if domain.find('.') == -1:
        return False
    for domain_part in domain.split('.'):
        if check_len(domain_part,0,'='):
            return False
        if domain_part[0] == '-' or domain_part[-1] == '-':
            return False
        for letter in domain_part:
            if 'Z'>=letter>='A' or 'z'>=letter>='a':
                continue
            elif '9'>=letter>='0' or letter == '-' or letter == '_':
                continue
            else:
                return False
        
    spec_ending = ['ru', 'su', 'com', 'org']

    ending = domain.split('.')[-1]
    if not ending in spec_ending:
        return False
    
    # Work with name
    for letter in name:
        if 'Z'>=letter>='A' or 'z'>=letter>='a':
            continue
        elif '9'>=letter>='0' or letter in spec_symbols:
            continue
        else:
            return False

    return True

if __name__ == "__main__":
    result = correct_email(input("Enter email address to chech it: "))
    if result:
        print(f'Everything is clear.')
    else:
        print(f'Wrong email address.')