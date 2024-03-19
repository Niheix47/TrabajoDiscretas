import flet as ft
import Model



def main(page: ft.Page):
    page.window_width = 1000       
    page.window_height = 500
    page.padding=15

    def btn_click(e):
        if not txt_number.value:
            page.route="/Binary"
            txt_number.error_text = "Please enter a number "
            page.update()
        else: 
            number = txt_number.value
            check = Model.isNumber(number)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                page.add(ft.Container(
                    ft.Row(
                        [
                            ft.Text(f"your number converted into binary is, {Model.transportB10toB2(int(number))}!", size=35,bgcolor=black,),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                alignment=ft.alignment.center_right,
                width=1000,
                height=250,
                bgcolor= "#f4ebd3",
                border_radius=100
                )
            )
                
    def btn_clickAnyToDec(e):
        if not txt_number.value:
            page.route="/Binary"
            txt_number.error_text = "Please enter a number "
            page.update()
        else: 
            number = txt_number.value
            check = Model.isNumber(number)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                page.add( ft.Container(ft.Row(
                [
                    ft.Text(f"Chose the System that you want to convert in",size=25),
                
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center_right,
                width=800,
                height=150,
                bgcolor= "#733380",
                border_radius=100,
            ),
                txt_Index,
                ft.Row(
                    [
                    ft.ElevatedButton("Get the result", on_click=btn_clickAnyToDecRes),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
                
    def btn_clickAnyToDecRes(e):
        if not txt_Index.value:
            txt_Index.error_text = "Please enter a number "
            page.update()
        else: 
            Index = txt_Index.value
            page.route = "/DivisorsIndex2"
            number = txt_number.value
            check = Model.isNumber(Index)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            elif number == 0 :
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                if number == 0 :
                    txt_number.error_text = "Please enter a valid number"
                    page.clean()
                    page.update()
                else:
                    res = Model.anyBaseTodecimal(int(number),int(Index))

                    page.add(ft.Container(
                        ft.Row(
                            [
                                ft.Text(f"The convertion from {Index} To Decimal is {res}),!",size=35,bgcolor=black),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    alignment=ft.alignment.center_right,
                    width=1000,
                    height=250,
                    bgcolor= "#e09ba6",
                    border_radius=100
                    )
                )
                
                


    def btn_clickDiv(e):
        if not txt_number.value:
            txt_number.error_text = "Please enter a number "
            page.update()
        else: 
            number = txt_number.value
            page.route = "/Divisors"
            check = Model.isNumber(number)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                divisors = Model.voidGetDiv(int(number),2,3)
                page.add(ft.Container(
                    ft.Row(
                        [
                            ft.Text(f"The divisors of your number are, {divisors}",size=35,bgcolor=black),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                alignment=ft.alignment.center_right,
                width=1000,
                height=250,
                bgcolor= "#856e4b",
                border_radius=100
                )
            )


    def btn_clickDivNo(e):
        if not txt_number.value:
            txt_number.error_text = "Please enter a number "
            page.update()
        else: 
            number = txt_number.value
            page.route = "/DivisorsNo"
            check = Model.isNumber(number)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                page.add(ft.Container(
                    ft.Row(
                        [
                            ft.Text(f"The number of divisors of your number are, {Model.voidGetDiv(int(number),2,1)}",size=35,bgcolor=black),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                alignment=ft.alignment.center_right,
                width=1000,
                height=250,
                bgcolor= "#008080",
                border_radius=100
                )
            )

    def btn_clickDivIndex(e):
        if not txt_number.value:
            txt_number.error_text = "Please enter a number "
            page.update()
        else: 
            number = txt_number.value
            page.route = "/DivisorsIndex"
            check = Model.isNumber(number)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                page.add(ft.Container(ft.Row(
                [
                    ft.Text(f"Chose the index of the divisor",size=25,bgcolor=black),
                
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center_right,
                width=800,
                height=150,
                bgcolor= "#a6d5d0",
                border_radius=100,
            ),
                txt_Index,
                ft.Row(
                    [
                     ft.ElevatedButton("Get the result", on_click=btn_clickDivIndex2),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )

    def btn_clickDivIndex2(e):
        if not txt_Index.value:
            txt_Index.error_text = "Please enter a number "
            page.update()
        else: 
            Index = txt_Index.value
            page.route = "/DivisorsIndex2"
            number = txt_number.value
            check = Model.isNumber(Index)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                page.add(ft.Container(
                    ft.Row(
                        [
                            ft.Text(f"The Divisor of index, {Index} ,For the number {txt_number.value} is  {Model.voidGetDiv(int(number),(int(Index)-1),2)}",size=35,bgcolor=black),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                alignment=ft.alignment.center_right,
                width=1000,
                height=250,
                bgcolor= "#522e31",
                border_radius=100
                )
            )
                
    def btn_clickMCDIndex2(e):
        if not txt_Index.value:
            txt_Index.error_text = "Please enter a number "
            page.update()
        else: 
            Index = txt_Index.value
            page.route = "/DivisorsIndex2"
            number = txt_number.value
            check = Model.isNumber(Index)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                page.add(ft.Container(
                    ft.Row(
                        [
                            ft.Text(f"The Maximum Divisor in common between {number} and {Index} is {Model.mcd(int(number),int(Index))}",size=35,bgcolor=black),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                alignment=ft.alignment.center_right,
                width=1000,
                height=250,
                bgcolor= "#522e31",
                border_radius=100
                )
            )

    
    def btn_clickReturn(e):
        page.clean()
        returnbt

    def btn_clickIsPrime(e):
        if not txt_number.value:
            txt_number.error_text = "Please enter a number "
            page.update()
        else: 
            number = txt_number.value
            page.route = "/Divisors"
            check = Model.isNumber(number)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                divisors = Model.voidFindPrimeNum(int(number))
                if divisors == True:
                    page.add(ft.Container(
                        ft.Row(
                            [
                                ft.Text(f"Your number is prime",size=35,bgcolor=black),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    alignment=ft.alignment.center_right,
                    width=1000,
                    height=250,
                    bgcolor= "#856e4b",
                    border_radius=100
                ),
            )
                else:
                    page.add(ft.Container(
                        ft.Row(
                            [
                                ft.Text(f"Your number isnt prime",size=35,bgcolor=black),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    alignment=ft.alignment.center_right,
                    width=1000,
                    height=250,
                    bgcolor= "#856e4b",
                    border_radius=100
                )
            )

    def btn_clickMcdIndex(e):
        if not txt_number.value:
            txt_number.error_text = "Please enter a number "
            page.update()
        else: 
            number = txt_number.value
            page.route = "/DivisorsIndex"
            check = Model.isNumber(number)
            if check == False:
                txt_number.error_text = "Please enter a valid number"
                page.update()
            else:
                page.clean()
                page.add(ft.Container(ft.Row(
                [
                    ft.Text(f"Chose the second number of the MCD",size=25,bgcolor=black),
                
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                alignment=ft.alignment.center_right,
                width=800,
                height=150,
                bgcolor= "#a6d5d0",
                border_radius=100,
            ),
                txt_Index,
                ft.Row(
                    [
                     ft.ElevatedButton("Get the result", on_click=btn_clickMCDIndex2),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        
    txt_number = ft.TextField(label="Your number",bgcolor="#02075d" ,border_color = ft.colors.TRANSPARENT,color=ft.colors.WHITE,)
    txt_Index = ft.TextField(label="Index")


    

    page.add(
        ft.Row(
            [
                txt_number
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            width = 2000,
        )
    )
    page.title = "Matematicas discrertas"
    blue = "#4334eb"
    red = "#eb3440"
    white = "#fcfcfc"
    black = "#000000"
    i =  0
    page.bgcolor="0799bf"
    returnbt = page.add(
        ft.Container(
            ft.Row(
                [
                    ft.ElevatedButton("Convert into binary", on_click=btn_click,),
                    ft.ElevatedButton("Divisors", on_click=btn_clickDiv),
                    ft.ElevatedButton("Number of divisors", on_click=btn_clickDivNo),
                    ft.ElevatedButton("Take a specific Divisor", on_click=btn_clickDivIndex),
                
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                 
            ),
            bgcolor=ft.colors.BLUE_200,
            width=1200,
            height=100,
            alignment=ft.alignment.center_right,
            border_radius= 50,
        )
    ) 
    page.add(
        ft.Container(
            ft.Row(
                [
                    ft.ElevatedButton("Convert a number to any base", on_click=btn_clickAnyToDec),
                    ft.ElevatedButton("Is Prime", on_click=btn_clickIsPrime),
                    ft.ElevatedButton("MCD", on_click=btn_clickMcdIndex),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor="#f4ebd3",
            width=1200,
            height=100,
            alignment=ft.alignment.center_right,
            border_radius= 50,
        )
    )
    returnbt



        

execute = ft.app(target=main)