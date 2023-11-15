test_requests = [

    # Return form name
    {
        'order_date': '2023-01-01',
        'customer_phone': '+71234567890',
        'customer_email': 'example@mail.com',
        'order_item': 'iphone',
    },
    {
        'deliver_date': '2023-12-12',
        'customer_phone': '+71234567890',
        'address': 'Moscow',
    },
    {
        'birth_date': '18.06.1992',
        'user_phone': '+71234567890',
        'user_email': 'example@mail.com',
    },
    {
        'created_at_date': '01.01.2023',
        'candidate_email': 'example@mail.com',
        'job_title': 'CEO',
    },
    {
        'created_at_date': '2023-06-01',
        'hr_phone': '+71234567890',
        'hr_email': 'example@mail.com',
        'job_description': 'CTO',
    },
    {
        'created_at_date': '2023-06-01',
        'hr_phone': '+71234567890',
        'hr_email': 'example@mail.com',
        'job_description': 'CTO',
        'description': 'Hot vacancy',
    },

    # Return a requests fields with types
    {
        'order_date': '2023-01-01',
        'customer_phone': '+71234567890',
        'customer_email': 'example@mail.com',
    },
    {
        'just_field': '2023-12-12',
        'some_phone': '+71234567890',
        'description': 'Moscow',
    },
    {
        'smth': '18.06.1992',
        'summary': '+71234567890',
        'address': 'example@mail.com',
    },

    # Return a validation errors
    {
        'order_date': '2023/01/01',
        'customer_phone': '81234567890',
        'customer_email': 'example',
    },
    {
        'order_date': '2023.12.12',
        'some_phone': '71234567890',
        'customer_email': 'example@example.com',
    },

]

expected_results = [
    {'response': 'OrderForm', 'status': 200},
    {'response': 'DeliveryForm', 'status': 200},
    {'response': 'UserForm', 'status': 200},
    {'response': 'ResumeForm', 'status': 200},
    {'response': 'VacancyForm', 'status': 200},
    {'response': 'VacancyForm', 'status': 200},
    {'response': {'order_date': 'date', 'customer_phone': 'phone', 'customer_email': 'email'}, 'status': 200},
    {'response': {'just_field': 'date', 'some_phone': 'phone', 'description': 'text'}, 'status': 200},
    {'response': {'smth': 'date', 'summary': 'phone', 'address': 'email'}, 'status': 200},
    {'response': ["date data '2023/01/01' does not match format %Y-%m-%d' or '%d.%m.%Y'", "phone data 81234567890 does not match format '+7 xxx xx xx'", 'The email address is not valid. It must have exactly one @-sign.'], 'status': 422},
    {'response': ["date data '2023.12.12' does not match format %Y-%m-%d' or '%d.%m.%Y'", "phone data 71234567890 does not match format '+7 xxx xx xx'", 'The domain name example.com does not accept email.'], 'status': 422},
]

parametrized_values = list(zip(test_requests, expected_results))
