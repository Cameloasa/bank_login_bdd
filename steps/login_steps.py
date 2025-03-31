from behave import given, when, then

@given(u'användaren befinner sig på inloggningssidan')
def step_login_page_exists(context):
    context.page = "login_page"
    print("Användaren är på inloggningssidan")


@when(u'användaren anger sitt användarnamn och lösenord')
def step_enter_credentials(context):
    context.credentials = {"username": "testuser", "password": "password123"}
    print("Användaren har angett sina uppgifter.")

@when("användaren anger felaktigt användarnamn och lösenord")
def step_enter_invalid_credentials(context):
    context.credentials = {"username": "fel_anv", "password": "fel_los"}
    print("Användaren har angett felaktiga uppgifter.")

@when(u'användaren inte skriver in något alls')
def step_enter_nothing(context):
    context.credentials = {"username": "", "password": ""}
    print("Användaren har inte angett något.")

@when(u'klickar på logga in knappen')
def step_click_login(context):
    if context.credentials["username"] and context.credentials["password"]:
        if context.credentials["username"] == "testuser" and context.credentials["password"] == "password123":
            context.result = "success"
        else:
            context.result = "error"
    else:
        context.result = "empty"
    print("Användaren klickade på logga in.")

@then(u'blir användaren inloggad och kan se saldot på startsidan')
def step_verify_login_succes(context):
    assert context.result == "success", "Inloggning misslyckades!"
    print("Inloggningen lyckades!")

@then("visa ett felmeddelande om användarnamn och lösenord")
def step_verify_login_failure(context):
    assert context.result in ["error", "empty"], "Felmeddelandet visades inte!"
    print("Felmeddelande visas för felaktiga uppgifter.")


