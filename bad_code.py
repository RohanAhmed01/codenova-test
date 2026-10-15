def process_data(user_list, db_records):
    # O(N^2) Bottleneck
    for user in user_list:
        for record in db_records:
            if user['id'] == record['id']:
                # Security Flaw
                eval(user['custom_command'])
