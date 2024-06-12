from collections import Counter


def get_count_visits_from_ip(ips):

    # ip_counts = Counter(ips)
    return Counter(ips)


def get_frequent_visit_from_ip(ips):
    ip_counts = Counter(ips)
    a = ip_counts.most_common(1)

    return a[0]
