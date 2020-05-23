AVAILABLE_COLORS = {
    'red': '0xFF0000',
    'green': '0x00FF00',
    'blue': '0x0000FF',
    'yellow': '0xFFFF00',
    'aqua': '0x00FFFF',
    'fuchsia': '0xFF00FF',
    'black': '0x000000',
    'white': '0xFFFFFF'
}


def moon_landing_date():
    print('Moon landing took place in: Jun 16th 1969 at 7:32 a.m. GTM-6')


def greetings(name):
    print('Good morning ' + name)


def custom_greeting(greeting, name):
    print(greeting + ' ' + name)


def multiple_greeting(greeting, *names):
    str_builder = ''

    for name in names:
        str_builder += name + ', '

    print(greeting + ' ' + str_builder)


def persona_info(name, age, email, alias, height):
    print(name + ' details:')
    print('\tage: ' + str(age))
    print('email: ' + email)
    print('alias: ' + alias)
    print('height ' + str(height))


def persona_info_2(name, age, email, alias=None, height=None):
    print(name + ' details:')
    print('\tage: ' + str(age))
    print('email: ' + email)
    print('alias: ' + alias)
    print('height ' + str(height))


def retrieve_hex_color(color_name):
    color_code = AVAILABLE_COLORS[color_name]
    return color_code


def get_formatted_color_code(color_name):
    formatted_str = f'{color_name} == '
    color_code = retrieve_hex_color(color_name)

    return formatted_str + color_code


if __name__ == '__main__':
    # moon_landing_date()
    # greetings('Eduardo')
    # custom_greeting('Hi', 'Eduardo')
    # custom_greeting('Hi', 'Eduardo')
    # multiple_greeting('Hello', 'Eduardo', 'Serch', 'Andrea')
    # persona_info('Eduardo', 29, 'example@mail.com', 'Cope', 1.74)
    # persona_info_2('Eduardo', 29, 'example@mail.com',)
    print(retrieve_hex_color('red'))
    print(get_formatted_color_code('red'))
