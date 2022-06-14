class Elements:
    # XPath
    warning_btn = '//*[@id="modern_app"]/div[2]/div/i[2]'
    new_first = '//*[@id="modern_content"]/div/div/div[2]/div[1]/div/div/div/span[1]'
                 
    # start_btn = '//*[@id="content"]/div/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[1]/div/div[2]/div[2]/div[2]/button'
    submit_btn = '//*[@id="content"]/div/div[1]/div[2]/div[2]/button'
    close_rating = '/html/body/div[6]/div/div[1]'
    out_btn = '//*[@id="content"]/div/div[1]/div[2]/div[2]/div/button'
    out_btn_confirm = '/html/body/div[6]/div/ul/li[2]'
    task = '/html/body/div[3]/main/div/div[2]/div[1]'
    spinner_xpath = '//*[@id="content"]/div/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[1]/div/div[2]/div[2]/div[2]/button/div/div[2]/div/div'
    login_btn = '//*[@id="header"]/header/div/div[2]/a/button'
    yes_btn = '/html/body/div/div/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/label'
    page_quality_bar = '/html/body/div/div/div/div[2]/div[1]/div/div[3]/span[4]/ins'
    # task_1 = '//*[@id="content"]/div/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[1]'
    # task_2 = '//*[@id="content"]/div/div[2]/div/div/div[2]/div[2]/div[1]/ul/li[2]'

    
    # CLASS NAME
    snipets = "snippets"
    snippet = "snippet"
    snippet_title = "snippet__title"
    spinner_class = 'spinner__circle'
    spinner_overlay = 'overlayed-spinner__overlay'
    start_btn = 'snippet__take-btn'
    modal_popup = 'base-modal-popup-header__title'

    # ID
    passp_field_login = 'passp-field-login'
    passp_sign_in = 'passp:sign-in'
    passp_field_passwd = 'passp-field-passwd'


    @staticmethod
    def get_radio_btn(task_id: int, page: int, btn_id: int) -> str:
        """Get the radio button of the page.

        Arguments:
            - task_id: The id of the task.
            - page: select 3 for the first page or 2 for the second and others pages
            - btn_id: radio button id (1, 2 or 3)
        
        Returns: The xpath of the radio button.
        
        Example:
        get_radio_btn(1, 3, 3) - get the third radio button on the second page in the first task
        """
        return  f"/html/body/div[{page}]/main/div/div[2]/div[{task_id}]/section/div[1]/form/div[1]/div[2]/div/div[{btn_id}]/div/button"