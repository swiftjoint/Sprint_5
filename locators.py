from selenium.webdriver.common.by import By


class TestAutorisation:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Главная, кнопка 'Войти в аккаунт'
    REGISTER_BUTTON = (
        By.XPATH, "//a[text()='Зарегистрироваться']")  # Окно входа с полями майл и пароль, кнопка 'Зарегистрироваться'
    NAME_INPUT_XPATH = (
        By.XPATH, "//label[text()='Имя']/following-sibling::input[@name='name']")  # Окно регистрации, поле 'Имя'
    EMAIL_INPUT_XPATH = (
        By.XPATH, "//input[@name='name']")  # Окно регистрации, поле 'Email'
    PASSWORD_INPUT_XPATH = (By.XPATH, "//input[@name='Пароль']")  # Окно регистрации, поле 'Пароль'
    REGISTRATION_BUTTON_LOGIN = (
        By.XPATH, "//button[text()='Зарегистрироваться']")  # Окно регистрации, кнопка 'Зарегистрироваться'
    LOGIN_BUTTON_VIEW = (By.XPATH, "//button[text()='Войти']")  # Окно входа с полями майл и пароль, кнопка 'Войти'
    PASSWORD_ERROR = (
        By.XPATH, "//p[text() = 'Некорректный пароль']")  # Окно регистрации, сообщение о некорректном пароле
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Главная, кнопка 'Личный Кабинет'
    REGISTRATION_FORM_LOGIN_BUTTON = (By.XPATH, "//a[text()='Войти']")  # Окно регистрации, кнопка 'Войти'
    RESET_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")  # Окно входа, кнопка 'Восстановить пароль'
    AUTHORIZED_USER = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка 'Оформить заказ' авторизованный


class TestNavigationLocators:
    PROFILE_LINK_LOCATOR = (By.XPATH, "//a[text()='Профиль']")  # Страница личного кабинета
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Страница личного кабинете, кнопка 'Конструктор'
    BURGER_ASSEMBLY_HEADER = (
        By.XPATH, "//h1[text()='Соберите бургер']")  # Главная авторизованная страница, с конструктором
    STELLAR_BURGERS_LOGO_LOCATOR = (
        By.XPATH, './/div[contains(@class, "AppHeader_header__logo")]')  # по клику на логотип 'Stellar Burgers'
    LOGOUT_BUTTON = (
        By.XPATH, "//button[contains(@class, 'Account_button') or text()='Выход']")  # ЛК кнопка 'Выход'


class TestConstructorSections:
    BURGER_CONSTRUCTOR_ELEMENT = (By.XPATH, "//span[text()='Булки']")  # Конструктор, раздел 'Булки'
    SELECTED_BURGER_ELEMENT = (By.XPATH, "//h2[text()='Булки']")  # Конструктор, элемент 'Булки'
    SAUCES_CONSTRUCTOR_ELEMENT = (By.XPATH, "//span[text()='Соусы']")  # Конструктор, элемент 'Соусы'
    SELECTED_SAUCES_ELEMENT = (By.XPATH, "//h2[text()='Соусы']")  # Конструктор, элемент 'Соусы'
    FILLINGS_CONSTRUCTOR_ELEMENT = (By.XPATH, "//span[text()='Начинки']")  # Конструктор, раздел 'Начинки'
    SELECTED_FILLINGS_ELEMENT = (By.XPATH, "//h2[text()='Начинки']")  # Конструктор, раздел 'Начинки'
