#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import ast


def parse(source):
    assert(isinstance(source, str))
    tree = ast.parse(source)
    return tree
