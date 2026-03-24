from admin import Admin

admin_test = Admin("joao", "lima", ["pode deletar", "pode adicionar pessoa"])
admin_test.describe_user()
admin_test.privileges.show_privileges()
