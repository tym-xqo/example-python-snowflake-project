#!/usr/bin/env python
# -*- coding: utf-8 -*-
from raw import db
from pprint import pprint


def sample_query():
    sql = (
        "select id, name, email, created_at"
        "  from users "
        " where email not like '%benchprep%' "
        " order by created_at limit 10"
    )
    result = db.result(sql)
    return result


if __name__ == "__main__":
    data = sample_query()
    pprint(data)
