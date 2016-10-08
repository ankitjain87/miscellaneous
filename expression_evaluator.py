"""Logical expression Evaluator. 
https://docs.google.com/document/d/16CKK4nL9peu2OORAVP4Gm8-N-8RCPiFv--0ku6jRibo/edit"""


def exp_and(left, right):
    return left and right


def exp_or(left, right):
    return left or right


def exp_not(left):
    return not left


def exp_eq(left, right):
    return left == right


def exp_gt(left, right):
    return left > right


def exp_lt(left, right):
    return left < right


def exp_in(left, right):
    return left in right


ops = {
    "AND": exp_and,
    "OR": exp_or,
    "NOT": exp_not,
    "EQ": exp_eq,
    "GT": exp_gt,
    "LT": exp_lt,
    "IN": exp_in
}


def get_value(obj, input_obj):
    if type(obj) == str:
        if obj.isdigit():
            return int(obj)

        try:
            obj1 = obj.split(".")
            data = input_obj
            for i in obj1:
                data = data[i]
            return data
        except KeyError:

            return obj

    return obj


def eval_expr(left, op, right):
    if op == "NOT":
        op = ops[op]
        if left:
            return op(left)
        else:
            return op(right)

    op = ops[op]
    return op(left, right)


def evaluate(expr, input_obj):
    op = expr[0]
    left = expr[1]
    right = expr[2]

    if op != "IN" and type(left) == list:
        left = evaluate(left, input_obj)

    if op != "IN" and type(right) == list:
        right = evaluate(right, input_obj)

    return eval_expr(get_value(left, input_obj), op, get_value(right, input_obj))


# Assuming the given user object will always have value like user.address.city or event.category.
input_obj = {
    "user": {
        "address": {
            "address_line": "XYZ Street",
            "city": "San Francisco",
            "state": "CA",
            "zipcode": "94150",
            "check": False
        }
    }
}

exp1 = ["NOT", ["EQ", "user.address.city", "10.5"], ["GT", "user.age", 35]]
exp2 = ["AND", ["IN", "user.address.city", ["infant", "child", "teen"]],["LT", "user.age", 18]]
exp3 = ["OR", ["EQ", "user.address.check", ["EQ", "user.address.city", "Los Angeles"]],["LT", "user.age", 18]]


print evaluate(exp1, input_obj)
print evaluate(exp2, input_obj)
print evaluate(exp3, input_obj)
