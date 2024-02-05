from flet import *
import time

def forgot_password():
    pass

def navigate_sign_up():
    pass

def main(page: Page):

    #page settings:
    
    page.title = "Sponsurf - Login"

    #geometry
    page.window_top = 150
    page.window_left = 300
    page.window_height = 600
    page.window_width = 1000
    
    page.bgcolor = "#000000"
    page.padding = 0
    page.window_maximizable = False
    page.window_minimizable = False
    page.window_resizable = False

    
    
    sponsurf_logo_img = Image(
        src = r"images\sponsurf_logo_img.png",
        width = 300,
        height = 300,
        border_radius = 10
        )
    
    welcome_column = Column(
        [Text(
            "Welcome",
            size = 36,
            color = '#ffffff',
            style = TextStyle(weight=FontWeight.BOLD)
            ),
        sponsurf_logo_img,
        Text("")
        ],

        alignment = MainAxisAlignment.SPACE_EVENLY,
        horizontal_alignment = "CENTER",
        spacing = 20
        )
        
    bgc1 = Container(
        content = welcome_column,
        bgcolor = colors.BLACK,
        margin = 0,
        padding = 0,
        width = page.window_width*0.2,
        height = page.window_height,
    )

    bgc2 = Container(
        content = Text(""),
        bgcolor = '#058999',
        margin = 0,
        padding = 0,
        width = page.window_width*0.02,
        height = page.window_height,
    )

    user_icon_img = Image(
        src = r"images\user_icon_img.png",
        width = 120,
        height = 120,
        border_radius = 10
        )

    email_login_textfield = TextField(
        label = "📧 Email",
        width = 300,
        height = 41.35,
        bgcolor = '#b5f7ff',
        text_size = 14,
        border_radius = 7
        )

    password_login_textfield = TextField(
        label = "🔑 Password",
        width = 300,
        height = 41.35,
        bgcolor = '#b5f7ff',
        text_size = 14,
        border_radius = 7,
        password=True,
        can_reveal_password=True
        )

    login_btn = ElevatedButton(
        text="Login",
        width = 300,
        height = 41.35,
        bgcolor = '#3467c0',
        color = '#ffffff',
        style = ButtonStyle(shape = RoundedRectangleBorder(radius=5))
        )

    forgot_password_btn = Container(
        content = Text("Forgot your password?",
                       size = 14,
                       color = '#0563c1',
                       style = TextStyle(decoration=TextDecoration.UNDERLINE)
                       ),
        bgcolor = '#6befff',
        on_click = forgot_password
        )

    sign_up_btn = Container(
        content = Text("Don’t have an account? Sign up",
                       size = 14,
                       color = '#0563c1',
                       style = TextStyle(decoration=TextDecoration.UNDERLINE)
                       ),
        bgcolor = '#6befff',
        on_click = navigate_sign_up
        )
        

        
    login_column = Column(
        [user_icon_img,
         email_login_textfield,
         password_login_textfield,
         login_btn,
         forgot_password_btn,
         sign_up_btn
         ],
        
        alignment = "CENTER",
        horizontal_alignment = "CENTER",
        spacing = 20
        )
    
    bgc3 = Container(
        content = login_column,
        bgcolor = "#6befff",
        margin = 0,
        padding = 0,
        width = page.window_width*0.78,
        height = page.window_height,
    )

    bgc3.alignment = alignment.Alignment(0, -0.5)

    row = Row(spacing=0, controls=[bgc1,bgc2,bgc3])
    page.add(row)
    
app(target=main)
