from name_function import get_formatted_name

#函数名必须以test_打头，这样该函数才会在执行pytest命令时自动运行
def test_first_last_name():
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    formatted_name = get_formatted_name('alice','pure','lily') 
    assert formatted_name == 'Alice Lily Pure'