from adafruit_pybadger import PyBadger

pybadger = PyBadger()

pybadger.auto_dim_display(delay=10, movement_threshold=20)

first_display = True

while True:
    if pybadger.button.a:
        pybadger.show_business_card(image_name="supercon.bmp",
                                    name_string="gmackie", name_scale=1,
                                    email_string_one="me@gmac.io",
                                    email_string_two="https://gmac.io/")
    elif pybadger.button.b:
        pybadger.show_qr_code(data="https://wobscale.website")
    elif pybadger.button.start or first_display:
        pybadger.show_badge(name_string="gmackie", hello_scale=2, my_name_is_scale=2, name_scale=2)
        first_display = False
