from prometheus_client import Counter

bs_affiliate_new_counter = Counter('bs_affiliate_new_counter', 'New affiliates counter')
bs_affiliate_wrong_counter = Counter('bs_affiliate_wrong_counter', 'Wrong affiliates counter')
